from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from .models import *


# home
def home(request):
    return render(request, "home.html")

# Register
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        if pass1 != pass2:
            return redirect('register')
        try:
            if User.objects.get(username=username):
                return redirect('register')
        except Exception as ex:
            print(ex)
        try:
            if User.objects.get(email=email):
                return redirect('register')
        except Exception as ex:
            print(ex)
        todouser = User.objects.create_user(username,email,pass1)
        todouser.save()
        messages.success(request, 'Register Success Please login!')
        print('Register Success Please login!')
        return redirect('userlogin')
    messages.error(request, 'Already registered')
    print('Already registered')
    return render(request, "authentication/login.html")

# Login
def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password1']
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request,user)
            messages.success(request, 'Login successfully')
            print("Login successfully")
            return redirect('todo')
        else:
            messages.error(request, 'Incorrect Username (or) Password')
            print("Incorrect Password")
            return redirect('userlogin')
    return render(request, "authentication/login.html")

# Logout
def userlogout(request):
    logout(request)
    messages.success(request, 'Logout seccussfully')
    print("Logout seccussfully")
    return redirect('home')

# Profile
def profile(request):
    return render(request, "todolist/profile.html")

# To Do List
@login_required
def todo(request):
    incomplete_count = Todo_task.objects.filter(completed=False).count()
    view_list = Todo_task.objects.filter(user=request.user).order_by('-date')
    return render(request, "todolist/todolist.html", {'view_todo' : view_list, 'incomplete_count' : incomplete_count})

# Adding To Do List
@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        descr = request.POST['description']
        completed = request.POST.get('completed') == 'on'
        Todo_task.objects.create(title = title, description = descr, completed = completed,  user=request.user)
        messages.success(request, 'Your task is saved')
        print("Your task is saved")
        return redirect('todo')
    else:
        messages.info(request, 'Enter Your New Task')
        print("Your task is not saved")
        return render(request, "todolist/adding_todo.html")


# Editing To Do List
@login_required
def edit_task(request, task_id):
    edit_tsk = get_object_or_404(Todo_task, id = task_id, user = request.user)  
    if request.method == 'POST':
        title = request.POST.get('title')
        descr = request.POST.get('description')
        completed = request.POST.get('completed') == 'on'
        if title:
            edit_tsk.title = title
            edit_tsk.description = descr
            edit_tsk.completed = completed
            edit_tsk.save()
            messages.success(request, 'Task is Updated')
            print("Task is Updated")
            return redirect('todo')
        else:
            print("Task is not Updated")
            return render('edit_task')
    return render(request, "todolist/edit_todo.html", {'edit_tsk':edit_tsk})


# Completing To Do List
@login_required
def complete_task(request, task_id):
    complete_tsk = get_object_or_404(Todo_task, id = task_id, user = request.user)
    complete_tsk.completed = not complete_tsk.completed
    complete_tsk.save()
    return redirect('todo')


# Deleting To Do List
@login_required
def delete_task(request, task_id):
    delete_tsk = get_object_or_404(Todo_task, id = task_id, user = request.user)
    # delete_tsk.delete()
    if request.method == 'POST':
        delete_tsk.delete()
        messages.success(request, 'Task is Deleted')
        print("Task is Deleted")
        return redirect('todo')
    else:
        messages.warning(request, 'Permission For Deletion?')
        print("Task is Not Deleted")
        return render(request, "todolist/delete.html" , {'delete_tsk' : delete_tsk})


# Gopi@3343
# Rame@3343
# Aopi@1243
# Kuma@121
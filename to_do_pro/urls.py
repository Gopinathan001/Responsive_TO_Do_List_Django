"""
URL configuration for to_do_pro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from to_do_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('Sign_Up/', views.register, name="register"),
    path('Sign_In/', views.userlogin, name="userlogin"),
    path('Sign_Out/', views.userlogout, name="userlogout"),
    path('Profile/', views.profile, name="profile"),
    path('To_Do_List/', views.todo, name="todo"),
    path('Add_Your_Task/', views.add_task, name="add_task"),
    path('Update_Your_Task/<int:task_id>/', views.edit_task, name="edit_task"),
    path('Task_Completed/<int:task_id>/', views.complete_task, name="complete_task"),
    path('Delete_Your_Task/<int:task_id>/', views.delete_task, name="delete_task"),
]

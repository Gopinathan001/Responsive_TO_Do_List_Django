from django.db import models
from django.contrib.auth.models import User



class Todo_task(models.Model):
    user = models.ForeignKey( User, on_delete=models.CASCADE)
    id=models.AutoField(auto_created=True,primary_key=True)
    title = models.CharField(max_length = 200)
    completed = models.BooleanField(default = False)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class product(models.Model):
    seller=models.ForeignKey(User,on_delete=models.CASCADE,default=str(User.id)
    product_name=models.CharField(max_length=200,default='')
    description=models.CharField(max_length=600,default='')
    def __str__(self):
        return self.product_name
# class Item(models.Model):
#     todolist=models.ForeignKey(ToDoList,on_delete=models.CASCADE)
#     text=models.CharField(max_length=100)
#     complete=models.BooleanField()
#     def __str__(self):
#         return self.text     
    
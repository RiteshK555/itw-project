from django.db import models

# Create your models here.
class ToDoList(models.Model):
    product_name=models.CharField(max_length=00)
    def __str__(self):
        return self.name
class Item(models.Model):
    todolist=models.ForeignKey(ToDoList,on_delete=models.CASCADE)
    text=models.CharField(max_length=100)
    complete=models.BooleanField()
    def __str__(self):
        return self.text     
    
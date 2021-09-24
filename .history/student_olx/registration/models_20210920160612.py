from django.db import models
from django.contrib.auth import User
# Create your models here.
class money(models.Model):
    amount=models.IntegerField(default=0)
    holder=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
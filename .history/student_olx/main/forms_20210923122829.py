from django import forms
from .models import *
class CreateNewProduct(forms.ModelForm):
    class Meta:
        model=
    product_name=forms.CharField(label="Product Name",max_length=200)
    description=forms.CharField(label="Description",max_length=600)
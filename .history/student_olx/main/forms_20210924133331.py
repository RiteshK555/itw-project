from django import forms
from .models import *
class CreateNewProduct(forms.ModelForm):
    class Meta:
        model=product
        fields=['seller','product_name','description','price','product_img']
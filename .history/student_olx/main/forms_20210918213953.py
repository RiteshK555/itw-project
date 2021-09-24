from django import forms
class CreateNewProduct(forms.Form):
    product_name=forms.CharField(label="Name",max_length=200)
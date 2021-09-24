from django import forms
class CreateNewProduct(forms.Form):
    product_name=forms.CharField(label="Product Name",max_length=200)
    description=forms.Char(label="Description")
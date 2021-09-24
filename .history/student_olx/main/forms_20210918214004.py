from django import forms
class CreateNewProduct(forms.Form):
    product_name=forms.CharField(label="Product name",max_length=200)
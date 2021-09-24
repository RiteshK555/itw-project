from django import forms
class CreateNewProduct(forms.Form):
    product_name=forms.CharField(label="ProductName",max_length=200)
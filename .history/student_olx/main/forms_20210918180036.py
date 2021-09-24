from django import forms
class CreateNewProduct(forms.Form):
    name=forms.CharField(label="Name",max_length=200)
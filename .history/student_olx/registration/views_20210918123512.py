from django.shortcuts import render

# Create your views here.
def register(response):
    if response.method=="POST":
        form=UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            form=UserCreationForm()
    else:
        form=UserCreationForm()
    return render(response,"main/register.html",{"form":form})
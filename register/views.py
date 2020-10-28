from django.shortcuts import render , redirect
from register.forms import RegisterForm 
# Create your views here.

def register (response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
             user = form.save()
        user.refresh_from_db()
        user.profile.first_name = form.cleaned_data.get('first_name')
        user.profile.last_name = form.cleaned_data.get('last_name')
        user.profile.email = form.cleaned_data.get('email')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect("/home")    
    else:
        form = RegisterForm()    

    return render(response, "register/register.html", {"form" : form})
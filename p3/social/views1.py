from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from .forms import CreateUserForm

def CreateUser(req):
    if req.method == "POST":
        form = CreateUserForm(req.POST, req.FILES)

        if form.is_valid():
            username = req.POST['username']
            name = req.POST['name']
            password = req.POST['password']
            email = req.POST['email']
            birthdate = req.POST['birthdate']
            gender = req.POST['gender']

            if User.objects.filter(username=username):
                messages.error(
                    req, "User name already Exist!!"
                )
                return render(req, "ListUsers.html", {"form": form})

            user = User.objects.create_user(name, username, email, password,birthdate, gender)
            user.save()

            messages.success(req, "Your accunt is successfully created!!! Please check your email to confirm your email address in order to activate your account.")

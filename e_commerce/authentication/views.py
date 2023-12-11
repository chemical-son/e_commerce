from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# register new users
# /auth/register/ :POST
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password"]
        password2 = request.POST["confirm_password"]

        if username and email and password1 and password2:
            # check if passwords match each other
            if password1 != password2:
                messages.error(request, "password dosn't match!")

            try:
                user = User.objects.create_user(
                    username=username, email=email, password=password1
                )

            except:
                messages.error(request, "try defferant username or email!")

            if user is not None:
                login(request, user)
                return redirect("/auth/welcome/")

    return render(request, "authentication/register.html", {})


# login user to access the system
# /auth/login/ :POST
def login_user(request):
    if request.user.is_authenticated:
        return redirect("/shop/")

    if request.method == "POST":
        username = request.POST["username"].lower()
        password = request.POST["password"]

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exits")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/shop/")
        else:
            messages.error(request, "Usernaem or password does not correct")

    return render(request, "authentication/login.html", {})


# logout user
# /auth/logout/ :POST
def logout_user(request):
    logout(request)

    return redirect("/shop/")


# welcome page
# /auth/welcome/ :GET
def welcome(request):
    return render(request, "authentication/welcome.html", {})

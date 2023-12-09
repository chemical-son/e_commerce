from django.shortcuts import render

# register new users
# /auth/register/ :POST
def register(request):
    return render(request, 'authentication/register.html', {})

# login user to access the system
# /auth/login/ :POST
def login_user(request):
    return render(request, 'authentication/login.html', {})


# logout user
# /auth/logout/ :POST
def logout_user(request):
    return render(request, 'authentication/login.html', {})


from django.shortcuts import render

def home(request):
    return render(request, 'admin_dashboard/home.html', {})
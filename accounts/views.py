from django.shortcuts import render, redirect
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        # Login User
        return 
    return render(request, 'accounts/login.html')

def logout(request):
    return redirect('index')

def register(request):
    if request.method == 'POST':
        messages.error(request, 'Testing error message')
        # Register User
        return redirect('register')
    return render(request, 'accounts/register.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

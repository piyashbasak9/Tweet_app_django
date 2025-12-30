# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegisterForm, EmailAuthenticationForm
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # You can add email verification here if needed
            login(request, user)
            messages.success(request, f'Account created for {user.username}!')
            return redirect('tweet_list')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        # First try to authenticate with email
        email = request.POST['username']  # form uses 'username' field for email
        password = request.POST['password']
        
        # Check if a user exists with this email
        try:
            user_obj = User.objects.get(email=email)
            username = user_obj.username
        except User.DoesNotExist:
            username = email  # will fail authentication
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('tweet_list')
        else:
            messages.error(request, 'Invalid email or password.')
    
    return render(request, 'login.html', {'form': form})

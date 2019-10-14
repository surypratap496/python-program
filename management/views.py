from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import books,books_transactions



def signup(request):
    if request.POST:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')
        user = User()
        user.username = username
        user.email = email
        if password == confirm:
            try:
                user.set_password(password)
                user.save()
            except Exception as e:
                messages.error(request, "User already exists.")
                return redirect('signup')
            return redirect('login')

    return render(request, 'pages/signup.html')

def user_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'pages/login.html')

def index(request):
    return render(request, 'pages/home.html')

def contact(request):
    return render(request, 'pages/contact.html')

def about(request):
    return render(request, 'pages/about.html')

def user_logout(request):
    try:
        del request.session['username']
    except:
        pass
    logout(request)
    return redirect('login')

@login_required
def settings(request):
    return render(request, 'pages/settings.html')

@login_required
def profile(request):
    return render(request, 'pages/profile.html')

@login_required
def issued_books(request):
    user = request.user
    book_list = books_transactions.objects.filter(user_id=user.id)
    context = {'books': book_list}
    return render(request, 'pages/issued_books.html', context=context)

@login_required
def list_books(request):
    book_list = books.objects.all()
    context = {'books': book_list}
    return render(request, 'pages/list_books.html', context=context)

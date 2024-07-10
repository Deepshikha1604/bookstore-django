from django.shortcuts import render, redirect
from .models import Book, Genre
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms

def genre_summary(request):
   genres = Genre.objects.all()
   return render(request,'genre_summary.html',{'genres':genres})

def genre(request,foo):
   
    try:
        genre = Genre.objects.get(name=foo)
        books = Book.objects.filter(genre=genre)
        return render(request,'category.html',{'books':books, 'genre': genre})
    except:
        messages.success(request,("That genre does not exists."))
        return redirect('home')


def product(request,pk):
     product = Book.objects.get(id=pk)
     return render(request, 'product.html',{'product':product})


def home(request):
    books = Book.objects.all()
    return render(request,'home.html',{'books':books})


def about(request):
    return render(request, 'about.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,("You have been loged in."))
            return redirect('home')
        else:
            messages.success(request,("Error occured, check your usename and password."))
            return redirect('login')
    else:
        return render(request,'login.html',{})

def logout_user(request):
   logout(request)
   messages.success(request,("You have been loged out."))
   return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username = username, password=password)
            login(request,user)
            messages.success(request,("You have been registered successfully."))
            return redirect('home')
        else:
            messages.success(request,("Error occured,please try again."))
            return redirect('register')
    else:
        return render(request,'register.html',{'form':form})
    




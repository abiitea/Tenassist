from django.shortcuts import render

def home(request):
    return render(request, "tenassist/home.html",)

def login(request):
    return render(request, "tenassist/login.html",)
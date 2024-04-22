from django.shortcuts import render

def home(request):
    return render(request, "tenassist/home.html",)

def login(request):
    fg = 'admin'
    rvk = request.GET.get("revoke")
    return render(request, "tenassist/login.html",)
def register_patient(request):
    return render(request, "tenassist/register_patient.html",)
from django.shortcuts import render, redirect
from . forms import PatientRegistrationForm
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, "tenassist/home.html",)

def login(request):
    fg = 'admin'
    rvk = request.GET.get("revoke")
    return render(request, "tenassist/login.html",)
def register_patient(request):

    form = PatientRegistrationForm()
    is_patient = True
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST, request.FILES)
        
        if form.is_valid():

            form.save()

            return redirect("login")

    context = {'patient_form': form}
    return render(request, "tenassist/register_patient.html", context=context)

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Information
from .form import InformationForm, Registration
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, "hom.html")

@login_required()
def my_view(request):
    if request.method == 'POST':
        fm = InformationForm(request.POST)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect(reverse('home'))
    else:
        fm = InformationForm()

    data = Information.objects.order_by('firstname')
    context = {
        'form': fm,
        "data_info": data
    }
    return render(request, "home.html", context)


def delete_info(request, id):
    Information.objects.filter(id=id).delete()
    return render(request, 'confirm_delete.html')


def edit_info(request, id):
    if request.method == 'POST':
        obj = Information.objects.get(id=id)
        fm = InformationForm(request.POST, instance=obj)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect(reverse('success'))
    else:
        obj = Information.objects.get(id=id)
        fm = InformationForm(instance=obj)
    return render(request, 'updated.html', {'form': fm})


def success_page(request):
    return render(request, 'confirm_delete.html')


def registration(request):
    if request.method == 'POST':
        fm = Registration(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Account created Successfully!! ')
    else:
        fm = Registration()
    return render(request, "registration.html", context={"form": fm})


def login_user(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            login(request, user)
            messages.success(request, "user Login successfully!!")
            # return render(request, 'hom.html')
    else:
        fm = AuthenticationForm()
    return render(request, "login.html", {'form': fm})


def logout_user(request):
    logout(request)
    return render(request, 'login.html')


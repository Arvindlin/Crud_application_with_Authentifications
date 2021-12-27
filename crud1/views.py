from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Information
from .form import InformationForm, Registration
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


def home(request):
    return render(request, "hom.html")


@login_required(login_url='/login/')
def my_view(request):
    if request.method == 'POST':
        fm = InformationForm(request.POST)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect(reverse('my_view'))
    else:
        fm = InformationForm()

    data = Information.objects.filter(user=request.user)
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
            request.session['username'] = uname
            return render(request, 'hom.html')
    else:
        fm = AuthenticationForm()
    return render(request, "login.html", {'form': fm})


def logout_user(request):
    logout(request)
    return render(request, 'logout.html')


def change_password(request):
    if request.method == 'POST':
        fm = PasswordChangeForm(user=request.user, data=request.POST)
        if fm.is_valid():
            user = fm.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Your Password was successfully updated")
            return redirect('home')
        else:
            messages.error(request, 'please correct the error below')
    else:
        fm = PasswordChangeForm(user=request.user)
    return render(request, 'passwordchange.html', {'form': fm})

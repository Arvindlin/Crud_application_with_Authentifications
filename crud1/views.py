from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Information, Profile
from .form import InformationForm, Registration, ProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from djangoProject1 import settings
from django.core.mail import send_mail


def home(request):
    '''It will render to home page.'''
    return render(request, "hom.html")


@login_required(login_url='/login/')
def my_view(request):
    '''This is for main CRUD application. To create and Retrive the data on html page.'''
    if request.method == 'POST':
        obj = User.objects.get(pk=request.user.id)
        print(obj)
        fm = InformationForm(request.POST)
        # print(fm)
        if fm.is_valid():
            # fm.save(context=request)
            new_key = fm.save()
            add_value = Information.objects.get(id=new_key.pk)
            add_value.user = obj
            add_value.save()
            # print(add_value)

        return HttpResponseRedirect(reverse('my_view'))
    # else:
        # obj = User.objects.get(pk=request.user.id)
        # print(obj)
        # inf = Information.objects.get(user = obj)
        # fm = InformationForm(instance=request.user)
        # fm.user = request.session['username']
        # print(fm.user)
    else:
        obj = User.objects.get(pk = request.user.id)
        # print(obj.id)
        # pf = Information.objects.get(user_id=obj.id)
        fm = InformationForm(instance=obj)
        # print(pf)
        fm.id = obj
        # print(fm)
    data = Information.objects.filter(user=request.user)
    # print(img)
    context = {
        'form': fm,
        "data_info": data,
        # 'Image':img,
    }
    return render(request, "home.html", context)


def delete_info(request, id):
    '''This view is to delete the selected information. '''
    Information.objects.filter(id=id).delete()
    return render(request, 'confirm_delete.html')


def edit_info(request, id):
    '''This view is to edit/Update the table of the CRUD App.'''
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
    '''To send the user to suceessful page after delete the Row of table.'''
    return render(request, 'confirm_delete.html')


def registration(request):
    '''For sign-up/Registeration of new user.'''
    if request.method == 'POST':
        fm = Registration(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Account created Successfully!! ')
            subject = 'Welcome to site'
            message1 = 'Thanks for registration'
            send_mail(subject, message1, settings.EMAIL_HOST_USER, [request.POST['email']], fail_silently=False)
    else:
        fm = Registration()
    return render(request, "registration.html", context={"form": fm})


def login_user(request):
    '''To log in the user through log-in page.'''
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
    '''To log-out the user.'''
    logout(request)
    return render(request, 'logout.html')


def change_password(request):
    '''To change the password through when user is logged in.'''
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


@login_required()
def upload_image(request):
    '''To upload the image through this view'''
    if request.method == 'POST':

        # user = User.objects.filter(pk =request.user.id)
        fm = ProfileForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            # obj = Profile.objects.get(pk=request.user.id)
            # obj = Information.objects.get(user = request.session['username'])
            # obj = Information.objects.get(user_id = request.user.id)
            # new_obj= fm.save()
            # add_new = Profile.objects.get(id=new_obj.pk)
            # add_new.user = obj.user
            # add_new.save()

    else:
        user = User.objects.get(pk = request.user.id)
        # print(user)
        pf = Profile.objects.get(user = user)
        # print(pf)
        fm = ProfileForm(instance=pf)
        fm.user = user
        # print(fm.user)

    return render(request, 'upload.html', {'form': fm})

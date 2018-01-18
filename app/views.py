from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import *
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def main(request):
    par = {
        'header': 'Main page'
    }
    return render(request, 'MainPage.html', context=par)


def user_registered(request):
    return render(request, 'registered.html')


class RegistrationForm(forms.Form):
    username = forms.CharField(min_length=5, label='Логин')
    password = forms.CharField(min_length=6, widget=forms.PasswordInput, label='Пароль')
    password2 = forms.CharField(min_length=6, widget=forms.PasswordInput, label='Повторите ввод')
    last_name = forms.CharField(label='Фамилия')
    first_name = forms.CharField(label='Имя')
    email = forms.EmailField(label='Email')


def registration_1(request):
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        is_val = form.is_valid()
        data = form.cleaned_data
        if data['password'] != data['password2']:
            is_val = False
            form.add_error('password2', ['Пароли должны совпадать'])
        if User.objects.filter(username=data['username']).exists():
            form.add_error('username', ['Такой логин уже занят'])
            is_val = False
        if is_val:
            new_user = User.objects.create_user(data['username'], data['email'], data['password'])
            print(new_user)
            user1 = User1()
            user1.user1 = new_user
            user1.email = data['email']
            user1.last_name = data['last_name']
            user1.first_name = data['first_name']
            user1.save()
            return HttpResponseRedirect('/registered')
        else:
            form = RegistrationForm()
    return render(request, 'registration_1.html', {'form': form})


def registration_form(request):
    errors = {}
    if request.method == 'POST':
        last_name = request.POST.get('last_name')
        if not last_name:
            errors['last_name'] = 'Введите Фамилию'

        first_name = request.POST.get('first_name')
        if not first_name:
            errors['first_name'] = 'Введите имя'

        email = request.POST.get('Email')
        if not email:
            errors['Email'] = 'Введите Email'

        username = request.POST.get('username')
        if not username:
            errors['username'] = 'Введите логин'
        elif len(username) < 8:
            errors['username'] = 'Длина логина должна превышать 5 символов'
        if User.objects.filter(username=username).exists():
            errors['username'] = 'Данный логин занят'

        password = request.POST.get('password')
        if not password:
            errors['password'] = 'Введите пароль'
        elif len(password) < 8:
            errors['password'] = 'Длина пароля должна превышать 6 символов'
        password_repeat = request.POST.get('password2')
        if password != password_repeat:
            errors['password_repeat'] = 'Пароли не совпадают'
        print(username, password, "1")

        if not errors:
            new_user = User.objects.create_user(username, email, password)
            print(new_user)
            user1 = User1()
            user1.user1 = new_user
            user1.email = email
            user1.last_name = last_name
            user1.first_name = first_name
            user1.save()
            return HttpResponseRedirect('/registered')
        else:
            context = {'errors': errors, 'username': username, 'email': email, 'last_name': last_name,
                       'first_name': first_name, 'password': password, 'password_repeat': password_repeat}
            return render(request, 'registration.html', context)
    return render(request, 'registration.html', {'errors': errors})


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')


def log_in(request):
    errors = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        if not username:
            errors['username'] = 'Введите логин'
        elif len(username) < 5:
            errors['username'] = 'Слишком короткий логин. Минимальная длина-5 знаков'

        password = request.POST.get('password')
        if not password:
            errors['password'] = 'Введите пароль'
        elif len(password) < 8:
            errors['password'] = 'Слишком короткий пароль. Минимальная длина-8 знаков'

        user = authenticate(request, username=username, password=password)
        print(user)
        if user is None and 'username' not in errors.keys() and 'password' not in errors.keys():
            errors['login'] = 'Логин или пароль введены неверно'

        if not errors:
            login(request, user)
            return HttpResponseRedirect('/logged_in')
        else:
            context = {'errors': errors}
            return render(request, 'UserLogin.html', context)
    return render(request, 'UserLogin.html', {'errors':errors})


def log_in1(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print(form)
        data = form.cleaned_data

        if form.is_valid():
            user = authenticate(request, username=data['username'], password=data['password'])
            print(len(data['username']), len(data['password']))
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/logged_in')
            else:
                form.add_error('username', ['Неверный логин или пароль'])
    else:
        form = LoginForm()
    return render(request, 'UserLogin_1.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'MainPage.html')


@login_required(login_url='/login2')
def logged_in(request):
    return render(request, 'loggedin.html')


def logged_in_view(request):
    if request.user.is_authenticated:
        return render(request, 'loggedin.html')
    else:
        return HttpResponseRedirect('/login1')

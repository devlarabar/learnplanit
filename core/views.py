from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
import core.helpers.request_helpers as helpers
from core.forms.account_forms import CustomSignupForm
from lessons.models import Subject


def index(request):
    context = helpers.prepare_context(request)
    context['title'] = None
    return render(request, 'core/index.html', context)


def login_view(request):
    context = helpers.prepare_context(request)

    context['form'] = AuthenticationForm(request.POST or None)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print(f"{username} logged in!")
            return redirect(request.GET.get('next', 'index'))
        else:
            context['error'] = "Invalid Credentials!"

    return render(request, "core/login.html", context=context)


def logout_view(request):
    context = helpers.prepare_context(request)
    user_id = helpers.get_user_id(request)
    print(f"User: {context['username']} ({user_id}) logged out!")
    logout(request)
    return redirect('index')


def signup_view(request):
    context = helpers.prepare_context(request)

    form = CustomSignupForm(None)
    context['valid_signup'] = False
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            un, pw = form.save()
            messages.success(request, 'Account created successfully')
            user = authenticate(username=un, password=pw)
            if user is not None:
                login(request, user)
                return redirect('index')
        else:
            print(form.errors)
            context['valid_signup'] = False
            context['form_errors'] = form.errors
            return render(request, "core/signup.html", context=context)

    context['form'] = form

    return render(request, "core/signup.html", context=context)

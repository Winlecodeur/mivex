from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse

def login(request):
    form = AuthenticationForm(request, request.POST or None)
    if request.method  == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('admin')
            else :
                return HttpResponse ('erreur de mot de passe ou username ou les deux')
    else :
        form = AuthenticationForm()
    return render (request, 'login.html', {'form':form})
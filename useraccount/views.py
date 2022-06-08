from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from useraccount.forms import SignUpForm
from django.contrib import messages
# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')
    
def login_view(request):
    form= AuthenticationForm(request.POST or None)
    if request.POST:
        username=request.POST.get("username")
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #return HttpResponseRedirect(reverse(''))
            return HttpResponseRedirect('/admin/')
        else:
            messages.info(request, 'Username or Password is Incorrect')
    context={'form':form}
    return render(request, 'login.html', context)

def register_view(request):
    form=SignUpForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, user+ ', Your account have successfully created.')
            return HttpResponseRedirect(reverse('user:login'))
    context={'form':form}
    return render(request, 'register.html' ,context)
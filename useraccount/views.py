
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.
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
    context={'form':form}
    return render(request, 'login.html', context)
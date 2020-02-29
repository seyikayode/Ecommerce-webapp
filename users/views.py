from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            mobile = request.POST['mobile']
            email = request.POST['email']
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, first_name=first_name, last_name=last_name, mobile=mobile, email=email,
                                username=username, password=password)
            login(request, user)
            messages.success(request, f'Welcome {username}!')
            return redirect('home')
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)

from django.shortcuts import render, redirect   # to change the route
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages     #like toastr message.error, debug, info, warning, success
from django.contrib.auth.decorators import login_required 
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)   # using our custom defined form 
        if form.is_valid():
            form.save()     # to add that to database
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created! You can login now.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')
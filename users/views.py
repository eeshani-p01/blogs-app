from django.shortcuts import render, redirect   # to change the route
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages     #like toastr message.error, debug, info, warning, success

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blogs-home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
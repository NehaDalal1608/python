from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Simulate saving user to database
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            messages.success(request, f'Registration successful for {username}!')
            return redirect('register')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})

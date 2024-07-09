from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserCreationForm, RecordForm
from .models import Record


def home(request):
    records = Record.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in')
            return redirect('home')
        else:
            messages.error(request, 'Couldn\'t log in...')
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})

def logout_user(request):
    logout(request)
    messages.info(request, 'You have successfully logged out...')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Basic validation
        if not (username and name and email and password1 and password2):
            messages.error(request, 'All fields are required.')
            return render(request, 'register.html')

        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'register.html')

        # Create the user
        try:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.first_name = name
            user.save()
            messages.success(request, 'You have successfully registered.')
            # Log in the user
            login(request, user)
            return redirect('home')
        except Exception as e:
            messages.error(request, f'Failed to register: {str(e)}')
            return render(request, 'register.html')
    return render(request, 'register.html')

def view_record(request, pk):
    if(request.user.is_authenticated):
        record = Record.objects.get(id=pk)
        return render(request, 'view_record.html', {'record': record})
    else:
        messages.error(request, 'You must be logged in to view this page')
        return redirect('home')

def delete_record(request, pk):
    if(request.user.is_authenticated):
        record = Record.objects.get(id=pk)
        record.delete()
        messages.info(request, 'Record deleted successfully...')
        return redirect('home')
    else:
        messages.error(request, 'You must be logged in to view this page')
        return redirect('home')

def add_record(request):
    if(request.user.is_authenticated):
        form = RecordForm(request.POST or None)
        if request.method == 'POST':
            form = RecordForm(request.POST)
            if form.is_valid():
                add_record = form.save()
                messages.success(request, 'Record added successfully...')
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.error(request, 'You must be logged in to view this page')
        return redirect('home')
    
def update_record(request, pk):
    if(request.user.is_authenticated):
        record = Record.objects.get(id=pk)
        form = RecordForm(instance=record)
        if request.method == 'POST':
            form = RecordForm(request.POST, instance=record)
            if form.is_valid():
                form.save()
                messages.success(request, 'Record updated successfully...')
                return redirect('home')
        return render(request, 'update_record.html', {'form': form, 'record': record})
    else:
        messages.error(request, 'You must be logged in to view this page...')
        return redirect('home')
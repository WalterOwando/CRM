from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

def home(request):
    records = Record.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('home')
    return render(request, 'home.html', {'records': records})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered. Welcome!")
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        try:
            customer_record = Record.objects.get(id=pk)
            return render(request, 'record.html', {'customer_record': customer_record})
        except Record.DoesNotExist:
            messages.error(request, "Record does not exist.")
            return redirect('home')
    else:
        messages.error(request, "You must be logged in to view this page.")
        return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        try:
            record = Record.objects.get(id=pk)
            record.delete()
            messages.success(request, "Record deleted successfully.")
        except Record.DoesNotExist:
            messages.error(request, "Record does not exist.")
    else:
        messages.error(request, "You must be logged in to delete records.")
    return redirect('home')

def add_record(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddRecordForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Record added successfully.")
                return redirect('home')
        else:
            form = AddRecordForm()
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.error(request, "You must be logged in to add records.")
        return redirect('home')

def update_record(request, pk):
    if request.user.is_authenticated:
        try:
            record = Record.objects.get(id=pk)
            form = AddRecordForm(request.POST or None, instance=record)
            if form.is_valid():
                form.save()
                messages.success(request, "Record updated successfully.")
                return redirect('home')
            return render(request, 'update_record.html', {'form': form})
        except Record.DoesNotExist:
            messages.error(request, "Record does not exist.")
    else:
        messages.error(request, "You must be logged in to update records.")
    return redirect('home')

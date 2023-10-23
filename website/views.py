from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.

def home(request):
    records = list(Record.objects.all())
    #check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #authinticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
        return redirect('home')
            
    else:
        return render(request, 'home.html', {'records':records})


def logout_user(request):
    logout(request)
    messages.success(request, "You Are Logged out!")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, "You Have Succesfully Registered...")
            return redirect('home')
        
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        #look up record
        customer_record1 = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record1})
    else:
        messages.success(request, "You Must Be Logged In!")
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Records Delete Successfully.")
        return redirect('home')
    else:
        messages.success(request, "You Must Be Logged In!")
        return redirect('home')

def add_record(request):
    form = AddRecordForm(request.POST or None)#same as in line 34
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Record Added")
                return redirect('home')
        else:
            return render(request, 'add_record.html' ,{'form':form})
    else:
        messages.success(request, "You Must Be Logged In!")
        return redirect('home')


from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CreateUserForm,Loginform,AddRecordForm,UpdateRecordForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Record
from django.contrib import messages
def home(request):
    return render(request,'webapp/index.html')

def register(request):
    form=CreateUserForm()
    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'You are now registered')
            return redirect('my-login')
    context={'form':form}
    return render(request,'webapp/register.html',context)    

def my_login(request):
    form = Loginform()
    if request.method=='POST':
        form = Loginform(request.POST,data=request.POST)
        if form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username = username,password = password)
            if user is not None:
                auth.login(request,user)
                messages.success(request,'Logged in success!')
                return redirect('dashboard')
    context={'form':form}
    return render(request,'webapp/my-login.html',context)            
 
def user_logout(request):
    auth.logout(request)
    messages.success(request,'logged out!')
    return redirect('my-login')
#  ---Dashboard---
@login_required(login_url='my-login')
def dashboard(request):
    my_record=Record.objects.all()
    context={'records':my_record}
    return render(request,'webapp/dashboard.html',context)
#--Create a record--
@login_required(login_url='my-login')
def create_record(request):
    form = AddRecordForm()
    if request.method=='POST':
        form = AddRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Record added ')
            return redirect('dashboard')
    context={'form':form}
    return render(request,'webapp/create-record.html',context)    

@login_required(login_url='my-login')
def update_record(request,pk):
    record=Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)
    if request.method=='POST':
        form = UpdateRecordForm(request.POST,instance=record)
        if form.is_valid():
            form.save()
            messages.success(request,'Record updated')
            return redirect('dashboard')
    context={'form':form}
    return render(request,'webapp/update-record.html',context)    

@login_required(login_url='my-login')
def view_record(request,pk):
    record=Record.objects.get(id=pk)
    context={'record':record}
    return render(request,'webapp/view-record.html',context)

@login_required(login_url='my-login')
def delete_record(request,pk):
    record=Record.objects.get(id=pk)
    record.delete()
    messages.success(request,'Record deleted!')
    return redirect('dashboard')

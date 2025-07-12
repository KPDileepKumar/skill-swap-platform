from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .utils import searchProfiles,paginateProfiles
# Create your views here.

def loginUser(request):
    
    if request.user.is_authenticated:
        return redirect('profiles')
    flag=0
    if request.method=="POST":
        username=request.POST['username'].lower()
        password=request.POST['password']
        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request,"User does not exist")
            flag=1
            
        if not flag:
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect(request.GET['next'] if 'next' in request.GET else 'account')
            else:
                messages.error(request,"Username OR Password is incorrect")
    page='login'
    context={'page':page}
    return render(request,"users/login_register.html",context)

def logoutUser(request):
    logout(request)
    messages.info(request,"User was logged out")
    return redirect('login')

def profiles(request):
    profiles,search_query=searchProfiles(request)
    custom_range,profiles=paginateProfiles(request,profiles,6)
    context={'profiles':profiles,'search_query':search_query,'custom_range':custom_range}
    return render(request,"core/profiles.html",context)
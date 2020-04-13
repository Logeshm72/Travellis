from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User ,auth
# Create your views here.

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)


        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials!!!') 
            return redirect('login')   


    else:
        return render(request,'login.html')





def register(request):

    if request.method =='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                #print('User name is already Taken!!!')
                messages.info(request,'Username is already taken!!!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():    
                #print('Email is taken!!')
                messages.info(request,'Email is taken!!')
                return redirect('register')
            else:    
                user =User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                #print('user created!')
                messages.info(request,'user created!')
                return redirect('login') 
        else:
             #print('Password is not matching---check it!!')
             messages.info(request,'Password is not matching---check it!!')
             return redirect('register')

    return render(request,'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

#from google.cloud import recaptchaenterprise_v1
#from google.cloud.recaptchaenterprise_v1 import Assessment


# Create your views here.



def index(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password =password  )

        if user is not None:
            auth.login(request , user)
            return redirect('/navbar')
        else:
            messages.info(request, 'invalid username or password')
            return redirect("/")
    else:
        return render(request,'index.html')


def register(request):

    if request.method == 'POST':

        email = request.POST['email']
        username = request.POST['username']
        password= request.POST['password']


        user = User.objects.create_user(username = username , password = password , email = email)
        user.save()
        print('user created')
        return redirect('/custom')

    return render(request,'register.html')


def custom(request):
    return render(request, 'custom.html')

def navbar(request):
    return render(request,'navbar.html')

def home(request):
    return render(request, 'home.html')

def account(request):
    return render(request, 'account.html')

def balance(request):
    return render(request, 'balance.html')

def history(request):
    return render(request, 'history.html')

def transaction(request):
    return render(request, 'transaction.html')

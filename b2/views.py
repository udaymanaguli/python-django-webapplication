from django.contrib import auth
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.db.backends import mysql
from django.shortcuts import render, redirect
import mysql.connector
from django.utils.datastructures import MultiValueDictKeyError
from .forms import saved
from django.contrib import messages
import b2.models
from .models import Vote, Choice, Option
from twilio.rest import Client
import random


def home(request):
    return render(request, "index.html")


val = None
pho = None
otn = None


def register(request):
    if request.method == 'POST':
        username1 = request.POST['i']
        password1 = request.POST['pass']
        password2 = request.POST['Cpass']
        date = request.POST['dob']
        phone = request.POST['num']
        if password1 == password2:
            usern = int(username1)
            y = Vote.objects.filter(identity=usern).exists()
            if y is False:
                return redirect('register')
            else:
                d = Vote.objects.filter(dob=date).exists()
                if d is False:
                    return redirect('register')
                else:
                    p = Vote.objects.filter(phone=phone).exists()
                    if p is False:
                        return redirect('register')
                    else:
                        f = User.objects.filter(username=username1).exists()
                        if f is False:
                            x = User.objects.create_user(username=username1, first_name=password1, last_name=phone)
                            x.save()
                            return redirect('home')
                        else:
                            return redirect('register')
        else:
            return redirect('register')
    else:
        return render(request, "register111.html")


def login(request):
    if request.method == 'POST':
        identities = request.POST.get('identi')
        pass11 = request.POST.get('pass1')
        phone_num = request.POST.get('numb')
        global pho
        pho = phone_num
        global val
        val = identities
        f = User.objects.filter(username=identities).exists()
        g = User.objects.filter(first_name=pass11).exists()
        if f is False:
            return redirect('home')
        else:
            if g is False:
                return redirect('login')
            else:
                h = Option.objects.filter(cidentity=identities).exists()
                if h is False:
                    return render(request, "verify.html")
                else:
                    return redirect('home')
    else:
        return render(request, "login1111.html")


def voting(request):
    if request.method == 'POST':
        global val
        num = val
        choi = request.POST.get('cho')
        reg = Option()
        reg.cidentity = num
        reg.choice = choi
        reg.save()
        return redirect('home')
    else:
        return render(request, "voting111.html")


def otp(request):
    if request.method == 'POST':
        otp21 = request.POST['o1']
        otp22 = request.POST['o2']
        otp23 = request.POST['o3']
        otp24 = request.POST['o4']
        otp25 = otp21 + otp22 + otp23 + otp24
        otp2 = int(otp25)
        if otn == otp2:
            return render(request, "votingcast.html")
        else:
            return redirect('login')
    else:
        return render(request, "otp11.html")


def send(request):
    otp1 = int(random.randint(1000, 9999))
    global otn
    otn = otp1
    account_sid = 'xxxxx'
    auth_token = 'xxxxxx'
    client = Client(account_sid, auth_token)
    message = client.messages.create(

        body=f"Your OTP is {otp1}",
        from_="+15617821580",
        to=f'{pho}'
    )
    return render(request, "otn.html")

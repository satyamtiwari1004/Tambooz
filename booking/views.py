from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/signin/')
def booking(request):
    return render(request,'booking/mybookings.html')
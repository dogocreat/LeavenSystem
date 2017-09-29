from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import *

from .models import DatePost
from django.contrib.auth.models import User
from django.contrib import auth
from datetime import datetime
# Create your views here.


def index(request):
    if request.user.is_authenticated():
        page = 'home'
        return render(request, 'home.html', locals())

    return render(request, 'login.html', locals())


def login(request):
    if request.user.is_authenticated():
        page = 'home'
        return render(request, 'home.html', locals())

    if 'username' in request.POST and 'password' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            page = 'home'
            return render(request, 'home.html', locals(),)
        else:
            return render(request, 'login.html', locals())


def leavenList(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html', locals())
    page = 'leavenList'
    dataList = DatePost.objects.filter(author=request.user)
    for data in dataList:
        data.timeRange = DatePost.TimeOptions[0][1] if DatePost.TimeOptions[0][0] == data.timeRange else DatePost.TimeOptions[1][1]

    return render(request, 'home.html', locals())


def addLeavenForm(request):
    if not request.user.is_authenticated():
        return render(request,'login.html', locals())
    page = 'LeavenForm'
    action_staut = 'add'
    now = datetime.now().strftime("%Y-%m-%d")
    timeOptions = DatePost.TimeOptions
    depOptions = DatePost.DepOptions
    return render(request, 'home.html', locals())


def submitLeavenForm(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html', locals())
    datePost = DatePost()
    datePost.author = request.user
    datePost.dep = request.POST['SelectDep']
    datePost.leaveDate = request.POST['LeavenDate']
    datePost.timeRange = request.POST['TimeRange']
    datePost.save()
    return redirect('/leavenList/')
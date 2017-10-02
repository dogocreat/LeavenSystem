from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import *
from django.core import serializers

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
    # print serializers.serialize('json',dataList)
    for data in dataList:
        data.timeRange = DatePost.TimeOptions[0][1] if DatePost.TimeOptions[0][0] == data.timeRange else DatePost.TimeOptions[1][1]
        data.leaveDate = data.leaveDate.strftime("%Y-%m-%d")

    return render(request, 'home.html', locals())


def addLeavenForm(request):
    if not request.user.is_authenticated():
        return render(request,'login.html', locals())
    page = 'LeavenForm'
    action_status = 'add'
    now = datetime.now().strftime("%Y-%m-%d")
    timeOptions = DatePost.TimeOptions
    depOptions = DatePost.DepOptions
    return render(request, 'home.html', locals())

def editLeavenForm(request,id):
    if not request.user.is_authenticated():
        return render(request,'login.html', locals())
    page = 'LeavenForm'
    action_status = 'edit'
    timeOptions = DatePost.TimeOptions
    depOptions = DatePost.DepOptions
    dataPost = DatePost.objects.get(pk=id)
    dataPost.leaveDate = dataPost.leaveDate.strftime("%Y-%m-%d")
    return render(request, 'home.html', locals())


def submitLeavenForm(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html', locals())
    if(request.POST['status'] == "edit"):
        id = request.POST['post_id']
        if DatePost.objects.filter(pk=id).exists():
            datePost = DatePost.objects.get(pk=id)
            datePost.author = request.user
            datePost.dep = request.POST['SelectDep']
            datePost.leaveDate = request.POST['LeavenDate']
            datePost.timeRange = request.POST['TimeRange']
            datePost.comment = request.POST['comment']
            datePost.save()
    else:
        datePost = DatePost.objects.get_or_create(
            author = request.user,
            dep = request.POST['SelectDep'],
            leaveDate = request.POST['LeavenDate'],
            timeRange = request.POST['TimeRange'],
            comment = request.POST['comment'],
        )
        # datePost.author = request.user
        # datePost.dep = request.POST['SelectDep']
        # datePost.leaveDate = request.POST['LeavenDate']
        # datePost.timeRange = request.POST['TimeRange']
        # datePost.save()
    return redirect('/leavenList/')

def delLeavenForm(request,id):
    if DatePost.objects.filter(pk=id).exists():
        print "--------------------------------------is exists"
        dataPost = DatePost.objects.get(pk=id)
        dataPost.delete()
    return redirect('/leavenList/')

def logout(request):
    auth.logout(request)
    return redirect('/')
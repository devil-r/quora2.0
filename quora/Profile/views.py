from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.db.models import Q
from .forms import Edit_info
from .models import User_info
from account.models import Account
from homepage.models import Bookmark ,Question
from homepage.models import A_info
# Create your views here.
def index(request):
    ans = A_info.objects.all()
    a = []
    for a_i in ans:
        if a_i.answer.user == request.user:
            a.append(a_i)
    if request.POST:
        que = Question()
        que.title = request.POST['question']
        que.user = request.user
        que.save()
        print("Question added to database")
    account = Account.objects.filter(user = request.user)[0]
    u_info = User_info()
    if User_info.objects.filter(user  = request.user).count()!=0:
        u_info=User_info.objects.filter(user  = request.user)[0]
    ctx = {"a_info" : a
            ,"account" : account, "user_info" : u_info}

    return render(request,'index.html' , ctx)

def editprofile(request):
    form = Edit_info()
    if request.POST:
        user = request.user
        account = Account.objects.filter(user=user)[0]
        account.age = request.POST.get('age')
        # account.gender = request.POST.get('gender')
        # print('gender: ',request.POST.get('gender'))
        account.address = request.POST.get('address')
        account.save()
        if User_info.objects.filter(user=user).count()==0:
            u_info = User_info(
             user = user,
             description = request.POST.get('description'),
             education = request.POST.get('education')
            )
            u_info.save()
        else:
            u_info = User_info.objects.filter(user=user)[0]
            u_info.description = request.POST.get('description')
            u_info.education = request.POST.get('education')
            u_info.save()

        return redirect('/profile')
    ctx = {'form' : form}
    return render ( request , 'edit.html',ctx )

def bookmarks(request):
    booook = Bookmark.objects.filter(user = request.user)
    a_info = []
    accounts = {}
    for bo in booook:
        ans = bo.answer
        info = A_info.objects.filter(answer = ans)[0]
        a_info.append(info)
        accounts[info] = Account.objects.filter(user = info.answer.user)[0].username
    if request.POST:
        que = Question()
        que.title = request.POST['question']
        que.user = request.user
        que.save()
        print("Question added to database")
    account = Account.objects.filter(user = request.user)[0]
    u_info = User_info()
    if User_info.objects.filter(user  = request.user).count()!=0:
        u_info=User_info.objects.filter(user  = request.user)[0]
    ctx = {"a_info" : a_info
            ,"account" : account, "user_info" : u_info ,"accounts":accounts}
    return render(request,'bookmark.html' , ctx)

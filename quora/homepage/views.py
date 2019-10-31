from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from .models import Answer, Question ,A_info ,Q_info , Bookmark ,Upvotes
from django.db.models import Q
from .forms import Answer_handler
from django.contrib import messages
from account.models import Account
# Create your views here.

def feeds(request):
    if not request.user.is_authenticated:
        return redirect('/auth')

    if request.POST:
        que = Question()
        que.title = request.POST['question']
        que.user = request.user
        que.save()
        print("Question added to database")
    answers = A_info.objects.all()
    a = []
    accounts = {}
    c=1
    account = Account.objects.filter(user = request.user)[0]
    for ans in answers:
        if ans.answer.user != request.user:
            a.append(ans)
            accounts[ans] = Account.objects.filter(user =ans.answer.user)[0].username

    ctx = {
        "user": request.user,
        "answers": a,
        "accounts": accounts,
        "account": account,
        "c": c
    }
    return render(request, 'feeds.html', ctx)

def answers(request):
    if request.POST:
        que = Question()
        que.title = request.POST['question']
        que.user = request.user
        que.save()
        print("Question added to database")
    ques = Question.objects.filter(~Q(user=request.user))
    f_ques = []
    for question in ques:
        ans = Answer.objects.filter(question = question)
        users = []
        for an in ans:
            users.append(an.user)
        if request.user not in users:
            f_ques.append(question)
    print('len',len(f_ques))
    ctx = {"questions" : f_ques}
    return render (request,'answers.html',ctx)


def questions(request):
    if not request.user.is_authenticated:
        return redirect('/auth')

    if request.POST:
        que = Question()
        que.title = request.POST['question']
        que.user = request.user
        que.save()
        print("Question added to database")

    ctx = {
        'questions': Question.objects.filter(user=request.user)
    }
    return render(request, 'questions.html', ctx)

def logout_handler(request):
    logout(request)
    print(f"user is authenticated {request.user.is_authenticated}")
    print("User is logout")
    print(f"user is authenticated {request.user.is_authenticated}")
    return redirect('/')

def answer_handler(request,q_id):
    if request.method == 'POST':
            ans = Answer()
            ans.user = request.user
            ans.question = Question.objects.filter(pk=q_id)[0]
            ans.save()
            ans_info = A_info()
            ans_info.answer = ans
            ans_info.text = request.POST['answer']
            #print('is_anonymous',request.POST['is_anonymous'])
            if "is_anonymous" in request.POST:
                is_a='True'
            else:
                is_a = 'False'
            ans_info.is_anonymous = is_a
            ans_info.save()
            return redirect('/home/answers')
    return render(request, 'answer_handler.html')

def q_delete(request , q_id):
    questions = Question.objects.filter(pk = q_id)
    question = questions[0]
    question.delete()
    return redirect('/home/questions')

def bookmark(request , a_id):
    answer = Answer.objects.filter (pk = a_id)[0]
    if Bookmark.objects.filter ( answer = answer ).filter(user = request.user).count() == 0:
        bookmark = Bookmark (
            user = request.user ,
            answer = answer
        )
        bookmark.save()
        messages.success(request, 'Answer Bookmarked')
    else:
        messages.warning(request, 'Answer is already bookmarked')
    return redirect('/home')

def upvote(request , a_id):
    answer = Answer.objects.filter (pk = a_id)[0]
    a_info = A_info.objects.filter (answer = answer)[0]
    if Upvotes.objects.filter ( answer = answer ).filter( user = request.user).count() == 0:
        upvotes = Upvotes (
            user = request.user ,
            answer = answer
        )
        upvotes.save()
        a_info.upvotes+=1;
        a_info.save()
        messages.success(request, 'Answer upvoted')
    else:
        upvotes =  Upvotes.objects.filter ( answer = answer ).filter( user = request.user)
        upvotes.delete()
        a_info.upvotes-=1
        a_info.save()
        messages.success(request , 'upvote removed')
    return redirect('/home')

"""
Django views for FAQ application UI
"""

from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
from faq_app.models import Question
from faq_app.forms import QuestionForm, AnswerForm


# Create your views here.
def index(request):
    """FAQ Application homepage"""
    list_questions = Question.objects.all()
    if not request.user.is_authenticated:
        list_questions = Question.objects.annotate(count=Count('answers')).filter(count__gt=0)
    return render(request, 'faq/index.html', {'list_questions': list_questions})


def signup(request):
    """FAQ Application signup page"""
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if password == password_confirm:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                #log user in and redirect to settings page
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                #create a Profile object for the new user
                return redirect('home_page')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signup')
    else:
        return redirect('home_page')


def sign_in(request):
    """FAQ Application sign in page"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home_page')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('sign_in')
    else:
        return redirect('home_page')


@login_required(login_url='sign_in')
def logout(request):
    """FAQ Application logout action"""
    auth.logout(request)
    return redirect('sign_in')


def question(request):
    """FAQ Application new question action"""
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('home_page')
            except:
                pass
    return redirect('home_page')


@login_required(login_url='sign_in')
def answer(request):
    """FAQ Application new answer action"""
    if request.method == "POST":
        data = request.POST.copy()
        data['client'] = request.user.id
        form = AnswerForm(data)
        if form.is_valid():
            try:
                form.save()
                return redirect('home_page')
            except:
                pass
    return redirect('home_page')
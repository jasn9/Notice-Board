from django.shortcuts import render, redirect

# Create your views here.

# views are basically a web page function that controls one functionality

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# brfore adding template make sure to add ' <appname>.app.<app name with firstletter in capital>config ' in setting

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import AccessBoard, Board, Profile

# for passing messages when redirect occur
from django.contrib import messages

import uuid


def index(request):
    context = {}
    return render(request, 'central/index.html', context)


def add_user(request):
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']
    birthyear = request.POST['birthyear']
    user = User.objects.create_user(username, email, password)
    user.save()
    profile = Profile()
    profile.user_id = user
    profile.username = username
    profile.birth_year = birthyear
    profile.save()
    return redirect('central:index')


def user_login(request):
    if request.user.is_authenticated:
        return redirect('central:detail', request.user.username)
    context = {'message': ''}
    if request.method == 'POST':
        # print(request.POST['username'],request.POST['password'])
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('central:dashboard')
        context = {'error_message': 'Invalid Username / Password'}

    return render(request, 'central/login.html', context)


def register(request):
    arr = []
    for i in range(2020, 1947, -1):
        arr.append(i)
    context = {'arr': arr}
    return render(request, 'central/register.html', context)


def log_out(request):
    logout(request)
    return redirect('central:index')


def dashboard(request):
    if request.user.is_authenticated:
        context = {'user': request.user}
        return render(request, 'central/dashboard.html', context)
    else:
        messages.warning(request, 'Unauthorized')
        return redirect('central:index')


# Dummy No Use
def game(request):
    return render(request, 'central/game.html')


def detail(request, username):
    if not request.user.is_authenticated:
        messages.warning(request, 'Unauthorized')
        return redirect('central:index')
    profile = Profile.objects.get(user_id=request.user)
    context = {'user': request.user, 'profile': profile}
    return render(request, 'central/detail.html', context)


def update(request):
    if request.user.is_authenticated:
        # username = request.POST['username']
        email = request.POST['email']
        name = request.POST['name']
        affilation = request.POST['affilation']
        birth_year = request.POST['birth_year']
        country = request.POST['country']
        address = request.POST['address']

        profile = Profile.objects.get(user_id=request.user)
        # profile.username = username
        print(email, affilation, name)
        request.user.email = email;
        profile.full_name = name
        profile.affilation = affilation
        profile.birth_year = birth_year
        profile.country = country
        profile.address = address
        profile.save()

        messages.success(request, 'Your Update Request Has Been Fulfiled')
        return redirect('central:detail', request.user)
    messages.warning(request, 'Unauthorized')
    return redirect('central:index')


def delete_user(request):
    if request.user.is_authenticated:
        obj = User.objects.get(username=request.user.username)
        obj.delete()
        messages.success(request, 'Your Request Have Been Fulfilled Successfully !!!')
        return redirect('central:index')


def create_board(request):
    if request.user.is_authenticated:
        context = {}
        return render(request, 'central/create_board.html', context)
    messages.warning(request, 'Unauthorized')
    return redirect('central:index')


def register_board(request):
    board_id = str(uuid.uuid1())
    owner = request.user
    topic = request.POST['topic']
    description = request.POST['description']
    board = Board()
    board.board_id = board_id
    board.owner = owner
    board.topic = topic
    board.description = description
    board.save()
    access = AccessBoard()
    access.board_id = board
    access.user_id = request.user
    access.save()
    return redirect('central:get_board', board_id)


def get_board(request, board_id):
    board = Board.objects.get(board_id=board_id)
    access = AccessBoard.objects.get(board_id=board, user_id=request.user)
    if access is not None:
        context = {
            "topic": board.topic,
            "description": board.description
        }
        return render(request, 'central/board.html',  context)
    else:
        messages.warning(request, 'Unauthorized')
        return redirect('central:index')


def my_boards(request):
    if request.user.is_authenticated:
        boards = Board.objects.filter(owner=request.user)
        print(boards)
        for board in boards:
            print(board.board_id)
        return render(request, 'central/my_boards.html', context={'boards': boards})

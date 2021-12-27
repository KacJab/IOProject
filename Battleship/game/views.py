from django.shortcuts import render
# Create your views here.
from .game_utilities import *
from .forms import CreateUserForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import ResultForm
from django.core import serializers


def home(request):
    return render(request, 'index.html', {})


@login_required(login_url='login')
def game(request, mode):
    context = {'mode': mode}
    return render(request, 'plansza.html', context)


def gamemode(request):
    return render(request, 'trybgry.html')


# @login_required(login_url='login')
# def game(request):
#     board = Board()
#     board.randomly_locate_ships(Fleet())
#     return render(request, 'game.html', {
#         'game_title': 'Battleship',
#         'board': board.board,
#         'board_ids': board.board_ids,
#     })


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'User ' + user + ' created successfully')
                return redirect('login')

        context = {'form': form}
        return render(request, 'users/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('gamemode')
            else:
                messages.info(request, 'Incorrect username or password')

        context = {}
        return render(request, 'users/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def statistics(request):
    return render(request, 'stat.html')


def save_result(request, mode):
    if request.method == "POST" and request.is_ajax():
        player1 = request.POST.get('player1', None)
        player2 = request.POST.get('player2', None)
        form = ResultForm(request.POST)
        if form.is_valid():
            instance = form.save()
            serialized_instance = serializers.serialize('json', [instance, ])
            return JsonResponse({"instance": serialized_instance}, status=200)

        else:
            return JsonResponse({"error": ":(("}, status=400)
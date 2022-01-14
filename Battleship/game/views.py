from django.shortcuts import render
# Create your views here.
from .game_utilities import *
from .forms import CreateUserForm, VerifyPasswordForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import ResultForm
from django.core import serializers
from .models import Result
from .models import Player
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


def home(request):
    trans = translate(language ='en')
    return render(request, 'index.html', {'trans': trans})

def translate(language):
    cur_language = get_language()
    try:
        activate(language)
        text = gettext('gvjujtf')
    finally:
        activate(cur_language)
    return text

@login_required(login_url='login')
def game(request, mode):
    if mode == 'multiplayer':
        context = {'mode': mode, 'player2_username': request.session['_player2_username']}
    else:
        context = {'mode': mode, 'player2_username': "kąputerek"}
    return render(request, 'plansza.html', context)

def gamemode(request):
    return render(request, 'trybgry.html')


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


@login_required
def login_player2(request):
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            try:
                player2 = Player.objects.get(username=username)
                if player2 == request.user:
                    messages.info(request, 'Nie możesz się zalogować dwa razy na tego samego użytkownika lol')
                    return redirect('login_player2')
                if player2.check_password(password):
                    request.session['_player2_username'] = username
                    return redirect('game', mode='multiplayer')
                else:
                    messages.info(request, 'Nieprawidłowe hasło')
                    redirect('login_player2')
            except Player.DoesNotExist:
                messages.info(request, 'Użytkownik o podanym loginie nie istnieje')
        context = {}
        return render(request, 'users/login_player2.html', context)


def playerpanel(request):
    form = PasswordChangeForm(request.user)
    verify_password_form = VerifyPasswordForm()

    context = {
        'form': form,
        'verify_password_form': verify_password_form
    }
    return render(request, 'panelGracza.html', context)


@login_required(login_url='login')
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
        else:
            messages.info(request, 'Incorrect password')
        return redirect('playerpanel')


@login_required(login_url='login')
def delete_account(request):
    if request.method == 'POST':
        form = VerifyPasswordForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            password_match = request.user.check_password(password)
            if password_match:
                request.user.delete()
                logout(request)
                return redirect('home')
            else:
                messages.info(request, 'Incorrect password')
                return redirect('playerpanel')
    return redirect('playerpanel')


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def statistics(request):
    # results = Result.objects.order_by("-result")[:5]
    ranking_multiplayer = Player.objects.order_by("-result_multiplayer")[:5]
    ranking_easy = Player.objects.order_by("-result_easy")[:5]
    ranking_medium = Player.objects.order_by("-result_medium")[:5]
    ranking_hard = Player.objects.order_by("-result_hard")[:5]
    context = {
        "ranking_multiplayer": ranking_multiplayer,
        "ranking_easy": ranking_easy,
        "ranking_medium": ranking_medium,
        "ranking_hard": ranking_hard,
    }
    return render(request, 'stat.html', context)


@login_required(login_url='login')
def allgames(request):
    result = Result.objects.all()
    context = {
        "result": result
    }
    return render(request, 'all_games.html', context)


@login_required(login_url='login')
def replay(request, result_id):
    result = Result.objects.get(id=result_id)
    context = {
        "result": result
    }
    return render(request, 'replay.html', context)


@login_required(login_url='login')
def save_result(request, mode):
    # if request.method == "POST" and request.is_ajax():
    if request.method == "POST":
        form = ResultForm(request.POST)
        print(form)
        print(form.is_valid)
        if form.is_valid():
            instance = form.save()
            serialized_instance = serializers.serialize('json', [instance, ])

            player1 = Player.objects.filter(username=request.POST.get("player1"))[0]
            result1 = float(request.POST.get("result1"))

            if mode == "multiplayer":
                player2 = Player.objects.filter(username=request.POST.get("player2"))[0]
                result2 = float(request.POST.get("result2"))

                if result1 > player1.result_multiplayer:
                    Player.objects.filter(username=request.POST.get("player1")).update(result_multiplayer=result1)
                if result2 > player2.result_multiplayer:
                    Player.objects.filter(username=request.POST.get("player2")).update(result_multiplayer=result2)

            else:
                if mode == "easy":
                    if result1 > player1.result_easy:
                        Player.objects.filter(username=request.POST.get("player1")).update(result_easy=result1)
                elif mode == "medium":
                    if result1 > player1.result_medium:
                        Player.objects.filter(username=request.POST.get("player1")).update(result_medium=result1)
                elif mode == "hard":
                    if result1 > player1.result_hard:
                        Player.objects.filter(username=request.POST.get("player1")).update(result_hard=result1)

            return JsonResponse({"instance": serialized_instance}, status=200)
        else:
            return JsonResponse({"error": ":(("}, status=400)
    else:
        print('error!')
        return JsonResponse({"error": "oops"}, status=400)
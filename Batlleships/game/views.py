from django.shortcuts import render
# Create your views here.
from .game_utilities import *
from django.shortcuts import render


def index(request):
    board = Board()
    board.randomly_locate_ships(Fleet())
    x = 5
    return render(request, 'game.html', {
        'game_title': 'Battleship',
        'board': board.board,
        'board_ids': board.board_ids,
    })

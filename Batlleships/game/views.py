from django.shortcuts import render
# Create your views here.
from .game_utilities import *
from django.shortcuts import render


def index(request):
    board = Board()
    board.randomly_locate_ships(Fleet())
    x = 5
    return render(request, 'game.html', {
        'board': board.board,
        'cols': len(board.board),
        'rows': len(board.board[0])
    })

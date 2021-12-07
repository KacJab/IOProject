import random


class Board:
    def __init__(self):
        self.board = [[0 for x in range(0, 10)] for y in range(0, 10)]

    def randomly_locate_ships(self, fleet):
        fleet = Fleet()
        for ship in fleet.ships:
            orientation = random.randint(0, 1)
            place_start = random.randint(0, 10 - ship.size)
            place_on_axis = random.randint(0, 9)
            for s in range(0, ship.size):
                if orientation == 0:
                    self.board[place_start+s][place_on_axis] = 1
                else:
                    self.board[place_on_axis][place_start+s] = 1


class Ship:
    def __init__(self, size):
        self.size = size


class Fleet:
    def __init__(self):
        self.ships = []
        for i in range(4):
            for j in range(4 - i):
                self.ships.append(Ship(i + 1))


board = Board()
board.randomly_locate_ships(Fleet())

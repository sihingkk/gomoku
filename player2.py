#!/usr/bin/env python3
from numpy import *

next_player = {"x": "o", "o": "x"}

def get_symbol(game,x,y):
    return game['board'][x][y]

def row_check(board, symbol):
    for r in range(len(board)):
        row = board[r]
        for i in range(len(row)+1-5):
            window = row[i:i+5]
            print(window)
            if ((window == array(['', symbol, symbol, symbol, ''])).all()):
                return (r,i)
    return ""


def player2(game):
    symbol = game['current_player']
    board = game['board']
    next_move = row_check(board, next_player[symbol])
    if(next_move !=""):
        return next_move
    next_move = row_check(transpose(board), next_player[symbol])
    if(next_move !=""):
        return transpose(next_move)
    return (random.randint(0, 10), random.randint(0,10))

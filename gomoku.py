import tkinter as tk
import numpy as np
from tkinter import ttk
from tkinter import messagebox
from player2 import player2
import time
from numpy import *

players = ["x", "o"]

next_player = {"x": "o", "o": "x"}

current_player = players[0]

def create_empty_board(x):
    return np.full((x,x), "")


size = 10

def create_game(size):
    return {'board': create_empty_board(size),
            'current_player': players[0]}

game = create_game(10)

def get_symbol(game,x,y):
    return game['board'][x][y]

def allowed_move(game,x,y):
    return game['board'][x][y] not in players

def make_move(game, x, y):
    if allowed_move(game,x,y):
        new_board = game['board'].copy()
        new_board[x][y] = game['current_player']
        game['board'] = new_board
        game['current_player'] = next_player[game['current_player']]
    return game

def row_check(row):
    for i in range(len(row)+1-5):
        window = row[i:i+5]
        if (len(window[window == window[0]]) == 5):
            return window[0]
    return ""

def who_won(game):
    for row in game['board']:
        if row_check(row) in players:
           return row_check(row)
    for row in transpose(game['board']):
        if row_check(row) in players:
           return row_check(row)

    return ""



def sizedButton(game,root, x,y):

    f = tk.Frame(root, height=50, width=50)
    f.pack_propagate(0) # don't shrink
    f.place(x = x * 50, y = y * 50)


    def button_on_click():
        global game
        if(game['current_player']=='x'):
            game = make_move(game, x, y)
            btn_easy["text"] = get_symbol(game,x,y)
            if(who_won(game) in players):
                messagebox.showinfo(title= "Game ends", message= "Player "+who_won(game) + " won the game." )

    btn_easy = tk.Button(f, text = game['board'][x][y], command = button_on_click)
    btn_easy.pack(fill=tk.BOTH, expand=1)


def background():
    root = tk.Tk()
    root.geometry('1160x640')

    def render(game):
        for widget in root.winfo_children():
            widget.destroy()
        for x in range(0,size,1):
            for y in range(0,size,1):
                sizedButton(game,root, x,y)
    def play():
        global game
        if(game['current_player']=='o'):
            (x,y) = player2(game)
            game = make_move(game,x,y)
        render(game)
        root.after(500, lambda: play())
    root.after(500, lambda: play())
    render(game)
    root.mainloop()

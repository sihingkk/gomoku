#!/usr/bin/env python3
from gomoku import *
from player2 import player2

class TestClass:
    def test_when_3_block_it(self):
        game = create_game(10)
        x = range(3)
        for i in x:
            game = make_move(game,3,2+i) # x
            game = make_move(game,4,2+i) # o
        print(game['board'])
        assert player2(game) == (3,1)

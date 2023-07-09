#!/usr/bin/env python3
from gomoku import *
from numpy import *

class TestClass:
    def test_when_making_a_move_alternate_players(self):
        game = create_game(10)
        first_state = make_move(game, 0, 0)
        second_state = make_move(first_state, 1, 1)
        assert get_symbol(second_state, 0, 0) == "x"
        assert get_symbol(second_state, 1, 1) == "o"

    def test_ignore_moves_that_already_there(self):
        game = create_game(10)
        state = make_move(game,0,0)
        assert get_symbol(state, 0, 0) == "x"
        state = make_move(game,0,0)
        assert get_symbol(state, 0, 0) == "x"

    def test_game_in_progress(self):
        game = create_game(10)


        x = range(4)
        for i in x:
            game = make_move(game,0,i)
            game = make_move(game,1,i)

        assert who_won(game) == ""

    def test_game_won_horizontal(self):
        game = create_game(10)
        x = range(4)
        for i in x:
            game = make_move(game,0,i)
            game = make_move(game,1,i)
        game = make_move(game,0,4)

        print(game)
        assert who_won(game) == "x"


    def test_game_won_vertical(self):
        game = create_game(10)
        x = range(4)
        for i in x:
            game = make_move(game,i,0)
            game = make_move(game,i,1)
        game = make_move(game,4,0)

        print(game)
        assert who_won(game) == "x"

    # def test_game_won_diagonal(self):
    #     game = create_game(10)
    #     x = range(4)
    #     for i in x:
    #         game = make_move(game,i,i)
    #         game = make_move(game,i+1,i)
    #     game = make_move(game,4,4)

    #     print(game)
    #     assert who_won(game) == "x"





    def test_row_check(self):
        assert row_check(array(["x","x","x","x","x"])) == "x"
        assert row_check(array(["x","x","x","x","y"])) == ""
        assert row_check(array(["y","y","y","y","y"])) == "y"

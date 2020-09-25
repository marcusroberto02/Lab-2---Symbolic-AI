# Game 2048: Artificial intelligence

# Instructions:
#   Move up, down, left, or right to merge the tiles. The objective is to 
#   get a tile with the number 2048 (or higher)
#
# Control:
#    arrows  : Merge up, down, left, or right
#    r       : Restart game
#    q / ESC : Quit

from Game2048 import Game2048
import numpy as np
import pygame
import random

moves = ['left', 'right', 'up', 'down']

# simuler N antal spil og udregn gennemsnitlig score
avg_score = 0
repetitions = 100
for i in range(repetitions):
    sim = Game2048()
    sim.reset()
    done = False
    score = 0
    while not done:
        action = moves[np.random.randint(4)]
        (board, score), reward, done = sim.step(action)
    avg_score += score

avg_score /= repetitions

# bestem gennemsnitlig score vha. monte carlo
mon_avg_score = 0
mon_repetitions = 100
rep = 10
mon = Game2048()
search_length = 10
win_rate = 0
global_max = 0
for i in range(mon_repetitions):
    mon.reset()
    t = 0
    done = False
    score = 0
    while not done:
        if t % 100 == 0 and t != 0:
            print(score, np.max(mon.board), "Move number:", t, "Game number:", i+1, "Search length:", search_length)
            print(mon.board)
        t += 1
        best_move = ""
        best_score = 0
        for move in mon.get_valid_moves(moves):
            cur_score = 0
            for k in range(rep):
                temp = Game2048((mon.board,mon.score))
                (b, s), r, d = temp.step(move)
                mc = 0
                while not d and mc < search_length:
                    next_move = moves[np.random.randint(len(moves))]
                    (b, s), r, d = temp.step(next_move)
                    mc += 1
                cur_score += s
            if cur_score > best_score:
                best_score = cur_score
                best_move = move
        (board, score), reward, done = mon.step(best_move)
    print(np.max(mon.board))
    print("Game nr:", i+1, "Score:", score)
    if np.max(mon.board) >= 2048:
        win_rate += 1
    mon_avg_score += score
    if score > global_max:
        global_max = score
            
win_rate /= mon_repetitions
win_rate *= 100
mon_avg_score /= mon_repetitions



print("From random plays average score is:", avg_score)
print("With Monte Carlo Search average score is:", mon_avg_score)
print("Win rate:", win_rate, "%")
print("Global max:", global_max)




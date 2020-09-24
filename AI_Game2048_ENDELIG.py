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
rep = 50
mon = Game2048()
search_length = 25
for i in range(mon_repetitions):
    print(i)
    mon.reset()
    done = False
    score = 0
    mc = 0
    while not done:
        # vælg bedste træk
        if mc % 100 == 0:
            print(score, np.max(mon.board), "Move number:", mc)
            if np.max(mon.board) == 2048:
                print(mon.board)
        mc += 1
        best_score = 0
        best_action = moves[0]
        for j in range(len(moves)):
            temp = Game2048((mon.board, mon.score))
            a_score = 0
            eq = np.copy(mon.board)
            (b, s), r, d = temp.step(moves[j])
            comp = eq == b
            if comp.all():
                continue
            for _ in range(rep):                
                t = 0
                while not d and t < search_length:
                    action = moves[np.random.randint(4)]
                    (b, s), r, d = temp.step(action)
                    t += 1
                    a_score += s
                temp = Game2048((mon.board, mon.score))
                (b, s), r, d = temp.step(moves[j])
            a_score /= rep
            if a_score > best_score:
                best_score = a_score
                best_action = moves[j]
        # udfør bedste træk
        (board, score), reward, done = mon.step(best_action)
    mon_avg_score += score
    print(np.max(mon.board), " <--")
    print(score)

mon_avg_score /= mon_repetitions



print("From random plays average score is:", avg_score)
print("With Monte Carlo Search average score is:", mon_avg_score)

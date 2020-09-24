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
        action = random.choice(moves)
        (board, score), reward, done = sim.step(action)
    avg_score += score

avg_score /= repetitions

# bestem gennemsnitlig score vha. monte carlo
mon_avg_score = 0
mon_repetitions = 100
rep = 1
for i in range(mon_repetitions):
    print(i)
    mon = Game2048()
    mon.reset()
    done = False
    score = 0
    while not done:
        # vælg bedste træk
        best_score = 0
        best_action = moves[0]
        for j in range(len(moves)):
            a_score = 0
            for k in range(rep):
                temp = Game2048((mon.board, mon.score))
                temp.reset()
                d = False
                s = 0
                while not d:
                    action = random.choice(moves)
                    (board, s), reward, d = temp.step(action)
                a_score += s
            a_score /= rep
            if a_score > best_score:
                best_score = a_score
                best_action = moves[j]
        # udfør bedste træk
        (board, score), reward, done = mon.step(best_action)
    mon_avg_score += score

mon_avg_score /= mon_repetitions

print("From random plays average score is:", avg_score)
print("With Monte Carlo Search average score is:", mon_avg_score)

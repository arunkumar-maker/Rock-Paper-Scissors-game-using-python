# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 17:41:30 2022

@author: Arun Kumar
"""
import random
while True:
    choices=["rock","paper","scissors"]
    computer=random.choice(choices)
    #print("Computer: ",computer)
    player=None
    while player not in choices:
        player=input("choose rock/paper/scissors: ").lower()
    #print("Player: ",player)
    if computer==player:
       print("Computer: ",computer)
       print("Player: ",player)
       print("Tie")
    elif player=="rock":
         if computer=="paper":
             print("Computer: ",computer)
             print("Player: ",player)
             print("You lost!!")
         if computer=="scissors":
             print("Computer: ",computer)
             print("Player: ",player)
             print("You won!!")
    elif player=="paper":
         if computer=="rock":
             print("Computer: ",computer)
             print("Player: ",player)
             print("You won!!")
         if computer=="scissors":
             print("Computer: ",computer)
             print("Player: ",player)
             print("You lost!!")
    elif player=="scissors":
         if computer=="rock":
             print("Computer: ",computer)
             print("Player: ",player)
             print("You lost!!")
         if computer=="paper":
             print("Computer: ",computer)
             print("Player: ",player)
             print("You won!!")
    play_again=input("Do you want to play again(y/n): ").lower()
    if play_again!="y":
        break
print("Bye...see you later :) ")






























































# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
player1 = input("Enter your choice(player1):")
player2 = input("Enter your choice(player2):")

if (player1 == player2):
    print("It's a draw. Try again.")
    
elif (player1 == "rock" and player2 == "paper"):
    print("Player2 wins")
    
elif (player1 == "paper" and player2 == "rock"):
    print("Player1 wins")
    
elif (player1 == "rock" and player2 == "scissors"):
    print("Player2 wins")
    
elif (player1 == "scissors" and player2 == "rock"):
    print("Player1 wins")
    
elif (player1 == "scissor" and player2 == "paper"):
    print("Player1 wins")
    
elif (player1 == "paper" and player2 == "scissor"):
    print("Player2 wins")
else:
    print("This is not a valid object selection")
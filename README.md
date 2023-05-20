# 3 Men Morris
CPSC 481-05 Group Project By: Kevin Nguyen, Harrison Park, Christian Verry
Our project is developed in Python and it takes inspiration from the code used to create the classic game Tic Tac Toe. 3 Men's Morris is a spin off of Tic Tac Toe and is an ancient game.
We built an AI that utilizes the minimax with alpha beta pruning so that the user can play against a competitive opponnent.
- It begins with our code printing out the “board” of the game and initializes a blank “board”. 
  - The game begins and the player and AI take turns putting down all three of their own game pieces.
  - Once all six game pieces have been placed, the player and AI take turns moving their own game pieces to try and reach the goal state of the board. 
- There are functions like “check_win”, “evaluate”, and “minimax”. 
- The “check_win” ensures that the program continually checks the current game state and compares it to the goal state. 
  - This ensures that the player and AI don’t keep continuing the game when the goal state is reached. 
- Function “minimax” is our implementation of the minimax algorithm with alpha beta pruning. 
- Function “evaluate” contains code to see the board state and call the “check_win” function during after the player makes a move or if the AI makes a move. 

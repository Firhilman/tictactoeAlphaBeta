# tictactoeAlphaBeta
Python AI script for 4x4 Tic Tac Toe using Minimax with Alpha-Beta Pruning.

This is an AI script, game board is not included. You can use this script and modify to your own game board. The main function that is going to be called is Play(), the Play() function takes in your game board, and the player as arguments. Player X or O can either be 0 or 1. This was made for a 4x4 tic tac toe with a game board that uses 1D Array. Empty cells have a value of -1.

There are two heuristic functions in the player.py file. instructions on how to switch to either one of them are commented in the code.

The default heuristic function's logic goes like this:
+1000 * (depth+1) for EACH 4-in-a-line for computer.
+100 * (depth+1) for EACH three-in-a-line (with a empty cell) for computer.
+10 * (depth+1) for EACH two-in-a-line (with two empty cells) for computer.
+1 * (depth+1) for EACH one-in-a-line (with three empty cells) for computer.
Negative scores for opponent, i.e., -1000, -100, -10, -1 * (depth+1) for EACH opponent's 4-in-a-line, 3-in-a-line, 2-in-a-line, and 1-in-a-line
0 otherwise (empty lines or lines with both computer's and opponent's seeds).

The other heuristic function is a much simpler:
+11 * (depth+1) for player win
-11 * (depth+1) for opponent win
0 for draw

Feel free to contribute to make it better and more optimized. 
Potential Optimization:
1. Apply symmetry
2. Apply memoization
3. Better heuristic function

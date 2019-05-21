from math import inf as infinity
import copy
import random




class Player:
    def __init__(self):
        pass

    def play(self, game_board_state, player_n):
        emptyPos = [i for i in range(len(game_board_state)) if game_board_state[i] < 0] # Checks the board for all empty spots
        # if len(emptyPos) == 16:
        #     return 9
        bestScore = -infinity # Player is maximizing player so bestScore == -infinity
        choices = [] # Creates an array to store best positions
        localState = copy.deepcopy(game_board_state) #Makes a local copy of the game board
        depth = 5 # Depth is set to 7 because that is the max depth in 4x4 to reach a winning condition

        # Loops through every child of game board to calculate the minimax
        for position in emptyPos: # Iterates through every empty positions
            localState[position] = player_n # Inserts player symbol in empty spot
            # calculate the score by calling minimax() functiom
            score = self.minimax(localState, depth, False, self.playerSwitch(player_n), player_n, -infinity, infinity)
            localState[position] = -1 # Reverts position to empty
            if score > bestScore:  # Checks if score is > current bestScore
                bestScore = score # If true, set current bestScore as score
                choices = [position] # If score > bestScore is true, put the position index in the 'choice' array
            elif bestScore == score: # If bestScore is equal to score, append it in the choices array
                choices.append(position)
        # try:
        return random.choice(choices) # Pick random index from choice array so game does not provide same outcome
        # except IndexError:
        #     return random.choice(emptyPos)

    #Creates MINIMAX Tree with alpha-beta pruning, planned to do memoization too but could not implement
    def minimax(self, state, depth, isMaximising, currentPlayer, oriPlayer, alpha, beta):

        emptyPos = [i for i in range(len(state)) if state[i] < 0] # Checks the board for all empty spots

        # If there is no empty spots, or depth == 0
        if len(emptyPos) == 0 or depth == 0:
            return self.complexScore(state, oriPlayer, depth+1) # Return the score
            end()

        if isMaximising: # If maximising player
            maxScore = -infinity # Set max score to -infinity, the worst possible value
            for position in emptyPos: # Iterates through every empty positions
                state[position] = currentPlayer # Inserts player symbol in empty spot
                # calculate the score by calling minimax() functiom
                score = self.minimax(state, depth-1, False, self.playerSwitch(currentPlayer), oriPlayer, alpha, beta)
                state[position] = -1 #Revert move
                maxScore = max(maxScore, score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
            return maxScore
        else:
            minScore = infinity
            for position in emptyPos:
                state[position] = currentPlayer
                score = self.minimax(state, depth-1, True, self.playerSwitch(currentPlayer), oriPlayer, alpha, beta)
                state[position] = -1 #Revert move
                minScore = min(minScore, score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
            return minScore

    def playerSwitch(self, player): #Function to switch players
        if player == 0:
            return 1
        else:
            return 0
##########################OTHER HEURISTIC FUNCTION MUCH SIMPLER#############################################################
    # def simpleScore(self, board, player, depth): #Simple scoring system, takes in original player argument in playet
    #     if self.winningCon(board, player): # If original player wins
    #         score = 11 * (depth) # 11 multiply the depth
    #     elif self.winningCon(board, self.playerSwitch(player)): # If opponent wins
    #         score = -11 * (depth) # -11 multiply the depth
    #     else:
    #         score = 0 #if draw
    #     return score

    # def winningCon(self, state, player): #Straight lines winning conditions
    #     winCombos = [
    #         [state[0], state[1], state[2], state[3]],
    #         [state[4], state[5], state[6], state[7]],
    #         [state[8], state[9], state[10], state[11]],
    #         [state[12], state[13], state[14], state[15]],
    #         [state[0], state[4], state[8], state[12]],
    #         [state[1], state[5], state[9], state[13]],
    #         [state[2], state[6], state[10], state[14]],
    #         [state[3], state[7], state[11], state[15]],
    #         [state[0], state[5], state[10], state[15]],
    #         [state[3], state[6], state[9], state[12]],
    #     ]
    #     opponent = self.playerSwitch(player)
    #     if [player, player, player, player] in winCombos:
    #         return True
    #     elif [opponent, opponent, opponent, opponent] in winCombos:
    #         return True
    #     else:
    #         return False
############################UNCOMMENT TO MAKE IT WORK, AND COMMENT THE complexScore() METHOD 
############################And in line 44 change self.complexScore() to self.simpleScore(state, oriPLayer, depth+1)


#########COMPLEX HEURSITIC FUNCTION############################################################################
    def complexScore(self, board, player, depth):
            score = 0
            for j in range(0, 4):
                #Check if there is a win for either player
                if board[j] != -1 and (board[j] == board[j+4] == board[j+8] == board[j+12]): # vertical line
                    if board[j] == player:
                        score += (1000 *(depth)) # If original player wins, return 1000 * depth
                        return score # Return score if there is a win, stop the loop.
                    else:
                        score += (-1000 *(depth)) # If opponent wins, return -1000 * depth
                        return score

                elif board[j*4] != -1 and (board[j*4] == board[j*4+1] == board[j*4+2] == board[j*4+3]): # horizontal line
                    if board[j*4] == player:
                        score += (1000 *(depth))
                        return score
                    else:
                        score += (-1000 *(depth))
                        return score

                elif board[0] != -1 and (board[0] == board[5] == board[10] == board[15]): # top left diagonal                
                    if board[0] == player:
                        score += (1000 *(depth))
                        return score
                    else:
                        score += (-1000 *(depth))
                        return score

                elif board[3] != -1 and (board[3] == board[6] == board[9] == board[12]): # top right diagonal                 
                    if board[3] == player:
                        score += (1000 *(depth))
                        return score
                    else:
                        score += (-1000 *(depth))
                        return score

                else:
                    if board[j+12] != -1 and (board[j] == board[j+8] == board[j+4]) and (board[j] == -1): # reverse vertical line
                        if board[j+12] == player:
                            score += (100 *(depth))
                        else:
                            score += (-100 *(depth))

                    if board[j+4] != -1 and (board[j+8] == board[j+4]) and (board[j] and board[j+12] == -1): # vertical line
                        if board[j+4] == player:
                            score += (10 *(depth))
                        else:
                            score += (-10 *(depth))

                    if board[j+12] != -1 and (board[j] == board[j+12]) and (board[j+4] and board[8] == -1): # vertical line
                        if board[j+12] == player:
                            score += (10 *(depth))
                        else:
                            score += (-10 *(depth))

                    if board[j] != -1 and (board[j] == board[j+4] == board[j+8]) and (board[j+12] == -1): # vertical line
                        if board[j] == player:
                            score += (10 *(depth))
                        else:
                            score += (-10 *(depth))

                    if board[j] != -1 and (board[j] == board[j+4]) and (board[j+8] and board[j+12] == -1): # vertical line
                        if board[j] == player:
                            score += (10 *(depth))
                        else:
                            score += (-10 *(depth))

                    if board[j] != -1 and (board[j+4] and board[j+8] and board[j+12] == -1): # vertical line
                        if board[j] == player:
                            score += (1 *(depth))
                        else:
                            score += (-1 *(depth))

                    if board[j+4] != -1 and (board[j] and board[j+8] and board[j+12] == -1): # vertical line
                        if board[j+4] == player:
                            score += (1 *(depth))
                        else:
                            score += (-1 *(depth))

                    if board[j+8] != -1 and (board[j] and board[j+4] and board[j+12] == -1): # vertical line
                        if board[j+8] == player:
                            score += (1 *(depth))
                        else:
                            score += (-1 *(depth))

                    if board[j+12] != -1 and (board[j] and board[j+8] and board[j+4] == -1): # vertical line
                        if board[j+12] == player:
                            score += (1 *(depth))
                        else:
                            score += (-1 *(depth))

                    if board[j*4+3] != -1 and (board[j*4+3] == board[j*4+1] == board[j*4+2]) and (board[j*4] == -1): # Switchhorizontal line
                        if board[j*4+3] == player:
                            score += (100 *(depth))
                        else:
                            score += (-100 *(depth))

                    if board[j*4+2] != -1 and (board[j*4+2] == board[j*4+1]) and (board[j*4] and board[j*4+3] == -1): # horizontal line
                        if board[j*4+2] == player:
                            score += (10 *(depth))
                        else:
                            score += (-10 *(depth))

                    if board[j*4] != -1 and (board[j*4] == board[j*4+3]) and (board[j*4+2] and board[j*4+1] == -1): # horizontal line
                        if board[j*4] == player:
                            score += (10 *(depth))
                        else:
                            score += (-10 *(depth))


                    if board[j*4] != -1 and (board[j*4] == board[j*4+1] == board[j*4+2]) and (board[j*4+3] == -1): # Switchhorizontal line
                        if board[j*4] == player:
                            score += (100 *(depth))
                        else:
                            score += (-100 *(depth))

                    if board[j*4] != -1 and (board[j*4] == board[j*4+1]) and (board[j*4+2] and board[j*4+3] == -1): # horizontal line
                        if board[j*4] == player:
                            score += (10 *(depth))
                        else:
                            score += (-10 *(depth))

                    if board[j*4] != -1 and (board[j*4+1] and board[j*4+2] and board[j*4+3] == -1): # horizontal line
                        if board[j*4] == player:
                            score += (1 *(depth))
                        else:
                            score += (-1 *(depth))


                    if board[j*4+1] != -1 and (board[j*4] and board[j*4+2] and board[j*4+3] == -1): # horizontal line
                        if board[j*4+1] == player:
                            score += (1 *(depth))
                        else:
                            score += (-1 *(depth))


                    if board[j*4+2] != -1 and (board[j*4] and board[j*4+1] and board[j*4+3] == -1): # horizontal line
                        if board[j*4+2] == player:
                            score += (1 *(depth))
                        else:
                            score += (-1 *(depth))


                    if board[j*4+3] != -1 and (board[j*4] and board[j*4+1] and board[j*4+2] == -1): # horizontal line
                        if board[j*4+3] == player:
                            score += (1 *(depth))
                        else:
                            score += (-1 *(depth))


                    if board[15] != -1 and (board[15] == board[5] == board[10]) and (board[0] == -1): # Switchminor diagonal
                        if board[15] == player:
                            score += (100 *(depth))
                        else:
                            score += (-100 *(depth))


                    if board[10] != -1 and (board[10] == board[5]) and (board[0] and board[15] == -1): # minor diagonal
                        if board[10] == player:
                            score += (10 *(depth))
                        else:
                            score += (-10 *(depth))


                    if board[0] != -1 and (board[0] == board[15]) and (board[5] and board[10] == -1): # minor diagonal
                        if board[0] == player:
                            score += (10 *(depth))
                        else:
                            score += (-10 *(depth))


                    if board[0] != -1 and (board[0] == board[5] == board[10]) and (board[15] == -1): # Switchminor diagonal
                        if board[0] == player:
                            score += (100 *(depth))
                        else:
                            score += (-100 *(depth))

                    if board[0] != -1 and (board[0] == board[5]) and (board[10] and board[15] == -1): # minor diagonal
                        if board[0] == player:
                            score += (10 *(depth))
                        else:
                            score += (-10 *(depth))

                    if board[0] != -1 and (board[5] and board[10] and board[15] == -1): # minor diagonal
                        if board[0] == player:
                            score += (1 *(depth))
                        else:
                            score += (-1 *(depth))

                    if board[5] != -1 and (board[0] and board[10] and board[15] == -1): # minor diagonal
                        if board[5] == player:
                            score += (1 *(depth))
                        else:
                            score += (-1 *(depth))


                    if board[10] != -1 and (board[0] and board[5] and board[15] == -1): # minor diagonal
                        if board[10] == player:
                            score += (1 *(depth))
                        else:
                            score += (-1 *(depth))


                    if board[15] != -1 and (board[0] and board[5] and board[10] == -1): # minor diagonal
                        if board[15] == player:
                            score += (1 *(depth))
                        else:
                            score += (-1 *(depth))


                    if board[12] != -1 and (board[12] == board[6] == board[9]) and (board[3] == -1): # Switchmajor diagonal
                        if board[12] == player:
                            score += (100 *(depth))
                        else:
                            score += (-100 *(depth))


                    if board[9] != -1 and (board[9] == board[6]) and (board[3] and board[12] == -1): # major diagonal
                        if board[9] == player:
                            score += (10 *(depth))
                        else:
                            score += (-10 *(depth))

                    if board[3] != -1 and (board[3] == board[12]) and (board[6] and board[9] == -1): # major diagonal
                        if board[3] == player:
                            score += (10 *(depth))
                        else:
                            score += (-10 *(depth))


                    if board[3] != -1 and (board[3] == board[6] == board[9]) and (board[12] == -1): # Switchmajor diagonal
                        if board[3] == player:
                            score += (100 *(depth))
                        else:
                            score += (-100 *(depth))

                    if board[3] != -1 and (board[3] == board[6]) and (board[9] and board[12] == -1): # major diagonal
                        if board[3] == player:
                            score += (10 *(depth))
                        else:
                            score += (-10 *(depth))

                    if board[3] != -1 and (board[6] and board[9] and board[12] == -1): # major diagonal
                        if board[3] == player:
                            score += (1 *(depth))
                        else:
                            score += (-1 *(depth))

                    if board[12] != -1 and (board[6] and board[9] and board[3] == -1): # major diagonal
                        if board[3] == player:
                            score += (1 *(depth))
                        else:
                            score += (-1 *(depth))
                            
                    if board[9] != -1 and (board[6] and board[12] and board[3] == -1): # major diagonal
                        if board[3] == player:
                            score += (1 *(depth))
                        else:
                            score += (-1 *(depth))

                    if board[6] != -1 and (board[9] and board[12] and board[3] == -1): # major diagonal
                        if board[3] == player:
                            score += (1 *(depth))
                        else:
                            score += (-1 *(depth))
            return score # default return value if no win condition is found
###############################################################################################################
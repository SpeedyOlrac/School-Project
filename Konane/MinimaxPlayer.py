from konane import *

# Carlo Gonzalez and Heather Murray


class MinimaxPlayer(Konane, Player):
    # generate moves for both players, using extract method override
    # calulate depth based on generated moves
    #  can then use the Wikipedia pseudo-code for Minimax
    def __init__(self, size, depthLimit):
        Konane.__init__(self, size)
        self.limit = depthLimit

    def initialize(self, side):
        # complete this
        self.side = side
        limit = self.limit
        self.name = "MinimaxDepth" + str(limit)

        self.currPlayer = self.side

    def getMove(self, board):
        # complete this
        # provides child nodes of each move on board
        moves = self.generateMoves(board, self.side)
        bestMove = []

        alpha = -float("inf")
        beta = float("inf")

        alpha = -float("inf")
        val = 0
        #beta = float("inf")
        self.currPlayer = self.opponent(self.side)
        for element in moves:
           
            val = self.alpha_beta_pruning(self.nextBoard(board, self.side, element), self.limit - 1, self.opponent(self.side), alpha, beta)

            if val > alpha:
                bestMove = element
                alpha = val
        return bestMove


    # Dr. Schwartz said to make the function below to recurse on the problem.
    # Eval just quantify each move.
    def minmax(self, board, m_depth, player):
        # Returns one value, either:
        # - a terminal value
        # - the best value for max
        # recursive code to min max the game.
        moves = self.generateMoves(board, player)
        n = len(moves)
 
        # base case
        if n == 0:
            self.currPlayer = self.opponent(self.side)
            #if player == 'B':
            if player == self.side:
                
                return -float("inf")
            else:
                return float("inf")

        if m_depth == 0:
            self.currPlayer = self.opponent(self.side)
            score = self.eval(board, player)
            return score

        #if player == 'B':
        if player == self.side:
            bestValue = -float("inf")

            for element in moves:
                self.currPlayer = self.opponent(self.side)
                # set value of child node to False even though Max, so that it will do the next block
                val = self.minmax(self.nextBoard(board, player, element), m_depth - 1, self.opponent(player))
                # check value to see if it's the best value for Max/B
                bestValue = max(bestValue, val)
            return bestValue

        elif player == 'W':
            bestValue = float("inf")
            self.currPlayer = self.opponent(self.side)
            for element in moves:
                
                # set value of child to True, even though Min, so it will do the if playerMax==True set
                val = self.minmax(self.nextBoard(board, player, element), m_depth - 1, self.opponent(player))
                bestValue = min(bestValue, val)
            return bestValue

def eval(self, board):
        # complete this – this will be your evaluation function.
        # Eval just quantifies each move.
        # High values should be good for max.
        # Compare all the moves and see which one is the best.
        # RETURNS A NUMBER - good or bad for Max

        # iterative deepening or best first search
        #    'W' surrounded by 'W' or '.'
        # calculate if no moves left for W, return +10
        # calculate if no moves left for B, return -10

        #We are counting the number of pieces that have no moves for each color
        eval_num = self.eval_func(board, 'B')
        #and subtracting the opponent
        eval_num -= self.eval_func(board, 'W')
        return eval_num

def eval_func (board, player)

    eval_num = 0
        for r in range(self.size):
            for c in range(self.size):
                # handles 4 corners of board
                elif r == 0 and c == 0:
                    if board[r][c] == player and (board[r + 1][c] == '.' or board[r + 1][c] == player) and (board[r][c + 1] == '.' or board[r][c + 1] == player):
                        eval_num += 10
                elif r == self.size - 1 and c == 0:
                    if board[r][c] == player and (board[r - 1][c] == '.' or board[r - 1][c] == player) and (board[r][c + 1] == '.' or board[r][c + 1] == player):
                        eval_num += 10
                elif r == 0 and c == self.size - 1:
                    if board[r][c] == player and (board[r + 1][c] == '.' or board[r + 1][c] == player) and (board[r][c - 1] == '.' or board[r][c - 1] == player):
                        eval_num += 10
                elif r == self.size - 1 and c == self.size - 1:
                    if board[r][c] == player and (board[r - 1][c] == '.' or board[r - 1][c] == player) and (board[r][c - 1] == '.' or board[r][c - 1] == player):
                        eval_num += 10
                
                # first & second columns
                elif c == 0 or c == 1:
                    #down or right only
                    if r == 1:
                        if board[r][c] == player and (board[r + 1][c] == '.' or board[r + 1][c] == player) and (
                                board[r][c + 1] == '.' or board[r][c + 1] == player):
                            eval_num += 10
                    # up or right only
                    elif r == self.size - 2:
                        if board[r][c] == player and (board[r - 1][c] == '.' or board[r - 1][c] == player) and (
                                board[r][c + 1] == '.' or board[r][c + 1] == player):
                            eval_num += 10
                    # up, down, or right
                    else:
                        if board[r][c] == player and (board[r + 1][c] == '.' or board[r + 1][c] == player) and (
                                board[r][c + 1] == '.' or board[r][c + 1] == player) and (board[r - 1][c] == '.' or board[r - 1][c] == player):
                            eval_num += 10
                        
                # last and next-to-last columns
                #elif c == self.size - 1 or c == self.size - 2:
                elif c == self.size - 1:
                    #down or LEFT only
                    if r == 1:
                        if board[r][c] == player and (board[r + 1][c] == '.' or board[r + 1][c] == player) and (
                                board[r][c - 1] == '.' or board[r][c - 1] == player):
                            eval_num += 10
                                            # up or LEFT only
                    elif r == self.size - 2:
                        if board[r][c] == player and (board[r - 1][c] == '.' or board[r - 1][c] == player) and (
                                board[r][c - 1] == '.' or board[r][c - 1] == player):
                            eval_num += 10
                                            # up, down, or LEFT
                    else:
                        if board[r][c] == player and (board[r + 1][c] == '.' or board[r + 1][c] == player) and (
                                board[r][c - 1] == '.' or board[r][c - 1] == player) and (board[r - 1][c] == '.' or board[r - 1][c] == player):
                            eval_num += 10
                        
                # first and second rows
                elif r == 0 or r == 1:
                    #down or right only
                    if c == 1:
                        if board[r][c] == player and (board[r + 1][c] == '.' or board[r + 1][c] == player) and (
                                board[r][c + 1] == '.' or board[r][c + 1] == player):
                            eval_num += 10
                                            elif c == self.size - 2:
                    # down or LEFT only
                        if board[r][c] == player and (board[r + 1][c] == '.' or board[r + 1][c] == player) and (
                                board[r][c - 1] == '.' or board[r][c - 1] == player):
                            eval_num += 10
                                            #other columns in row 0:   left, right, or down
                    else:
                        if board[r][c] == player and (board[r + 1][c] == '.' or board[r + 1][c] == player) and (
                                board[r][c - 1] == '.' or board[r][c - 1] == player) and (board[r][c + 1] == '.' or board[r][c + 1] == player):
                            eval_num += 10
                        
                #last and next-to-last rows
                elif r == self.size - 1 or r == self.size - 2:
                    #up or right only
                    if c == 1:
                        if board[r][c] == player and (board[r - 1][c] == '.' or board[r - 1][c] == player) and (
                                board[r][c + 1] == '.' or board[r][c + 1] == player):
                            eval_num += 10
                                            #up or left only
                    elif c == self.size - 2:
                        if board[r][c] == player and (board[r - 1][c] == '.' or board[r - 1][c] == player) and (
                                board[r][c - 1] == '.' or board[r][c - 1] == player):
                            eval_num += 10
                                            #up, left, or right
                    else:
                        if board[r][c] == player and (board[r - 1][c] == '.' or board[r - 1][c] == player) and (
                                board[r][c + 1] == '.' or board[r][c + 1] == player) and (board[r][c - 1] == '.' or board[r][c - 1] == player):
                            eval_num += 10
                        

                #all other spaces within board's two outermost rows and columns
                else:
                    if board[r][c] == player and (board[r][c + 1] == '.' or board[r][c + 1] == player) and (board[r][c - 1] == '.' or board[r][c - 1] == player) and (board[r + 1][c] == '.' or board[r + 1][c] == player) and (board[r - 1][c] == '.' or board[r - 1][c] == player):
                        eval_num += 10


# game = Konane(8)
# game.playNGames(1, SimplePlayer(8), MinimaxPlayer(8, 3), 1)




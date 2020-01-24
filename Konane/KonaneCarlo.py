#Carlo Gonzalez, Heather Murray
#
#

from konane import *


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

        # we added this to have a depth
        self.bestValue = 0

    def getMove(self, board):
        # complete this
        # provides child nodes of each move on board
        moves = self.generateMoves(board, self.side)
        bestMove = []
        alpha = -float("inf")
        beta = float("inf")
        val = 0
        
        for element in moves:
            val = self.minmax(self.nextBoard(board, self.side, element), self.limit - 1, self.side, alpha, beta)
            if val > alpha:
                bestMove = element
                alpha = val
            
        return bestMove

        #returns eitherh
        #   heuristic value from terminal node,
        #   alpha from max, or
        #   beta from min
    def minmax(self, board, m_depth, player, alpha, beta):
    
        moves = self.generateMoves(board, player)
        n = len(moves)
        # alpha = -float("inf")
        # beta = float("inf")

        # base case)
        # if score == 10 or score == -10:
        #     return score

        if n == 0:
            if player == self.side:
                return -float("inf")
            else:
                return float("inf")

        if m_depth == 0:
            return self.eval(board)

        if player == self.side:
            for element in moves:
                score = self.minmax(self.nextBoard(board, player, element), m_depth - 1, self.opponent(player), alpha, beta)
                alpha = max(alpha, score)
                # pruning condition; don't explore any more children
                if alpha >= beta:
                    break

            return alpha
        else:
            for element in moves:
                beta = min(beta, self.minmax(self.nextBoard(board, player, element), m_depth - 1, self.opponent(player)))
                if alpha >= beta:
                    break
            return beta


    def eval(self, board):
        # complete this – this will be your evaluation function.
        # Eval just quantifies each move.
        # High values should be good for max.
        # Compare all the moves and see which one is the best.
        # RETURNS A NUMBER - good or bad for Max

        # iterative deepening or best first search
        #    'W' surrounded by 'W' or '.'
        # calculate if no moves left for W, return +sys.maxsize
        # calculate if no moves left for B, return -sys.maxsize

        # number of pieces left for the current move - value of 1
        piecesLeftW = Konane.countSymbol(self, board,'W')
        piecesLeftB = Konane.countSymbol(self, board,'B') 
        # if piecesLeftB > piecesLeftW:
        #     piecesLeft = 1

        nextMovesW = len(self.generateMoves(board, 'W'))
        nextMovesB = len(self.generateMoves(board, 'B'))

        if nextMovesB == 0:
            return -float("inf")
        if nextMovesW == 0:
            return float("inf")
        # number of double jumps - value of 2

        mostJumps = 0
        for m in self.generateMoves(board, self.side):
            jumps = 0
            if m[0] != m[2]:
                jumps = abs( (m[0] - m[2]) / 2)
            if m[1] != m[3]:
                jumps = abs( (m[1] - m[3]) / 2)
            if jumps > mostJumps:
                mostJumps =  jumps

        # and another value
        block_white = 0
        # for r in range(self.size-2):
        #     for c in range(self.size-2):
        #         if board[r][c] == 'W' and (board[r+1][c] == '.' or board[r+1][c] == 'W'):
        #             block_white += 1
        #         if board[r][c] == 'W' and (board[r][c+1] == '.' or board[r][c+1] == 'W'):
        #             block_white += 1
        #         if c != 0:
        #             if board[r][c] == 'W' and (board [r][c-1] == '.' or board[r][c-1] == 'W'):
        #                 block_white += 1
        #         if r != 0:
        #             if board[r][c] == 'W' and (board [r-1][c] == '.' or board[r-1][c] == 'W'):
        #                 block_white += 1

        #         if board[r][c] == 'W' and (board[r+1][c] == '.' or board[r+1][c] == 'W') and (board[r][c+1] == '.' or board[r][c+1] == 'W'):
        #             if r != 0:
        #                 if (board[r - 1][c] == '.' or board[r - 1][c] == 'W'):
        #                     block_white += 3
        #             if c != 0:
        #                 if (board [r][c-1] == '.' or board[r][c-1] == 'W'):
        #                     block_white += 3

     

        # placing weights
        value = ((nextMovesB - nextMovesW )) + ((piecesLeftB - piecesLeftW) * 0) + (block_white * 0) + (mostJumps * 0)
        return value

# game = Konane(8)
# game.playNGames(1, SimplePlayer(8), MinimaxPlayer(8, 3), 1)
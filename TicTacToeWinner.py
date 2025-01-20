"""
Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:

Players take turns placing characters into empty squares ' '.
The first player A always places 'X' characters, while the second player B always places 'O' characters.
'X' and 'O' characters are always placed into empty squares, never on filled ones.
The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.

Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be 
played on grid[rowi][coli]. return the winner of the game if it exists (A or B). 
In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".

You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), 
the grid is initially empty, and A will play first.

Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: A wins, they always play first.
"""

def findWinner(moves):
    win_moves = [
        [(0, 0), (0, 1), (0, 2)], [(0, 0), (1,0), (2,0)],
        [(0, 1), (1,1), (2, 1)], [(1,0), (1,1), (1,2)],
        [(0,2), (1,2), (2,2)], [(2,0), (2,1), (2,2)],
        [(0,0), (1,1), (2,2)], [(0,2), (1,1), (2,0)]
    ]

    moves_a = [(move[0], move[1]) for move in moves[::2]]
    moves_b = [(move[0], move[1]) for move in moves[1::2]]

    for win_move in win_moves:
        if win_move[0] in moves_a and win_move[1] in moves_a and win_move[2] in moves_a:
            return "A"
        if win_move[0] in moves_b and win_move[1] in moves_b and win_move[2] in moves_b:
            return "B"
    
    if len(moves) < 9:
        return "Pending"
    
    return "Draw"

moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
print(moves, findWinner(moves))

moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
print(moves, findWinner(moves))

moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
print(moves, findWinner(moves))

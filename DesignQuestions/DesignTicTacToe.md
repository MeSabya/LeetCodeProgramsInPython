Suppose that two players are playing a game of tic-tac-toe on an n x n board. They are following specific rules to play and win the game.

A move is guaranteed to be valid if a mark is placed on an empty block.
No more moves are allowed once a winning condition is reached.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Your task is to implement a TicTacToe class, which will be used by two players to play the game and win fairly.

Given the 2D array containing the inputs for the TicTacToe object and the move function, you have to implement the TicTacToe class.

Assume that you have the following input array:

[[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]


Here, the first index of the 2D array is the input for the TicTacToe object and the rest of the indexes will be used as input for the move function.

Keep in mind the following functionalities that need to be implemented:

TicTacToe class, which declares an object to create the board.
__init__(self, n), which initializes the object of TicTacToe to create the board of size n.
move(row int, col int, player int), which indicates that the player with ID player plays at the cell (row, col) of the board. The move is guaranteed to be a valid move.

## Solution
While playing tic-tac-toe, we must find if the player has won. A player can win by marking an entire row, column, diagonal, or anti-diagonal cells. We can solve this problem in a constant time.

Let’s break the problem into two parts.

First, if there are n rows and n columns on a board, at each move, we must check if the player has already marked all of the cells in a row or column, that is, the certain row or column is marked n times.

Second, we must check if the player marked all the cells on the diagonal or anti-diagonal on every move. There can only be one diagonal and one anti-diagonal, no matter what the size of the board is.

From the given conditions, we know that a move is always valid and placed on an empty cell. So, we can be certain that if a player has marked any row n times, they must have marked a different column each time.

As there are always n cells on the diagonal or anti-diagonal, the player must mark the cells on the diagonal or anti-diagonal n times to win the game, either by diagonal or anti-diagonal.


## Algorithm
From the discussion, we can conclude that we need a data structure to count how many times a player marks a row, column, or diagonal.

👉 To implement the first part we will proceed as follows:

For each player, we will build an array, rows, of size n, where rows will store the number of times a player has marked a cell on the 
i th row. Likewise, for each player, we will also build an array, cols, of size n, which will store the number of times a player marks a cell on the 
i th col.

Here, the winning condition will be if either rows[i] or cols[j] is equal to n after the player marks the cell on 
i th  row and j th col.

👉 To implement the second part, we can use a similar idea:
There is only one diagonal and one anti-diagonal. For each player, we will use integer variables (diagonal, anti-diagonal) for the diagonal and antidiagonal. These variables will store how many times a cell is marked on each of the diagonals.

Here, a player will win if the value of the diagonal is equal to n, after the player marks a cell on a diagonal row. Similarly, a player will win if the value of the anti_diagonal variable for that player is equal to n, after the player marks a cell on an anti-diagonal row.

```python
import math

class TicTacToe:

    # TicTacToe class contains rows, cols, diagonal,
	# and anti_diagonal to create a board.
    # Constructor is used to create n * n tic - tac - toe board.

    def __init__(self, n): 
        self.rows = [0] * (n)
        self.cols = [0] * (n)
        self.diagonal = 0 
        self.anti_diagonal = 0 

    # Move function will allow the players to play the game
    # for given row and col.
    def move(self, row, col, player):

         # current_player will be used to keep track of players, 
         # i.e.,1 for player 1 and - 1 for player 2.
        current_player = -1
        if player == 1:
            current_player = 1

        # Update current_player in rows and cols lists.
        self.rows[row] += current_player
        self.cols[col] += current_player

        # Update diagonal.
        if row == col: 
            self.diagonal += current_player

        # Update anti diagonal
        if col == (len(self.cols) - row - 1): 
            self.anti_diagonal += current_player

        n = len(self.rows)

        # Check if the current player wins
        if abs(self.rows[row]) == n or abs(self.cols[col]) == n or abs(self.diagonal) == n or abs(self.anti_diagonal) == n: 
            return player
        
        return 0

 # Driver code
input = [
    [3],
    [0, 0, 1],
    [0, 2, 2],
    [2, 2, 1],
    [1, 1, 2],
    [2, 0, 1],
    [1, 0, 2],
    [2, 1, 1]
]

ticTacToe = TicTacToe(input[0][0])
win = 0

for i in range(1,len(input)): 
    print("Player " + str(input[i][2]) + " makes a move at (" + str(input[i][0]) + ", " + str(input[i][1]) + ")")
    
    win = ticTacToe.move(input[i][0], input[i][1], input[i][2])

    if (win == 0): 
        print("No one wins")
    else :
        print("Player " + str(win) + " wins")
        break
 ```

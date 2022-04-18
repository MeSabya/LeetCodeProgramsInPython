# Problem Description 

```doc
Design a Snake game that is played on a device with screen size = width x height. 
Play the game online if you are not familiar with the game.

The snake is initially positioned at the top left corner (0,0) with length = 1 unit.

You are given a list of food's positions in row-column order. 
When a snake eats the food, its length and the game's score both increase by 1.

Each food appears one by one on the screen. 
For example, the second food will not appear until the first food was eaten by the snake.

When a food does appear on the screen, 
it is guaranteed that it will not appear on a block occupied by the snake.

When snake crosses itself, the game will over. 

Example:
Given width = 3, height = 2, and food = [[1,2],[0,1]].

Snake snake = new Snake(width, height, food);

Initially the snake appears at position (0,0) and the food at (1,2).

|S| | |
| | |F|

snake.move("R"); -> Returns 0

| |S| |
| | |F|

snake.move("D"); -> Returns 0

| | | |
| |S|F|

snake.move("R"); -> Returns 1 (Snake eats the first food and right after that, the second food appears at (0,1) )

| |F| |
| |S|S|

snake.move("U"); -> Returns 1

| |F|S|
| | |S|

snake.move("L"); -> Returns 2 (Snake eats the second food)

| |S|S|
| | |S|

snake.move("U"); -> Returns -1 (Game over because snake collides with border)
```

```python
from collections import deque

class SnakeGame(object):

    def __init__(self, width,height,food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.__width = width
        self.__height = height
        self.__score = 0
        self.__f = 0
        self.__food = food
        self.__snake = deque([(0, 0)])
        self.__direction = {"U": (-1, 0), "L": (0, -1), "R": (0, 1), "D": (1, 0)}
        self.__lookup = {(0, 0)}

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        def valid(x, y):
            return 0 <= x < self.__height and \
                   0 <= y < self.__width and \
                   (x, y) not in self.__lookup
        d = self.__direction[direction]
        x, y = self.__snake[-1][0] + d[0], self.__snake[-1][1] + d[1]
        self.__lookup.remove(self.__snake[0])
        tail = self.__snake.popleft()
        if not valid(x, y):
            return -1
        elif self.__f != len(self.__food) and (self.__food[self.__f][0], self.__food[self.__f][1]) == (x, y):
            self.__score += 1
            self.__f += 1
            self.__snake.appendleft(tail)
            self.__lookup.add(tail)
        self.__snake.append((x, y))
        self.__lookup.add((x, y))
        return self.__score
```

## Explanation:

**Check the constraints in the given problem description**:

1. Each food appears one by one on the screen. you need to keep a counter to manage food.
2. When a snake eats the food, its length and the game's score both increase by 1. How to maintain/ensure the snake length is increased?
3. When snake crosses itself, the game will over. How do you know the snake has crossed itself, where are you going to maintain this stuff ?

### Answer is:

1. We should use list (```self.__food```) to store the given food coordinates. Then we will maintain a counter to know how many food coordinates we are already processed. ```self.__f``` 
   is the counter we are using to mark the current food coordinates from the food vector.
   
2. We should store snake's position in a list . when the snake eats food at a coordinates lets say at (x, y), we should add (x, y) to the snakes position list.

3. using a lookup dictionary.







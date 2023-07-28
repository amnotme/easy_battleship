# Floating Fortress - Battleship Implementation

Welcome to Floating Fortress - a battleship implementation! Engage in an exciting battle of wits and strategy as you try to sink your opponent's warships on a hidden grid.

## Instructions

1. The hidden location of the warships should be determined in each of the two players' identical grids, while keeping in mind that they cannot join or overlap.

2. Each ship is depicted as a line of m squares, where m indicates the volume of the ship.

3. Each player needs to select a location on the opponent's grid to launch an attack against.

4. If the attack hits an opponent's ship, the opponent's ship sinks.

5. The player who manages to sink all of their opponent's ships wins!

## How to Play

### Setup

1. Run the Python script to start the game.
2. Enter the names of Player 1 and Player 2 when prompted.
3. Choose the size of the board (between 1 and 20) and the number of ships (between 1 and 5) for each player.

### Placing Ships

1. Player 1 will be prompted to set their ships on the board. The board will be displayed, and you will be asked to enter the location for each ship in the format "row,column" (e.g., "1,3" or "4,2").
2. Make sure to place your ships within your grid's boundaries and in empty spaces.
3. Repeat the process until all the ships are placed for Player 1.

### Gameplay

1. The game will notify you when it's your turn.
2. You will see a board with symbols representing different elements:
   - "^": Your ship
   - "H": Hit (when you hit an opponent's ship)
   - "w": Water (when you miss the opponent's ship)
   - "0": Empty space
3. Enter the coordinates of your attack in the format "row,column" (e.g., "1,3" or "4,2") to attack your opponent's grid.
4. If your attack hits your opponent's ship, you will be informed that it was a direct hit.
5. If your attack misses, you will be notified that you missed.
6. The game will switch to the other player after each turn.
7. The game will continue until one player sinks all of their opponent's ships.

### Winning the Game

The first player to sink all of their opponent's ships will be declared the winner!

## Example

To give you a better idea of the game, here's a quick example of how the game might progress:

```
$ python floating_fortress.py

What's player's 1 name? Alice
What's player's 2 name? Bob
How big would you like your board to be? (size >= 1 and size <= 20): 10
How many ships would you like? (ships >= 1 and ships <= 5): 3

===========================
    let the games begin    
===========================

It's your turn, Alice. Here's your board:
^ 0 0 0 0 0 0 0 0 0 |1*
0 0 0 0 0 0 0 0 0 0 |2*
0 0 0 0 0 0 0 0 0 0 |3*
0 0 0 0 0 0 0 0 0 0 |4*
0 0 0 0 0 0 0 0 0 0 |5*
0 0 0 0 0 0 0 0 0 0 |6*
0 0 0 0 0 0 0 0 0 0 |7*
0 0 0 0 0 0 0 0 0 0 |8*
0 0 0 0 0 0 0 0 0 0 |9*
0 0 0 0 0 0 0 0 0 0 |10*

Where would you like to attack? (row,column), like : '1,3' or '4,2': 5,5

That was a direct hit! Great job!

...
```

## Conclusion

Thank you for playing Floating Fortress Battleship! Have fun and may the best strategist win!

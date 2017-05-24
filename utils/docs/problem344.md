![projecteuler.net](images/print_page_logo.png)

## Silver dollar game

### Problem 344 ![](images/icon_info.png)Published on Saturday, 25th June
2011, 07:00 pm; Solved by 227;  
Difficulty rating: 100%

One variant of N.G. de Bruijn's **silver dollar** game can be described as
follows:

On a strip of squares a number of coins are placed, at most one coin per
square. Only one coin, called the **silver dollar**, has any value. Two
players take turns making moves. At each turn a player must make either a
_regular_ or a _special_ move.

A _regular_ move consists of selecting one coin and moving it one or more
squares to the left. The coin cannot move out of the strip or jump on or over
another coin.

Alternatively, the player can choose to make the _special_ move of pocketing
the leftmost coin rather than making a regular move. If no regular moves are
possible, the player is forced to pocket the leftmost coin.

The winner is the player who pockets the silver dollar.

![p344_silverdollar.gif](project/images/p344_silverdollar.gif)  

A _winning configuration_ is an arrangement of coins on the strip where the
first player can force a win no matter what the second player does.

Let W(n,c) be the number of winning configurations for a strip of n squares, c
worthless coins and one silver dollar.

You are given that W(10,2) = 324 and W(100,10) = 1514704946113500.

Find W(1 000 000, 100) modulo the semiprime 1000 036 000 099 (= 1 000 003 · 1
000 033).

  
  


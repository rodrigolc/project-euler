![projecteuler.net](images/print_page_logo.png)

## Spilling the beans

### Problem 334 ![](images/icon_info.png)Published on Saturday, 23rd April
2011, 04:00 pm; Solved by 341;  
Difficulty rating: 65%

In Plato's heaven, there exist an infinite number of bowls in a straight line.  
Each bowl either contains some or none of a finite number of beans.  
A child plays a game, which allows only one kind of move: removing two beans
from any bowl, and putting one in each of the two adjacent bowls.  
The game ends when each bowl contains either one or no beans.

For example, consider two adjacent bowls containing 2 and 3 beans
respectively, all other bowls being empty. The following eight moves will
finish the game:

![p334_beans.gif](project/images/p334_beans.gif)

You are given the following sequences:  

t_0_ = 123456.  
---  
t_i_ =  | ![p334_cases.gif](project/images/p334_cases.gif) |  |  |  | t_i-1_  
---  
2  
,  |  |  if t_i-1_ is even  
![p334_lfloor.gif](project/images/p334_lfloor.gif) |  | t_i-1_  
---  
2  
![p334_rfloor.gif](project/images/p334_rfloor.gif) |  926252,  |  if t_i-1_ is
odd  
|  |  where ⌊x⌋ is the floor function  
|  |  and ![p334_oplus.gif](project/images/p334_oplus.gif) is the bitwise XOR
operator.  
b_i_ = ( t_i_ mod 211) + 1.  
---  
  
The first two terms of the last sequence are b_1_ = 289 and b_2_ = 145.  
If we start with b_1_ and b_2_ beans in two adjacent bowls, 3419100 moves
would be required to finish the game.

Consider now 1500 adjacent bowls containing b_1_, b_2_,..., b_1500_ beans
respectively, all other bowls being empty. Find how many moves it takes before
the game ends.

  
  


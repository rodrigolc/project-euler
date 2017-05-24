![projecteuler.net](images/print_page_logo.png)

## Searching for a maximum-sum subsequence

### Problem 149 ![](images/icon_info.png)Published on Friday, 13th April 2007,
10:00 pm; Solved by 3545;  
Difficulty rating: 50%

Looking at the table below, it is easy to verify that the maximum possible sum
of adjacent numbers in any direction (horizontal, vertical, diagonal or anti-
diagonal) is 16 (= 8 + 7 + 1).

−2| 5| 3| 2  
---|---|---|---  
9| −6| 5| 1  
3| 2| 7| 3  
−1| 8| −4|   8  
  
Now, let us repeat the search, but on a much larger scale:

First, generate four million pseudo-random numbers using a specific form of
what is known as a "Lagged Fibonacci Generator":

For 1 ≤ _k_ ≤ 55, _s__k_ = [100003 − 200003_k_ \+ 300007_k_3] (modulo 1000000)
− 500000.  
For 56 ≤ _k_ ≤ 4000000, _s__k_ = [_s__k−24_ \+ _s__k−55_ \+ 1000000] (modulo
1000000) − 500000.

Thus, _s_10 = −393027 and _s_100 = 86613.

The terms of _s_ are then arranged in a 2000×2000 table, using the first 2000
numbers to fill the first row (sequentially), the next 2000 numbers to fill
the second row, and so on.

Finally, find the greatest sum of (any number of) adjacent entries in any
direction (horizontal, vertical, diagonal or anti-diagonal).

  
  


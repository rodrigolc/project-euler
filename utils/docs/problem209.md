![projecteuler.net](images/print_page_logo.png)

## Circular Logic

### Problem 209 ![](images/icon_info.png)Published on Friday, 19th September
2008, 06:00 pm; Solved by 1896;  
Difficulty rating: 60%

A k-input _binary truth table_ is a map from k input bits (binary digits, 0
[false] or 1 [true]) to 1 output bit. For example, the 2-input binary truth
tables for the logical AND and XOR functions are:

x | y | x AND y  
---|---|---  
0| 0| 0  
0| 1| 0  
1| 0| 0  
1| 1| 1  
x | y | x XOR y  
---|---|---  
0| 0| 0  
0| 1| 1  
1| 0| 1  
1| 1| 0  
  
  

How many 6-input binary truth tables, τ, satisfy the formula

τ(a, b, c, d, e, f) AND τ(b, c, d, e, f, a XOR (b AND c)) = 0

  

for all 6-bit inputs (a, b, c, d, e, f)?

  
  


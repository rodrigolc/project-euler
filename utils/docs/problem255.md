![projecteuler.net](images/print_page_logo.png)

## Rounded Square Roots

### Problem 255 ![](images/icon_info.png)Published on Friday, 11th September
2009, 09:00 pm; Solved by 672;  
Difficulty rating: 75%

We define the _rounded-square-root_ of a positive integer n as the square root
of n rounded to the nearest integer.

The following procedure (essentially Heron's method adapted to integer
arithmetic) finds the rounded-square-root of n:

Let d be the number of digits of the number n.  
If d is odd, set x0 = 2×10(d-1)⁄2.  
If d is even, set x0 = 7×10(d-2)⁄2.  
Repeat:

![p255_Heron.gif](project/images/p255_Heron.gif)

until xk+1 = xk.

As an example, let us find the rounded-square-root of n = 4321.  
n has 4 digits, so x0 = 7×10(4-2)⁄2 = 70.  
![p255_Example.gif](project/images/p255_Example.gif)  
Since x2 = x1, we stop here.  
So, after just two iterations, we have found that the rounded-square-root of
4321 is 66 (the actual square root is 65.7343137…).

The number of iterations required when using this method is surprisingly low.  
For example, we can find the rounded-square-root of a 5-digit integer (10,000
≤ n ≤ 99,999) with an average of 3.2102888889 iterations (the average value
was rounded to 10 decimal places).

Using the procedure described above, what is the average number of iterations
required to find the rounded-square-root of a 14-digit number (1013 ≤ n &lt;
1014)?  
Give your answer rounded to 10 decimal places.

Note: The symbols ⌊x⌋ and ⌈x⌉ represent the floor function and ceiling
function respectively.

  
  


![projecteuler.net](images/print_page_logo.png)

## abc-hits

### Problem 127 ![](images/icon_info.png)Published on Friday, 1st September
2006, 06:00 pm; Solved by 4482;  
Difficulty rating: 50%

The radical of _n_, rad(_n_), is the product of distinct prime factors of _n_.
For example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.

We shall define the triplet of positive integers (_a_, _b_, _c_) to be an abc-
hit if:

  1. GCD(_a,_ _b_) = GCD(_a_, _c_) = GCD(_b_, _c_) = 1
  2. _a_ &lt; _b_
  3. _a_ \+ _b_ = _c_
  4. rad(_abc_) &lt; _c_

For example, (5, 27, 32) is an abc-hit, because:

  1. GCD(5, 27) = GCD(5, 32) = GCD(27, 32) = 1
  2. 5 &lt; 27
  3. 5 + 27 = 32
  4. rad(4320) = 30 &lt; 32

It turns out that abc-hits are quite rare and there are only thirty-one abc-
hits for _c_ &lt; 1000, with ∑_c_ = 12523.

Find ∑_c_ for _c_ &lt; 120000.

  
  


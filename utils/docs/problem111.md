![projecteuler.net](images/print_page_logo.png)

## Primes with runs

### Problem 111 ![](images/icon_info.png)Published on Friday, 16th December
2005, 06:00 pm; Solved by 5273;  
Difficulty rating: 45%

Considering 4-digit primes containing repeated digits it is clear that they
cannot all be the same: 1111 is divisible by 11, 2222 is divisible by 22, and
so on. But there are nine 4-digit primes containing three ones:

1117, 1151, 1171, 1181, 1511, 1811, 2111, 4111, 8111

We shall say that M(_n_, _d_) represents the maximum number of repeated digits
for an _n_-digit prime where _d_ is the repeated digit, N(_n_, _d_) represents
the number of such primes, and S(_n_, _d_) represents the sum of these primes.

So M(4, 1) = 3 is the maximum number of repeated digits for a 4-digit prime
where one is the repeated digit, there are N(4, 1) = 9 such primes, and the
sum of these primes is S(4, 1) = 22275. It turns out that for _d_ = 0, it is
only possible to have M(4, 0) = 2 repeated digits, but there are N(4, 0) = 13
such cases.

In the same way we obtain the following results for 4-digit primes.

**Digit, _d_** | **M(4, _d_)** | **N(4, _d_)** | **S(4, _d_)**  
---|---|---|---  
0 | 2 | 13 | 67061  
1 | 3 | 9 | 22275  
2 | 3 | 1 | 2221  
3 | 3 | 12 | 46214  
4 | 3 | 2 | 8888  
5 | 3 | 1 | 5557  
6 | 3 | 1 | 6661  
7 | 3 | 9 | 57863  
8 | 3 | 1 | 8887  
9 | 3 | 7 | 48073  
  
For _d_ = 0 to 9, the sum of all S(4, _d_) is 273700.

Find the sum of all S(10, _d_).

  
  


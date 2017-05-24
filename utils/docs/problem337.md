![projecteuler.net](images/print_page_logo.png)

## Totient Stairstep Sequences

### Problem 337 ![](images/icon_info.png)Published on Saturday, 7th May 2011,
10:00 pm; Solved by 357;  
Difficulty rating: 70%

Let {a1, a2,..., an} be an integer sequence of length n such that:

  * a1 = 6
  * for all 1 ≤ i &lt; n : φ(ai) &lt; φ(ai+1) &lt; ai &lt; ai+11

Let S(N) be the number of such sequences with an ≤ N.  
For example, S(10) = 4: {6}, {6, 8}, {6, 8, 9} and {6, 10}.  
We can verify that S(100) = 482073668 and S(10 000) mod 108 = 73808307.

Find S(20 000 000) mod 108.

1 φ denotes **Euler's totient function**.

  
  


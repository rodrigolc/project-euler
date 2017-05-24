![projecteuler.net](images/print_page_logo.png)

## Efficient exponentiation

### Problem 122 ![](images/icon_info.png)Published on Friday, 2nd June 2006,
06:00 pm; Solved by 5634;  
Difficulty rating: 40%

The most naive way of computing _n_15 requires fourteen multiplications:

_n_ × _n_ × ... × _n_ = _n_15

But using a "binary" method you can compute it in six multiplications:

_n_ × _n_ = _n_2  
_n_2 × _n_2 = _n_4  
_n_4 × _n_4 = _n_8  
_n_8 × _n_4 = _n_12  
_n_12 × _n_2 = _n_14  
_n_14 × _n_ = _n_15

However it is yet possible to compute it in only five multiplications:

_n_ × _n_ = _n_2  
_n_2 × _n_ = _n_3  
_n_3 × _n_3 = _n_6  
_n_6 × _n_6 = _n_12  
_n_12 × _n_3 = _n_15

We shall define m(_k_) to be the minimum number of multiplications to compute
_n__k_; for example m(15) = 5.

For 1 ≤ _k_ ≤ 200, find ∑ m(_k_).

  
  


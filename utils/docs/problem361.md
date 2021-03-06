![projecteuler.net](images/print_page_logo.png)

## Subsequence of Thue-Morse sequence

### Problem 361 ![](images/icon_info.png)Published on Sunday, 4th December
2011, 04:00 am; Solved by 230;  
Difficulty rating: 90%

The **Thue-Morse sequence** {Tn} is a binary sequence satisfying:

  * T0 = 0
  * T2n = Tn
  * T2n+1 = 1 - Tn

The first several terms of {Tn} are given as follows:  
01101001100101101001011001101001....

We define {An} as the sorted sequence of integers such that the binary
expression of each element appears as a subsequence in {Tn}.  
For example, the decimal number 18 is expressed as 10010 in binary. 10010
appears in {Tn} (T8 to T12), so 18 is an element of {An}.  
The decimal number 14 is expressed as 1110 in binary. 1110 never appears in
{Tn}, so 14 is not an element of {An}.

The first several terms of An are given as follows:  

n| 0| 1| 2| 3| 4| 5| 6| 7| 8| 9| 10| 11| 12| …  
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---  
An| 0| 1| 2| 3| 4| 5| 6| 9| 10| 11| 12| 13| 18| …  
  
We can also verify that A100 = 3251 and A1000 = 80852364498.

Find the last 9 digits of ![p361_Thue-Morse1.gif](project/images/p361_Thue-
Morse1.gif).

  
  


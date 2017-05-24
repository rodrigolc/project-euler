![projecteuler.net](images/print_page_logo.png)

## Special subset sums: testing

### Problem 105 ![](images/icon_info.png)Published on Friday, 23rd September
2005, 06:00 pm; Solved by 5775;  
Difficulty rating: 45%

Let S(A) represent the sum of elements in set A of size _n_. We shall call it
a special sum set if for any two non-empty disjoint subsets, B and C, the
following properties are true:

  1. S(B) ≠ S(C); that is, sums of subsets cannot be equal.
  2. If B contains more elements than C then S(B) &gt; S(C).

For example, {81, 88, 75, 42, 87, 84, 86, 65} is not a special sum set because
65 + 87 + 88 = 75 + 81 + 84, whereas {157, 150, 164, 119, 79, 159, 161, 139,
158} satisfies both rules for all possible subset pair combinations and S(A) =
1286.

Using [sets.txt](project/resources/p105_sets.txt) (right click and "Save
Link/Target As..."), a 4K text file with one-hundred sets containing seven to
twelve elements (the two examples given above are the first two sets in the
file), identify all the special sum sets, A1, A2, ..., A_k_, and find the
value of S(A1) + S(A2) + ... + S(A_k_).

NOTE: This problem is related to [Problem 103](problem=103) and [Problem
106](problem=106).

  
  


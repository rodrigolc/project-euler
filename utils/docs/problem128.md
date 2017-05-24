![projecteuler.net](images/print_page_logo.png)

## Hexagonal tile differences

### Problem 128 ![](images/icon_info.png)Published on Friday, 29th September
2006, 06:00 pm; Solved by 3565;  
Difficulty rating: 55%

A hexagonal tile with number 1 is surrounded by a ring of six hexagonal tiles,
starting at "12 o'clock" and numbering the tiles 2 to 7 in an anti-clockwise
direction.

New rings are added in the same fashion, with the next rings being numbered 8
to 19, 20 to 37, 38 to 61, and so on. The diagram below shows the first three
rings.

![](project/images/p128.gif)

By finding the difference between tile _n_ and each of its six neighbours we
shall define PD(_n_) to be the number of those differences which are prime.

For example, working clockwise around tile 8 the differences are 12, 29, 11,
6, 1, and 13. So PD(8) = 3.

In the same way, the differences around tile 17 are 1, 17, 16, 1, 11, and 10,
hence PD(17) = 2.

It can be shown that the maximum value of PD(_n_) is 3.

If all of the tiles for which PD(_n_) = 3 are listed in ascending order to
form a sequence, the 10th tile would be 271.

Find the 2000th tile in this sequence.

  
  


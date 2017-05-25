![projecteuler.net](images/print_page_logo.png)

## Bidirectional Recurrence

### Problem 505 ![](images/icon_info.png)Published on Sunday, 1st March 2015,
01:00 am; Solved by 141;  
Difficulty rating: 90%

Let:

$\begin{array}{ll} x(0)&amp;=0 \\\ x(1)&amp;=1 \\\
x(2k)&amp;=(3x(k)+2x(\lfloor \frac k 2 \rfloor)) \text{ mod } 2^{60} \text{
for } k \ge 1 \text {, where } \lfloor \text { } \rfloor \text { is the floor
function} \\\ x(2k+1)&amp;=(2x(k)+3x(\lfloor \frac k 2 \rfloor)) \text{ mod }
2^{60} \text{ for } k \ge 1 \\\ y_n(k)&amp;=\left\\{{\begin{array}{lc} x(k)
&amp;&amp; \text{if } k \ge n \\\ 2^{60} - 1 - max(y_n(2k),y_n(2k+1))
&amp;&amp; \text{if } k &lt; n \end{array}} \right. \\\ A(n)&amp;=y_n(1)
\end{array}$

You are given:

$\begin{array}{ll} x(2)&amp;=3 \\\ x(3)&amp;=2 \\\ x(4)&amp;=11 \\\
y_4(4)&amp;=11 \\\ y_4(3)&amp;=2^{60}-9\\\ y_4(2)&amp;=2^{60}-12 \\\
y_4(1)&amp;=A(4)=8 \\\ A(10)&amp;=2^{60}-34\\\ A(10^3)&amp;=101881
\end{array}$

Find $A(10^{12})$.

  
  

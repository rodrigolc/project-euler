![projecteuler.net](images/print_page_logo.png)

## Investigating multiple reflections of a laser beam

### Problem 144 ![](images/icon_info.png)Published on Friday, 9th March 2007,
05:00 pm; Solved by 4524;  
Difficulty rating: 50%

In laser physics, a "white cell" is a mirror system that acts as a delay line
for the laser beam. The beam enters the cell, bounces around on the mirrors,
and eventually works its way back out.

The specific white cell we will be considering is an ellipse with the equation
4_x_2 \+ _y_2 = 100

The section corresponding to −0.01 ≤ _x_ ≤ +0.01 at the top is missing,
allowing the light to enter and exit through the hole.

![](project/images/p144_1.gif)![](project/images/p144_2.gif)

The light beam in this problem starts at the point (0.0,10.1) just outside the
white cell, and the beam first impacts the mirror at (1.4,-9.6).

Each time the laser beam hits the surface of the ellipse, it follows the usual
law of reflection "angle of incidence equals angle of reflection." That is,
both the incident and reflected beams make the same angle with the normal line
at the point of incidence.

In the figure on the left, the red line shows the first two points of contact
between the laser beam and the wall of the white cell; the blue line shows the
line tangent to the ellipse at the point of incidence of the first bounce.

The slope _m_ of the tangent line at any point (_x_,_y_) of the given ellipse
is: _m_ = −4_x_/_y_

The normal line is perpendicular to this tangent line at the point of
incidence.

The animation on the right shows the first 10 reflections of the beam.

How many times does the beam hit the internal surface of the white cell before
exiting?

  
  


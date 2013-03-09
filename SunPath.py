#! /usr/bin/env python
# import math
import dislin

n = 361
x = range (n)
y1 = range (n)
y2 = range (n)
for i in range (0,n):
  x[i] = i
#  y1[i] = math.sin (v)
#  y2[i] = math.cos (v)

# Dislin Plot!
dislin.metafl ('xwin')
dislin.disini ()
dislin.complx ()
dislin.pagera ()

dislin.axspos (450, 1800)
dislin.axslen (2200, 1200)

dislin.name   ('X-axis', 'X')
dislin.name   ('Y-axis', 'Y')

dislin.labdig (-1, 'X')
dislin.ticks  (9, 'X')
dislin.ticks  (10, 'Y')

dislin.titlin ('Demonstration of CURVE', 1)
dislin.titlin ('SIN (X), COS (X)', 3)

ic = dislin.intrgb (0.95, 0.95, 0.95)
dislin.axsbgd (ic)
 
dislin.graf   (0., 360., 0., 90., -1., 1., -1., 0.5)
dislin.setrgb (0.7, 0.7, 0.7)
dislin.grid   (1,1)

dislin.color  ('fore')
dislin.height (50)
dislin.title  ()

dislin.color  ('red')
dislin.curve  (x, y1, n)
dislin.color  ('green')
dislin.curve  (x, y2, n)
dislin.disfin ()

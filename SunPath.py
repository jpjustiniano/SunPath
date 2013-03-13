#! /usr/bin/env python
# import math
import sys
import dislin

version=0.1
dev='Juan Pablo Justiniano'


lat = sys.argv[1]
lon = sys.argv[2]
# include option to highliht a special day
# include option to change exit format


n = 361
x = range (n)
y1 = range (n)
y2 = range (n)
for i in range (0,n):
  x[i] = i
#  y1[i] = ...
#  y2[i] = ...

# Dislin Plot!
dislin.metafl ('xwin') #diagram format
dislin.disini () #start up dislin
dislin.complx () #Complex text font
dislin.pagera () #Plots borders

dislin.axspos (450, 1800) #defines the X-position of the axis system
dislin.axslen (2200, 1200) #defines the size of an axis system in X-direction

dislin.name   ('Azimuth Angle (Horizontal)', 'X') #Axe name
dislin.name   ('Altitude Angle (Vertical)', 'Y')

dislin.labdig (-1, 'X') #number of decimal places for labels
dislin.ticks  (10, 'X') #number of ticks for the axis
dislin.ticks  (10, 'Y')

dislin.titjus ('Left') #Title alignment
dislin.titlin ('Sun Path Chart', 1)
dislin.titlin ('Orthographic Projection', 3)
dislin.titjus ('Cent') #Title alignment
location = 'Latitud:',str(lat),' ,Longitude:',str(lon) # dejar con 1 decimal
dislin.titlin (location, 2)

ic = dislin.intrgb (0.95, 0.95, 0.95) # explicit colour value from RGB
dislin.axsbgd (ic) #background colour
 
if lat>=0:  # variar para polo norte y sur
	dislin.graf   (60., 300., 0., 15., 0., 90., 0., 10.) 
	#Level 1->2 (XA, XE, XOR, XSTEP, YA, YE, YOR, YSTEP)
else:
	dislin.graf   (240., 480., 0., 15., 0., 90., 0., 10.)}
	# Change 360.. to 0..
# Add North, South, East and west in second axis

dislin.setrgb (0.7, 0.7, 0.7)# explicit colour value from RGB
dislin.grid   (1,1)#overlays a grid on an axis system. (IX,IYG) grid lines between labels

dislin.color  ('fore')
dislin.height (50) #character height
dislin.title  () #plots a title over an axis

dislin.color  ('red')
dislin.curve  (x, y1, n)
dislin.color  ('green')
dislin.curve  (x, y2, n)

dislin.disfin () #End of plotting. Level 2 -> 0

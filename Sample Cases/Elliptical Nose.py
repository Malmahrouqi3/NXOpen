# Elliptical.py
# Generate the points, connect them with a spline then add a third line to connect the first and last point to the corner point (triangular enclosure)
# n points to define the nose shape
# nose rotation is about the y axis
# so that each point output is multiplied by either sin theta or cos theta

# this code generates .exp and .txt files for a set of n points
# In NX, make a spline, two more splines, then rotation about the Y axis

# XZ Plane (to change the plane, flip the inputs of New_Val)
from Expressions import format_exp, write_exp_file, write_txt_file
expressions_list = list ()
expressions_list101 = list ()

## Nose Control parameters
expressions_list.append (format_exp('Elliptical_Inclination_Angle', 'number', 90, 'Degrees'))
expressions_list.append (format_exp('Elliptical_Length', 'number', 10, 'MilliMeter'))
expressions_list.append (format_exp('Elliptical_Diameter', 'number', -10, 'MilliMeter'))
expressions_list.append (format_exp('Elliptical_xShift', 'number', 10, 'MilliMeter'))
expressions_list.append (format_exp('Elliptical_yShift', 'number', 10, 'MilliMeter'))
expressions_list.append (format_exp('Elliptical_zShift', 'number', 10, 'MilliMeter'))

from math import *
import numpy as np
n = 50

xVal = np.linspace(0, 1, n, endpoint = True)
zVal = np.linspace(0, 1, n, endpoint = True)
for i in range (0,n):
    # Make expressions for points
    Z_part = str(sqrt(1-((xVal[i]-1)**2)))
    x = '(' + str (xVal[i]) + '*Elliptical_Length)*cos (Elliptical_Inclination_Angle)-(Elliptical_Diameter/2)*(' + Z_part + '*sin (Elliptical_Inclination_Angle))'
    z = '(' + str (xVal[i]) + '*Elliptical_Length)*sin (Elliptical_Inclination_Angle)+(Elliptical_Diameter/2)*(' + Z_part + '*cos (Elliptical_Inclination_Angle))'
    New_Val = format_exp ('Elliptical_pt'+ str (i),'pt', 'point(Elliptical_xShift +' + x + ',Elliptical_yShift,' + z + '+Elliptical_zShift)', 'MilliMeter')
    
    expressions_list.append (New_Val)
    expressions_list101.append ('Elliptical_pt'+ str (i))

# add the closing point
# (Elliptical_Length,0,0)
# introducing point rotation would be a circle thus (x^2) + (z^2) = (Elliptical_Length^2)
x = 'Elliptical_Length*cos (Elliptical_Inclination_Angle)'
z = 'Elliptical_Length*sin (Elliptical_Inclination_Angle)'
New_Val = format_exp ('Elliptical_pt_end','pt', 'point(Elliptical_xShift+' + x + ',Elliptical_yShift,' + z + '+Elliptical_zShift)', 'MilliMeter')

expressions_list.append (New_Val)
expressions_list101.append ('Elliptical_pt_end')

write_exp_file (expressions_list, 'Elliptical')
write_txt_file (expressions_list101, 'Elliptical')

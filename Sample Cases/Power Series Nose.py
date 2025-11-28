# Power Series.py
# Generate the points, connect them with a spline then add a third line to connect the first and last point to the corner point (triangular enclosure)
# n points to define the nose shape
# nose rotation is about the y axis
# so that each point output is multiplied by either sin theta or cos theta

# this code generates .exp and .txt files for a set of n points
# In NX, make a spline, two more splines, then rotation about the Y axis

# XZ Plane (to change the plane, flip the inputs of New_Val)
from Expressions import format_exp, write_exp_file, write_txt_file
from math import *
import numpy as np

n = 50 #  number of points to define the nose shape
expressions_list = list ()
expressions_list101 = list ()

## Nose Control parameters
expressions_list.append (format_exp('PS_Inclination_Angle', 'number', 90, 'Degrees'))
expressions_list.append (format_exp('PS_Length', 'number', 10, 'MilliMeter'))
expressions_list.append (format_exp('PS_Diameter', 'number', -10, 'MilliMeter'))
expressions_list.append (format_exp('PS_xShift', 'number', 10, 'MilliMeter'))
expressions_list.append (format_exp('PS_yShift', 'number', 10, 'MilliMeter'))
expressions_list.append (format_exp('PS_zShift', 'number', 10, 'MilliMeter'))
expressions_list.append (format_exp('PS_C', 'number', 1, 'MilliMeter'))

xVal = np.linspace(0, 1, n, endpoint = True)

for i in range (0,n):
    # Make the expressions for the points
    # x to establish the x value, z to establish the z values of the nose cone
    # introducing point rotation would be a circle thus (x^2) + (z^2) = (PS_Length^2)
    x = '(' + str (xVal[i]) + '*PS_Length)*cos (PS_Inclination_Angle) - (PS_Diameter/2)*(' + str (xVal[i]) + '^PS_C) *(sin (PS_Inclination_Angle))'
    z = '(' + str (xVal[i]) + '*PS_Length)*sin (PS_Inclination_Angle) + (PS_Diameter/2)*(' + str (xVal[i]) + '^PS_C) *(cos (PS_Inclination_Angle))'
    New_Val = format_exp ('PS_pt'+ str (i),'pt', 'point(PS_xShift +' + x + ',PS_yShift,' + z + '+ PS_zShift)', 'MilliMeter')
    
    expressions_list.append (New_Val)
    expressions_list101.append ('PS_pt'+ str (i))

# add the closing point
# (PS_Length,0,0)
# introducing point rotation would be a circle thus (x^2) + (z^2) = (PS_Length^2)
x = 'PS_Length * cos (PS_Inclination_Angle)'
z = 'PS_Length * sin (PS_Inclination_Angle)'
New_Val = format_exp ('PS_pt_end','pt', 'point(PS_xShift +' + x + ',PS_yShift,' + z + '+ PS_zShift)', 'MilliMeter')

expressions_list.append (New_Val)
expressions_list101.append ('PS_pt_end')

write_exp_file (expressions_list, 'PS')
write_txt_file (expressions_list101, 'PS')

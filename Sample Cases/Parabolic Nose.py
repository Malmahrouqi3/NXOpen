# Parabolic.py
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
expressions_list.append (format_exp('Para_Inclination_Angle', 'number', 90, 'Degrees'))
expressions_list.append (format_exp('Para_Length', 'number', 10, 'MilliMeter'))
expressions_list.append (format_exp('Para_Diameter', 'number', -10, 'MilliMeter'))
expressions_list.append (format_exp('Para_xShift', 'number', 10, 'MilliMeter'))
expressions_list.append (format_exp('Para_yShift', 'number', 10, 'MilliMeter'))
expressions_list.append (format_exp('Para_zShift', 'number', 10, 'MilliMeter'))
expressions_list.append (format_exp('Para_C', 'number', 1, 'MilliMeter'))

from math import *
import numpy as np
n = 50

xVal = np.linspace(0, 1, n, endpoint = True)
zVal = np.linspace(0, 1, n, endpoint = True)

for i in range (0,n):
    # make the expressions for the points here
    # the equation is y = R(((2x/K)-K(x/L)^2)/(2-K))
    # so so Z = R * ((2*xval-k*xval^2)/(2-K))
    Z_part = '((2*'+ str(xVal[i]) + '-Para_C*('+ str(xVal[i]) +'^2))/(2-Para_C))'
    x = '(' + str (xVal[i]) + '*Para_Length)*cos (Para_Inclination_Angle)-(Para_Diameter/2)*(' + Z_part + '*sin (Para_Inclination_Angle))'
    z = '(' + str (xVal[i]) + '*Para_Length)*sin (Para_Inclination_Angle)+(Para_Diameter/2)*(' + Z_part + '*cos (Para_Inclination_Angle))'
    New_Val = format_exp ('Para_pt'+ str (i),'pt', 'point(Para_xShift +' + x + ',Para_yShift,' + z + '+Para_zShift)', 'MilliMeter')
    
    expressions_list.append (New_Val)
    expressions_list101.append ('Para_pt'+ str (i))
    
# add the closing point
# (Para_Length,0,0)
# introducing point rotation would be a circle thus (x^2) + (z^2) = (Para_Length^2)
x = 'Para_Length*cos (Para_Inclination_Angle)'
z = 'Para_Length*sin (Para_Inclination_Angle)'
New_Val = format_exp ('Para_pt_end','pt', 'point(Para_xShift+' + x + ',Para_yShift,' + z + '+Para_zShift)', 'MilliMeter')

expressions_list.append (New_Val)
expressions_list101.append ('Para_pt_end')

write_exp_file (expressions_list, 'Parabolic')
write_txt_file (expressions_list101, 'Parabolic')

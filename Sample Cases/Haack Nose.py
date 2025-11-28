# Haack.py 
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
expressions_list.append (format_exp('Haack_Inclination_Angle', 'number', 0, 'Degrees'))
expressions_list.append (format_exp('Haack_Length', 'number', 10, 'MilliMeter'))
expressions_list.append (format_exp('Haack_Diameter', 'number', -10, 'MilliMeter'))
expressions_list.append (format_exp('Haack_xShift', 'number', 0, 'MilliMeter'))
expressions_list.append (format_exp('Haack_yShift', 'number', 0, 'MilliMeter'))
expressions_list.append (format_exp('Haack_zShift', 'number', 0, 'MilliMeter'))
expressions_list.append (format_exp('Haack_C', 'number', 0, ''))

from math import *
import numpy as np
n = 50

xVal = np.linspace(0, 1, n, endpoint = True)
zVal = np.linspace(0, 1, n, endpoint = True)

t = 0    # t should be a scalar value t
for i in range (0,n):
    t = acos(1-2*xVal[i])
    # t1, t2, t3 gives the inputs for the sqrt () of the Haack Equation
    t1 = str(t)
    t2 = str((sin(2*t))/2)
    t3 = 'Haack_C*' + str((sin(t))**3)
    Z_part = 'sqrt (('+t1+'-'+t2+'+'+t3+')/pi())'
    # make expressions for points
    x = '(' + str (xVal[i]) + '*Haack_Length)*cos (Haack_Inclination_Angle)-(Haack_Diameter/2)*((' + Z_part + ')*sin (Haack_Inclination_Angle))'
    z = '(' + str (xVal[i]) + '*Haack_Length)*sin (Haack_Inclination_Angle)+(Haack_Diameter/2)*((' + Z_part + ')*cos (Haack_Inclination_Angle))'
    New_Val = format_exp ('Haack_pt'+ str (i),'pt', 'point(Haack_xShift +' + x + ',Haack_yShift,' + z + '+Haack_zShift)', 'MilliMeter')
    
    expressions_list.append (New_Val)
    expressions_list101.append ('Haack_pt'+ str (i))

# add the closing point
# (Para_Length,0,0)
# introducing point rotation would be a circle thus (x^2) + (z^2) = (Haack_Length^2)
x = 'Haack_Length*cos (Haack_Inclination_Angle)'
z = 'Haack_Length*sin (Haack_Inclination_Angle)'
New_Val = format_exp ('Haack_pt_end','pt', 'point(Haack_xShift+' + x + ',Haack_yShift,' + z + '+Haack_zShift)', 'MilliMeter')

expressions_list.append (New_Val)
expressions_list101.append ('Haack_pt_end')

write_exp_file (expressions_list, 'Haack')
write_txt_file (expressions_list101, 'Haack')

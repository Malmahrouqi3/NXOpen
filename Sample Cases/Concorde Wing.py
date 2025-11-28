from Expressions import format_exp, write_exp_file, write_txt_file
from Airfoil import Airfoil_XZ
from math import *
import numpy as np

expressions_list = list ()
expressions_list101 = list ()
# Two angles (Elevation angle (airfoil-wise), and Dihedral angle (span-wise))
# We need two airfoils + LE & TE lines
# LE given a specific equation
# TE givne a specific equation - line with sweep angle

## Wing
Airfoil_XZ ('Wing', 'Airfoil_w0', 'S8037 (16%).dat', '') # Root Airfoil
Airfoil_XZ ('Wing', 'Airfoil_w1', 'S8037 (16%).dat', '') # Tip Airfoil

## Set up major expressions
## Control parameters of Leading Edge
expressions_list.append (format_exp('LE_a1', 'number', 0.55, ''))
expressions_list.append (format_exp('LE_a2', 'number', 0.1, ''))
expressions_list.append (format_exp('LE_L', 'number', 350, 'MilliMeter')) # chord-wise length
expressions_list.append (format_exp('LE_max', 'number', 'sin((2*(LE_a2^4)*(Xlim^5) + (LE_a2^2)*(Xlim^3) + (1.2*(LE_a2)*(Xlim)))*180/pi())/LE_a1', ''))
expressions_list.append (format_exp('LE_xShift', 'number', 'Wing_xShift', 'MilliMeter'))
expressions_list.append (format_exp('LE_yShift', 'number', 'Wing_yShift', 'MilliMeter'))
expressions_list.append (format_exp('LE_zShift', 'number', 'Wing_zShift', 'MilliMeter'))

## Control parameters of Tailing Edge
expressions_list.append (format_exp('TE_Length', 'number', 'Wing_B*cos(TE_Sweep_Angle)', 'MilliMeter')) # Tailing Edge Length
expressions_list.append (format_exp('TE_Sweep_Angle', 'number', 10, 'Degrees')) # Tailing Edge Sweep Angle
expressions_list.append (format_exp('TE_xShift', 'number', 'Wing_L + Wing_xShift', 'MilliMeter'))
expressions_list.append (format_exp('TE_yShift', 'number', 'Wing_yShift', 'MilliMeter'))
expressions_list.append (format_exp('TE_zShift', 'number', 'Wing_zShift', 'MilliMeter'))

## Wing (Airfoil_XZ)
expressions_list.append (format_exp('Wing_B', 'number', 275, 'MilliMeter'))
expressions_list.append (format_exp('Wing_xScale', 'number', 1, '')) # Scale up or down x values
expressions_list.append (format_exp('Wing_yScale', 'number', 1, '')) # Scale up or down y values
expressions_list.append (format_exp('Wing_L', 'number', 400, 'MilliMeter'))
expressions_list.append (format_exp('Xlim', 'number', '1.345*pi()', ''))
expressions_list.append (format_exp('Airfoil_w0_Chord', 'number', 'Wing_L', 'MilliMeter'))
expressions_list.append (format_exp('Airfoil_w1_Chord', 'number', 'Wing_L - LE_L + Wing_B*sin (TE_Sweep_Angle)', 'MilliMeter')) # Wing_L- x-axix leading edge length + sweep angle

expressions_list.append (format_exp('Wing_xShift', 'number', 0, 'MilliMeter'))
expressions_list.append (format_exp('Wing_yShift', 'number', 0, 'MilliMeter'))
expressions_list.append (format_exp('Wing_zShift', 'number', 0, 'MilliMeter'))

expressions_list.append (format_exp('Airfoil_w0_xShift', 'number', 'Wing_xShift', 'MilliMeter'))
expressions_list.append (format_exp('Airfoil_w1_xShift', 'number', 'LE_L + Wing_xShift', 'MilliMeter')) # the x-axix leading edge length
expressions_list.append (format_exp('Airfoil_w0_yShift', 'number', 'Wing_yShift', 'MilliMeter'))
expressions_list.append (format_exp('Airfoil_w1_yShift', 'number', 'Wing_B + Wing_yShift', 'MilliMeter'))
expressions_list.append (format_exp('Airfoil_w0_zShift', 'number', 'Wing_zShift', 'MilliMeter'))
expressions_list.append (format_exp('Airfoil_w1_zShift', 'number', 'Wing_zShift', 'MilliMeter'))

write_exp_file (expressions_list, 'Ogive_Expression')

expressions_list = list ()
expressions_list101 = list ()

if True: #Leading Edge
    # the general equation: a1*y = sin(2*(a2^4)*(x^5)+(a2^2)*(x^3)+(1.2*a2*x))
    n = 50
    xVal = np.linspace(0, 1.345*pi, n, endpoint = True)
    for i in range (0,n):
        xpart = str (xVal[i])
        ypart = 'sin((2*(LE_a2^4)*('+xpart+'^5) + (LE_a2^2)*('+xpart+'^3) + (1.2*(LE_a2)*('+xpart+')))*180/pi())/LE_a1'
        # make the expressions for the points here
        x = '(' + xpart + '*LE_L/Xlim)'
        y = '(' + ypart + '*Wing_B/LE_max)'
        New_Val = format_exp ('LE_pt'+ str (i),'pt', 'point(LE_xShift +' + x + ',LE_yShift + ' + y + ',LE_zShift)', '')
        expressions_list.append (New_Val)
        expressions_list101.append ('LE_pt'+ str (i))
    
if True: #Tailing Edge
    # the general equation: y = tan(sweep angle)
    n = 50
    Val = np.linspace(0, 1, n, endpoint = True)
    for i in range (0,n):
        # make the expressions for the points here
        x = '(' + str (Val[i]) + '*Wing_B) * tan (TE_Sweep_Angle)'
        y = '(' + str (Val[i]) + '*Wing_B)'
        New_Val = format_exp ('TE_pt'+ str (i),'pt', 'point(TE_xShift +' + x + ',TE_yShift + ' + y + ',TE_zShift)', '')
        expressions_list.append (New_Val)
        expressions_list101.append ('TE_pt'+ str (i))

write_exp_file (expressions_list, 'Ogive_Lines')
write_txt_file (expressions_list101, 'Ogive_Lines')
from Expressions import format_exp, write_exp_file, write_txt_file
import numpy as np
from math import *

expressions_list = list ()

## Distances on the x axis
expressions_list.append (format_exp('Fuselage_L', 'number', 1000, 'MilliMeter'))
expressions_list.append (format_exp('Section0_L', 'number', 'Fuselage_L*0.2', 'MilliMeter'))
expressions_list.append (format_exp('Section1_L', 'number', 'Fuselage_L*0.4', 'MilliMeter'))
expressions_list.append (format_exp('Section2_L', 'number', 'Fuselage_L*0.6', 'MilliMeter'))
expressions_list.append (format_exp('Section3_L', 'number', 'Fuselage_L*0.8', 'MilliMeter'))
expressions_list.append (format_exp('Section4_L', 'number', 'Fuselage_L', 'MilliMeter'))

expressions_list.append (format_exp('Fuselage_xShift', 'number', 0, 'MilliMeter'))
expressions_list.append (format_exp('Fuselage_yShift', 'number', 0, 'MilliMeter'))
expressions_list.append (format_exp('Fuselage_zShift', 'number', 0, 'MilliMeter'))
##--------------------------------------------------------------------------------
##  First Cross-section
expressions_list.append (format_exp('Section0_A', 'number', 10, ''))
expressions_list.append (format_exp('Section0_B', 'number', 10, ''))
expressions_list.append (format_exp('Section0_C', 'number', 10, ''))
expressions_list.append (format_exp('Section0_xShift', 'number', 0, 'MilliMeter'))
expressions_list.append (format_exp('Section0_yShift', 'number', 0, 'MilliMeter'))
expressions_list.append (format_exp('Section0_zShift', 'number', 0, 'MilliMeter'))
##--------------------------------------------------------------------------------
##  Second Cross-section
expressions_list.append (format_exp('Section1_A', 'number', 10, ''))
expressions_list.append (format_exp('Section1_B', 'number', 10, ''))
expressions_list.append (format_exp('Section1_C', 'number', 10, ''))
expressions_list.append (format_exp('Section1_xShift', 'number', 0, 'MilliMeter'))
expressions_list.append (format_exp('Section1_yShift', 'number', 0, 'MilliMeter'))
expressions_list.append (format_exp('Section1_zShift', 'number', 0, 'MilliMeter'))
##--------------------------------------------------------------------------------
##  Third Cross-section
expressions_list.append (format_exp('Section2_A', 'number', 10, ''))
expressions_list.append (format_exp('Section2_B', 'number', 10, ''))
expressions_list.append (format_exp('Section2_C', 'number', 10, ''))
expressions_list.append (format_exp('Section2_xShift', 'number', 0, 'MilliMeter'))
expressions_list.append (format_exp('Section2_yShift', 'number', 0, 'MilliMeter'))
expressions_list.append (format_exp('Section2_zShift', 'number', 0, 'MilliMeter'))
##--------------------------------------------------------------------------------
##  Fourth Cross-section
expressions_list.append (format_exp('Section3_A', 'number', 10, ''))
expressions_list.append (format_exp('Section3_B', 'number', 10, ''))
expressions_list.append (format_exp('Section3_C', 'number', 10, ''))
expressions_list.append (format_exp('Section3_xShift', 'number', 0, 'MilliMeter'))
expressions_list.append (format_exp('Section3_yShift', 'number', 0, 'MilliMeter'))
expressions_list.append (format_exp('Section3_zShift', 'number', 0, 'MilliMeter'))
##--------------------------------------------------------------------------------
##  Fifth Cross-section
expressions_list.append (format_exp('Section4_A', 'number', 10, ''))
expressions_list.append (format_exp('Section4_B', 'number', 10, ''))
expressions_list.append (format_exp('Section4_C', 'number', 10, ''))
expressions_list.append (format_exp('Section4_xShift', 'number', 0, 'MilliMeter'))
expressions_list.append (format_exp('Section4_yShift', 'number', 0, 'MilliMeter'))
expressions_list.append (format_exp('Section4_zShift', 'number', 0, 'MilliMeter'))

# ellipse equation (x/A)^2 + (y/B)^2 = 1 upper surface
# ellipse equation (x/A)^2 + (y/C)^2 = 1 lower surface
# y = B * sqrt (1-(x/A)^2)

expressions_list101 = list ()

import matplotlib as mp

n = 50 # number of points
s = ['Section0','Section1', 'Section2', 'Section3','Section4']
angle0 = np.linspace(0, 2*pi, n*2)

Val0 = np.cos(angle0)
Val1 = np.sin(angle0)

# create the set of points for each cross-section
for section in s:
    count = 0
    for i in range (0,n):
        Y = section + '_yShift + Fuselage_yShift +' + str (Val0[i]) + '*' + section + '_A'
        Z = section + '_zShift + Fuselage_zShift +' + str (Val1[i]) + '*' + section + '_B'
        X = section + '_L +'+ section + '_xShift + Fuselage_xShift'
        expressions_list.append (format_exp(section+'_pt'+str (count), 'pt','point('+X+','+Y+ ','+Z+')', 'MilliMeter'))
        expressions_list101.append (section+'_pt'+str (count))
        count = count + 1
    for i in range (n,2*n):
        Y = section + '_yShift + Fuselage_yShift +' + str (Val0[i]) + '*' + section + '_A'
        Z = section + '_zShift + Fuselage_zShift +' + str (Val1[i]) + '*' + section + '_C'
        X = section + '_L +'+ section + '_xShift + Fuselage_xShift'
        expressions_list.append (format_exp(section+'_pt'+str (count), 'pt','point('+X+','+Y+ ','+Z+')', 'MilliMeter'))
        expressions_list101.append (section+'_pt'+str (count))
        count = count + 1

write_exp_file (expressions_list, 'HyperionNX_Fuselage_Expression')
write_txt_file (expressions_list101, 'HyperionNX_Fuselage_Expression')
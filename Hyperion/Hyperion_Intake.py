from Expressions import format_exp, write_exp_file, write_txt_file
from math import *
import numpy as np
expressions_list = list ()
expressions_list101 = list ()

## Intake Control parameters
if True:
## Intake Control parameters
    expressions_list.append (format_exp('Sin_Intake_Inclination_Angle', 'number', 90, 'Degrees'))
    expressions_list.append (format_exp('Sin_Intake_Middle_Plane_Angle', 'number', 45, 'Degrees'))
    expressions_list.append (format_exp('Sin_Intake_EDF_Length', 'number', 80, 'MilliMeter'))
    expressions_list.append (format_exp('Sin_Intake_EDF_OD', 'number', 123, 'MilliMeter'))
    expressions_list.append (format_exp('Sin_Intake_EDF_ID', 'number', 121, 'MilliMeter'))
    expressions_list.append (format_exp('Sin_Intake_Thickness', 'number',2, 'MilliMeter'))
    expressions_list.append (format_exp('Sin_Intake_Height', 'number',40, 'MilliMeter'))
    expressions_list.append (format_exp('Sin_Intake_d1', 'number',100, 'MilliMeter')) # distance between 1st middle cross-section and front cross-section
    expressions_list.append (format_exp('Sin_Intake_d2', 'number',100, 'MilliMeter')) # distance between 2nd middle cross-section and 3rd middle cross-section
    expressions_list.append (format_exp('Sin_Intake_d3', 'number',100, 'MilliMeter')) # distance between EDF and 3rd middle cross-section
    expressions_list.append (format_exp('Sin_Intake_Length', 'number', 'Sin_Intake_d1 + Sin_Intake_d2', 'MilliMeter'))
    expressions_list.append (format_exp('Sin_Intake_Dia1', 'number', 10 , 'MilliMeter')) # front cross-section inner diameter
    expressions_list.append (format_exp('Sin_Intake_Dia2', 'number', 10 , 'MilliMeter')) # 1st middle cross-section inner diameter
    expressions_list.append (format_exp('Sin_Intake_Dia3', 'number', 10 , 'MilliMeter')) # 2nd middle cross-section inner diameter
    expressions_list.append (format_exp('Sin_Intake_xShift', 'number', 10, 'MilliMeter'))
    expressions_list.append (format_exp('Sin_Intake_yShift', 'number', 10, 'MilliMeter'))
    expressions_list.append (format_exp('Sin_Intake_zShift', 'number', 10, 'MilliMeter'))
n = 50 # even number
# so basically there are 6 cross-sections, two for the EDF, two for mid-section, and two for the front cross-section of the intake
# make a simple circle for each
angle0 = np.linspace(0, 2*pi, n)
Val0 = np.cos(angle0)
Val1 = np.sin(angle0)

##  Front Semi-Elliptical cross-section of Intake
#   Outer Line
angle1 = np.linspace(pi, 2*pi, n-1)
Val0_front = np.cos(angle1)
Val1_front = np.sin(angle1)
if True:
    for i in range (0,n-1):
        Y_part =  str  (Val0_front[i])
        Z_part =  str  (Val1_front[i])
        y = '-((' + Y_part + ')*(Sin_Intake_Dia1*0.5+Sin_Intake_Thickness)*cos (Sin_Intake_Inclination_Angle)-(Sin_Intake_Dia1*0.5+Sin_Intake_Thickness)*(' + Z_part + ')*sin (Sin_Intake_Inclination_Angle))'
        z =  '((' + Y_part + ')*(Sin_Intake_Dia1*0.5+Sin_Intake_Thickness)*sin (Sin_Intake_Inclination_Angle)+(Sin_Intake_Dia1*0.5+Sin_Intake_Thickness)*(' + Z_part + ')*cos (Sin_Intake_Inclination_Angle))'
        New_Val = format_exp ('Sin_Intake_Front0_pt'+ str (i),'pt', 'point(Sin_Intake_xShift,Sin_Intake_yShift +' +  z + ',' + y + '+Sin_Intake_Dia1*0.25+Sin_Intake_zShift)', 'MilliMeter')
        expressions_list.append (New_Val)
        expressions_list101.append ('Sin_Intake_Front0_pt'+ str (i))
    for i in [0]:
        Y_part =  str  (Val0_front[i])
        Z_part =  str  (Val1_front[i])
        y = '-((' + Y_part + ')*(Sin_Intake_Dia1*0.5+Sin_Intake_Thickness)*cos (Sin_Intake_Inclination_Angle)-(Sin_Intake_Dia1*0.5+Sin_Intake_Thickness)*(' + Z_part + ')*sin (Sin_Intake_Inclination_Angle))'
        z =  '((' + Y_part + ')*(Sin_Intake_Dia1*0.5+Sin_Intake_Thickness)*sin (Sin_Intake_Inclination_Angle)+(Sin_Intake_Dia1*0.5+Sin_Intake_Thickness)*(' + Z_part + ')*cos (Sin_Intake_Inclination_Angle))'
        New_Val = format_exp ('Sin_Intake_Front0_pt'+ str (n-1),'pt', 'point(Sin_Intake_xShift,Sin_Intake_yShift +' + z +',' + y + '+Sin_Intake_Dia1*0.25+Sin_Intake_zShift)', 'MilliMeter')
        expressions_list.append (New_Val)
        expressions_list101.append ('Sin_Intake_Front0_pt'+ str (n-1))

    ##  1st Middle cross-section of Intake
    #   Outer Line
    for i in range (0,n):
        Y_part =  str  (Val0[i])
        Z_part =  str (Val1[i])
        y = '(' + Y_part + ')*(Sin_Intake_Dia2*0.5+Sin_Intake_Thickness)*cos (Sin_Intake_Inclination_Angle)-(Sin_Intake_Dia2*0.5+Sin_Intake_Thickness)*(' + Z_part + ')*sin (Sin_Intake_Inclination_Angle)'
        z = '(' + Y_part + ')*(Sin_Intake_Dia2*0.5+Sin_Intake_Thickness)*sin (Sin_Intake_Inclination_Angle)+(Sin_Intake_Dia2*0.5+Sin_Intake_Thickness)*(' + Z_part + ')*cos (Sin_Intake_Inclination_Angle)'
        New_Val = format_exp ('Sin_Intake_mid00_pt'+ str (i),'pt', 'point(Sin_Intake_d1+Sin_Intake_xShift,Sin_Intake_yShift + ' + y + ' ,' + z + '+Sin_Intake_zShift)', 'MilliMeter')
        expressions_list.append (New_Val)
        expressions_list101.append ('Sin_Intake_mid00_pt'+ str (i))
    #   Inner Line
    for i in range (0,n):
        Y_part =  str  (Val0[i])
        Z_part =  str (Val1[i])
        y = '(' + Y_part + ')*(Sin_Intake_Dia2*0.5)*cos (Sin_Intake_Inclination_Angle)-(Sin_Intake_Dia2*0.5)*(' + Z_part + ')*sin (Sin_Intake_Inclination_Angle)'
        z = '(' + Y_part + ')*(Sin_Intake_Dia2*0.5)*sin (Sin_Intake_Inclination_Angle)+(Sin_Intake_Dia2*0.5)*(' + Z_part + ')*cos (Sin_Intake_Inclination_Angle)'
        New_Val = format_exp ('Sin_Intake_mid01_pt'+ str (i),'pt', 'point(Sin_Intake_d1+Sin_Intake_xShift,Sin_Intake_yShift +' + y + ',' + z + '+Sin_Intake_zShift)', 'MilliMeter')
        expressions_list.append (New_Val)
        expressions_list101.append ('Sin_Intake_mid01_pt'+ str (i))

    ##  2nd Middle cross-section of Intake
    #   Outer Line
    for i in range (0,n):
        Y_part =  str  (Val0[i])
        Z_part =  str (Val1[i])
        y =  '(' + Y_part + ')*(Sin_Intake_Dia3*0.5+Sin_Intake_Thickness)*cos (Sin_Intake_Inclination_Angle)-(Sin_Intake_Dia3*0.5+Sin_Intake_Thickness)*(' + Z_part + ')*sin (Sin_Intake_Inclination_Angle)'
        z =  '(' + Y_part + ')*(Sin_Intake_Dia3*0.5+Sin_Intake_Thickness)*sin (Sin_Intake_Inclination_Angle)+(Sin_Intake_Dia3*0.5+Sin_Intake_Thickness)*(' + Z_part + ')*cos (Sin_Intake_Inclination_Angle)'
        x = '-(' + z + ')*sin (Sin_Intake_Middle_Plane_Angle)'
        z = ' (' + z + ')*cos (Sin_Intake_Middle_Plane_Angle)'
        New_Val = format_exp ('Sin_Intake_Mid10_pt'+ str (i),'pt', 'point(Sin_Intake_d2+Sin_Intake_d1+Sin_Intake_xShift'+ x +',Sin_Intake_yShift +' + y + ',' + z + '+Sin_Intake_zShift+Sin_Intake_Height)', 'MilliMeter')
        expressions_list.append (New_Val)
        expressions_list101.append ('Sin_Intake_Mid10_pt'+ str (i))
    #   Inner Line
    for i in range (0,n):
        Y_part =  str  (Val0[i])
        Z_part =  str (Val1[i])
        y =  '(' + Y_part + ')*(Sin_Intake_Dia3*0.5)*cos (Sin_Intake_Inclination_Angle+Sin_Intake_Middle_Plane_Angle)-(Sin_Intake_Dia3*0.5)*(' + Z_part + ')*sin (Sin_Intake_Inclination_Angle+Sin_Intake_Middle_Plane_Angle)'
        z =  '(' + Y_part + ')*(Sin_Intake_Dia3*0.5)*sin (Sin_Intake_Inclination_Angle+Sin_Intake_Middle_Plane_Angle)+(Sin_Intake_Dia3*0.5)*(' + Z_part + ')*cos (Sin_Intake_Inclination_Angle+Sin_Intake_Middle_Plane_Angle)'
        x = '-(' + z + ')*sin (Sin_Intake_Middle_Plane_Angle)'
        z =  '(' + z + ')*cos (Sin_Intake_Middle_Plane_Angle)'
        New_Val = format_exp ('Sin_Intake_Mid11_pt'+ str (i),'pt', 'point(Sin_Intake_d2+Sin_Intake_d1+Sin_Intake_xShift'+ x +',Sin_Intake_yShift +' + y + ',' + z + '+Sin_Intake_zShift+Sin_Intake_Height)', 'MilliMeter')
        expressions_list.append (New_Val)
        expressions_list101.append ('Sin_Intake_Mid11_pt'+ str (i))

    ##  EDF
    #   EDF Outer Edge (cross-section plane)
    for i in range (0,n):
        Y_part =  str  (Val0[i])
        Z_part =  str (Val1[i])
        y = '(' + Y_part + ')*(Sin_Intake_EDF_OD*0.5)*cos (Sin_Intake_Inclination_Angle)-(Sin_Intake_EDF_OD*0.5)*(' + Z_part + ')*sin (Sin_Intake_Inclination_Angle)'
        z = '(' + Y_part + ')*(Sin_Intake_EDF_OD*0.5)*sin (Sin_Intake_Inclination_Angle)+(Sin_Intake_EDF_OD*0.5)*(' + Z_part + ')*cos (Sin_Intake_Inclination_Angle)'
        New_Val = format_exp ('Sin_Intake_EDF_OD0_pt'+ str (i),'pt', 'point(Sin_Intake_d3+Sin_Intake_d2+Sin_Intake_d1+Sin_Intake_xShift,Sin_Intake_yShift +' + y + ',' + z + '+Sin_Intake_zShift+2*Sin_Intake_Height)', 'MilliMeter')
        expressions_list.append (New_Val)
        expressions_list101.append ('Sin_Intake_EDF_OD0_pt'+ str (i))
    #   EDF Inner Edge (cross-section plane)
    for i in range (0,n):
        Y_part =  str  (Val0[i])
        Z_part =  str (Val1[i])
        y = '(' + Y_part + ')*(Sin_Intake_EDF_ID*0.5)*cos (Sin_Intake_Inclination_Angle)-(Sin_Intake_EDF_ID*0.5)*(' + Z_part + ')*sin (Sin_Intake_Inclination_Angle)'
        z = '(' + Y_part + ')*(Sin_Intake_EDF_ID*0.5)*sin (Sin_Intake_Inclination_Angle)+(Sin_Intake_EDF_ID*0.5)*(' + Z_part + ')*cos (Sin_Intake_Inclination_Angle)'
        New_Val = format_exp ('Sin_Intake_EDF_ID0_pt'+ str (i),'pt', 'point(Sin_Intake_d3+Sin_Intake_d2+Sin_Intake_d1+Sin_Intake_xShift,Sin_Intake_yShift +' + y +',' + z + '+Sin_Intake_zShift+2*Sin_Intake_Height)', 'MilliMeter')
        expressions_list.append (New_Val)
        expressions_list101.append ('Sin_Intake_EDF_ID0_pt'+ str (i))
    #   EDF Outer Edge (cross-section plane)
    for i in range (0,n):
        Y_part =  str  (Val0[i])
        Z_part =  str (Val1[i])
        y = '(' + Y_part + ')*(Sin_Intake_EDF_OD*0.5)*cos (Sin_Intake_Inclination_Angle)-(Sin_Intake_EDF_OD*0.5)*(' + Z_part + ')*sin (Sin_Intake_Inclination_Angle)'
        z = '(' + Y_part + ')*(Sin_Intake_EDF_OD*0.5)*sin (Sin_Intake_Inclination_Angle)+(Sin_Intake_EDF_OD*0.5)*(' + Z_part + ')*cos (Sin_Intake_Inclination_Angle)'
        New_Val = format_exp ('Sin_Intake_EDF_OD1_pt'+ str (i),'pt', 'point(Sin_Intake_EDF_Length+Sin_Intake_d3+Sin_Intake_d2+Sin_Intake_d1+Sin_Intake_xShift,Sin_Intake_yShift+' + y + ',' + z + '+Sin_Intake_zShift+2*Sin_Intake_Height)', 'MilliMeter')
        expressions_list.append (New_Val)
        expressions_list101.append ('Sin_Intake_EDF_OD1_pt'+ str (i))
    #   EDF Inner Edge (cross-section plane)
    for i in range (0,n):
        Y_part =  str (Val0[i])
        Z_part =  str (Val1[i])
        y = '(' + Y_part + ')*(Sin_Intake_EDF_ID*0.5)*cos (Sin_Intake_Inclination_Angle)-(Sin_Intake_EDF_ID*0.5)*(' + Z_part + ')*sin (Sin_Intake_Inclination_Angle)'
        z = '(' + Y_part + ')*(Sin_Intake_EDF_ID*0.5)*sin (Sin_Intake_Inclination_Angle)+(Sin_Intake_EDF_ID*0.5)*(' + Z_part + ')*cos (Sin_Intake_Inclination_Angle)'
        New_Val = format_exp ('Sin_Intake_EDF_ID1_pt'+ str (i),'pt', 'point(Sin_Intake_EDF_Length+Sin_Intake_d3+Sin_Intake_d2+Sin_Intake_d1+Sin_Intake_xShift, Sin_Intake_yShift +' + y + ',' + z + '+Sin_Intake_zShift+2*Sin_Intake_Height)', 'MilliMeter')
        expressions_list.append (New_Val)
        expressions_list101.append ('Sin_Intake_EDF_ID1_pt'+ str (i))
# Add the Guide Lines
# Straight line from front to 1st middle (Sin_Intake_xShift to Sin_Intake_d1+Sin_Intake_xShift)
if True:
    xValues = np.linspace(0, 1, n)
    for i in range (0,n):
        X_part =  str  (xValues[i])
        Z_part =  str (0)
        New_Val = format_exp ('Sin_Intake_line0_pt'+ str (i),'pt', 'point(Sin_Intake_xShift + Sin_Intake_d1 * ' + X_part + ',Sin_Intake_yShift,' + Z_part + '+Sin_Intake_zShift)', 'MilliMeter')
        expressions_list.append (New_Val)
        expressions_list101.append ('Sin_Intake_line0_pt'+ str (i))

    # Sinusoidal line from 1st middle to 3rd middle (Sin_Intake_d1+Sin_Intake_xShift to Sin_Intake_d3+Sin_Intake_d2+Sin_Intake_d1+Sin_Intake_xShift)
    xValues = np.linspace(0, 1, n)
    zValues = np.linspace(0, pi, n)
    for i in range (0,n):
        X_part =  str  (xValues[i])
        Z_part =  'Sin_Intake_Height*' + str ((sin (zValues[i]-pi/2)+1))
        New_Val = format_exp ('Sin_Intake_line1_pt'+ str (i),'pt', 'point(Sin_Intake_xShift + Sin_Intake_d1 + (Sin_Intake_d2+Sin_Intake_d3) * ' + X_part + ',Sin_Intake_yShift,' + Z_part + '+Sin_Intake_zShift)', 'MilliMeter')
        expressions_list.append (New_Val)
        expressions_list101.append ('Sin_Intake_line1_pt'+ str (i))
write_exp_file (expressions_list, 'HyperionNX_Intake')
write_txt_file (expressions_list101, 'HyperionNX_Intake')
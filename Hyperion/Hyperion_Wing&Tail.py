# It is a forwardSwept Angeled wing with 3 cross-sections
# We need 3 cross-sections to form the wing ==> 3 .exp files
# We need 2 cross-sections to form the Hstabs  ==> 2 .exp files
# We need 2 cross-sections to form the Vstabs  ==> 3 .exp files
''''
Wing: 0 - S8037, 1 - S8037, 2 - SD8040 (inboard to outboard)
Vstab: 0 - NACA 0008, 1 - NACA 0010, 2 - NACA 0010 (bottom to top)
Hstab: All NACA 0012
'''

from Airfoil import Airfoil_XY, Airfoil_XZ
#def Airfoil (Part_Name,Airfoil_Name, filename .dat, Unit):
##--------------------------------------------------------
## Wing
Airfoil_XZ ('Wing', 'Airfoil_w0', 'S8037 (16%).dat', 'MilliMeter')
Airfoil_XZ ('Wing', 'Airfoil_w1', 'S8037 (16%).dat', 'MilliMeter')
Airfoil_XZ ('Wing', 'Airfoil_w2', 'sd8040 (10%).dat', 'MilliMeter')
##--------------------------------------------------------
## Tail
## Hstab
Airfoil_XZ ('Hstab', 'Airfoil_h0', 'NACA 0012.dat', 'MilliMeter')
Airfoil_XZ ('Hstab', 'Airfoil_h1', 'NACA 0012.dat', 'MilliMeter')
## Vstab
Airfoil_XY ('Vstab', 'Airfoil_v0', 'NACA0008.dat', 'MilliMeter')
Airfoil_XY ('Vstab', 'Airfoil_v1', 'NACA0010.dat', 'MilliMeter')
Airfoil_XY ('Vstab', 'Airfoil_v2', 'NACA0010.dat', 'MilliMeter')

# Now, run Hyperion_Wing&Tail.py
# Spacing between Airfoils

### Specific Part Shifts

## Wings ==> Wing_half_span = Wing_B_1 + Wing_B_2
    # Wing_Lambda_1 = 0
    # Wing_Lambda_2 = 0
    # Wing_Lambda_3 = -10
    # Wing_Lambda_4 = -10
    # Wing_B_1 = 275
    # Wing_B_2 = 400
    # Wing_L = 400
    # Wing_Chord_1 = Wing_L
    # Wing_Chord_2 = Wing_L+Wing_B_1*(tan(Wing_Lambda_3)-tan(Wing_Lambda_1))
    # Wing_Chord_3 = Wing_L+Wing_B_1*(tan(Wing_Lambda_3)-tan(Wing_Lambda_1))+Wing_b_2*(tan(Wing_Lambda_4)-tan(Wing_Lambda_2))

    # Airfoil_w0_xShift = 0
    # Airfoil_w1_xShift = Wing_B_1*tan(Wing_Lambda_1)
    # Airfoil_w2_xShift = Wing_B_1*tan(Wing_Lambda_1) + Wing_B_2*tan(Wing_Lambda_2)
    # Airfoil_w0_yShift = 0
    # Airfoil_w1_yShift = Wing_B_1
    # Airfoil_w2_yShift = Wing_B_1 + Wing_B_2
    # Airfoil_w0_zShift = 0
    # Airfoil_w1_zShift = 0
    # Airfoil_w2_zShift = 0

## Hstab ==> Hstab_half_span = Hstab_B_1
    # Hstab_Lambda_1 = 0
    # Hstab_Lambda_2 = 0
    # Hstab_L = 0
    # Hstab_Chord_1 = Hstab_L
    # Hstab_Chord_2 = Hstab_L+Hstab_B_1*(tan(Hstab_Lambda_3)-tan(Hstab_Lambda_1))

    # Airfoil_h0_xShift = 0
    # Airfoil_h1_xShift = Hstab_B_1*tan(Hstab_Lambda_1)
    # Airfoil_h0_yShift = 0
    # Airfoil_h1_yShift = Hstab_B_1
    # Airfoil_h0_zShift = 0
    # Airfoil_h1_zShift = 0

## Vstabs ==> Vstab_half_span = Vstab_B_1 + Vstab_B_2

    # Vstab_Lambda_1 = 75
    # Vstab_Lambda_2 = 55
    # Vstab_Lambda_3 = 20
    # Vstab_Lambda_4 = Vstab_Lambda_3
    # Vstab_B_1 = 150
    # Vstab_B_2 = 300
    # Vstab_L = 1100
    # Vstab_Chord_1 = Vstab_L
    # Vstab_Chord_2 = Vstab_L+Vstab_B_1*(tan(Vstab_Lambda_3)-tan(Vstab_Lambda_1))
    # Vstab_Chord_3 = Vstab_L+Vstab_B_1*(tan(Vstab_Lambda_3)-tan(Vstab_Lambda_1))+VStab_b_2*(tan(Vstab_Lambda_4)-tan(Vstab_Lambda_2))

    # Airfoil_v0_xShift = 0
    # Airfoil_v1_xShift = Vstab_B_1*tan(Vstab_Lambda_1)
    # Airfoil_v2_xShift = Vstab_B_1*tan(Vstab_Lambda_1)+Vstab_B_2*tan(Vstab_Lambda_2)
    # Airfoil_v0_yShift = 0
    # Airfoil_v1_yShift = Vstab_B_1
    # Airfoil_v2_yShift = Vstab_B_1 + Vstab_B_2
    # Airfoil_v0_zShift = 0
    # Airfoil_v1_zShift = 0
    # Airfoil_v2_zShift = 0
##   Writing Expressions

from Expressions import format_exp, write_exp_file
expressions_list = list ()

## Degrees
expressions_list.append (format_exp('Wing_Lambda_1', 'number', 0, 'Degrees'))
expressions_list.append (format_exp('Wing_Lambda_2', 'number', 0, 'Degrees'))
expressions_list.append (format_exp('Wing_Lambda_3', 'number', -10, 'Degrees'))
expressions_list.append (format_exp('Wing_Lambda_4', 'number', -10, 'Degrees'))

expressions_list.append (format_exp('Hstab_Lambda_1', 'number', 0, 'Degrees'))
expressions_list.append (format_exp('Hstab_Lambda_2', 'number', 0, 'Degrees'))

expressions_list.append (format_exp('Vstab_Lambda_1', 'number', 75, 'Degrees'))
expressions_list.append (format_exp('Vstab_Lambda_2', 'number', 50, 'Degrees'))
expressions_list.append (format_exp('Vstab_Lambda_3', 'number', 20, 'Degrees'))
expressions_list.append (format_exp('Vstab_Lambda_4', 'number', 20, 'Degrees'))

## Wing (Airfoil_XZ)
expressions_list.append (format_exp('Wing_B_1', 'number', 275, 'MilliMeter'))
expressions_list.append (format_exp('Wing_B_2', 'number', 400, 'MilliMeter'))
expressions_list.append (format_exp('Wing_L', 'number', 400, 'MilliMeter'))
expressions_list.append (format_exp('Airfoil_w0_Chord', 'number', 'Wing_L', 'MilliMeter'))
expressions_list.append (format_exp('Airfoil_w1_Chord', 'number', 'Wing_L+Wing_B_1*(tan(Wing_Lambda_3)-tan(Wing_Lambda_1))', 'MilliMeter'))
expressions_list.append (format_exp('Airfoil_w2_Chord', 'number', 'Wing_L+Wing_B_1*(tan(Wing_Lambda_3)-tan(Wing_Lambda_1))+Wing_b_2*(tan(Wing_Lambda_4)-tan(Wing_Lambda_2))', 'MilliMeter'))

expressions_list.append (format_exp('Airfoil_w0_xShift', 'number', 0, 'MilliMeter'))
expressions_list.append (format_exp('Airfoil_w1_xShift', 'number', 'Wing_B_1*tan(Wing_Lambda_1)', 'MilliMeter'))
expressions_list.append (format_exp('Airfoil_w2_xShift', 'number', 'Wing_B_1*tan(Wing_Lambda_1) + Wing_B_2*tan(Wing_Lambda_2)', 'MilliMeter'))
expressions_list.append (format_exp('Airfoil_w0_yShift', 'number', 0, 'MilliMeter'))
expressions_list.append (format_exp('Airfoil_w1_yShift', 'number', 'Wing_B_1', 'MilliMeter'))
expressions_list.append (format_exp('Airfoil_w2_yShift', 'number', 'Wing_B_1 + Wing_B_2', 'MilliMeter'))
expressions_list.append (format_exp('Airfoil_w0_zShift', 'number', 0, 'MilliMeter'))
expressions_list.append (format_exp('Airfoil_w1_zShift', 'number', 0, 'MilliMeter'))
expressions_list.append (format_exp('Airfoil_w2_zShift', 'number', 0, 'MilliMeter'))

## Hstab (Airfoil_XZ)
expressions_list.append (format_exp('Hstab_B_1', 'number', 275, 'MilliMeter'))
expressions_list.append (format_exp('Hstab_L', 'number', 400, 'MilliMeter'))
expressions_list.append (format_exp('Airfoil_h0_Chord', 'number', 'Hstab_L', 'MilliMeter'))
expressions_list.append (format_exp('Airfoil_h1_Chord', 'number', 'Hstab_L+Hstab_B_1*(tan(Hstab_Lambda_2)-tan(Hstab_Lambda_1))', 'MilliMeter'))

expressions_list.append (format_exp('Airfoil_h0_xShift', 'number', 0, 'MilliMeter'))
expressions_list.append (format_exp('Airfoil_h1_xShift', 'number', 'Hstab_B_1*tan(Hstab_Lambda_1)', 'MilliMeter'))
expressions_list.append (format_exp('Airfoil_h0_yShift', 'number', 0, 'MilliMeter'))
expressions_list.append (format_exp('Airfoil_h1_yShift', 'number', 'Hstab_B_1', 'MilliMeter'))
expressions_list.append (format_exp('Airfoil_h0_zShift', 'number', 0, 'MilliMeter'))
expressions_list.append (format_exp('Airfoil_h1_zShift', 'number', 0, 'MilliMeter'))

## Vstab (Airfoil_XY)
expressions_list.append (format_exp('Vstab_B_1', 'number', 150, 'MilliMeter'))
expressions_list.append (format_exp('Vstab_B_2', 'number', 300, 'MilliMeter'))
expressions_list.append (format_exp('Vstab_L', 'number', 1100, 'MilliMeter'))
expressions_list.append (format_exp('Airfoil_v2_Chord', 'number', 'Vstab_L', 'MilliMeter'))
expressions_list.append (format_exp('Airfoil_v1_Chord', 'number', 'Vstab_L+Vstab_B_1*(tan(Vstab_Lambda_3)-tan(Vstab_Lambda_1))', 'MilliMeter'))
expressions_list.append (format_exp('Airfoil_v0_Chord', 'number', 'Vstab_L+Vstab_B_1*(tan(Vstab_Lambda_3)-tan(Vstab_Lambda_1))+Vstab_b_2*(tan(Vstab_Lambda_4)-tan(Vstab_Lambda_2))', 'MilliMeter'))

expressions_list.append (format_exp('Airfoil_v2_xShift', 'number', 0, 'MilliMeter'))
expressions_list.append (format_exp('Airfoil_v1_xShift', 'number', 'Vstab_B_1*tan(Vstab_Lambda_1)', 'MilliMeter'))
expressions_list.append (format_exp('Airfoil_v0_xShift', 'number', 'Vstab_B_1*tan(Vstab_Lambda_1) + Vstab_B_2*tan(Vstab_Lambda_2)', 'MilliMeter'))
expressions_list.append (format_exp('Airfoil_v2_zShift', 'number', 0, 'MilliMeter'))
expressions_list.append (format_exp('Airfoil_v1_zShift', 'number', 'Vstab_B_1', 'MilliMeter'))
expressions_list.append (format_exp('Airfoil_v0_zShift', 'number', 'Vstab_B_1 + Vstab_B_2', 'MilliMeter'))
expressions_list.append (format_exp('Airfoil_v2_yShift', 'number', 0, 'MilliMeter'))
expressions_list.append (format_exp('Airfoil_v1_yShift', 'number', 0, 'MilliMeter'))
expressions_list.append (format_exp('Airfoil_v0_yShift', 'number', 0, 'MilliMeter'))

write_exp_file (expressions_list, 'HyperionNX_Major_Expression')

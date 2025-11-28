def Airfoil_XY (Part_Name,Airfoil_Name,filename, Unit):
# Airfoil_Name (Airfoil0, Aifoil_NACAxxx, etc)
# Part_Name (Wing_xxx,Vstabxxx, etc)
# filename ('NACA008.dat', etc)
# unit (Unitless, Degrees, MilliMeter, Inch, Feet, etc)
  
    from read_dat import Read_Dat
    val = Read_Dat (filename)
    x = val
    y = val
    z = val

    #convert that into an exp. file (type = point)
    from Expressions import format_exp, write_exp_file, write_txt_file

    #create a list of strings for the expressiosn
    expressions_list = list ()
    expressions_list101 = list ()

    #   Part Shift (Universal)
    PxShift = Part_Name +'_xShift'
    PyShift = Part_Name +'_yShift'
    PzShift = Part_Name +'_zShift'

    # change the 3 lines to comments outside testing
    expressions_list.append (format_exp(PxShift, 'number', 0, Unit))
    expressions_list.append (format_exp(PyShift, 'number', 0, Unit))
    expressions_list.append (format_exp(PzShift, 'number', 0, Unit))

    #   Airfoil Shift
    AxShift = '+'+Airfoil_Name+'_xShift' + '+'
    AyShift = '+'+Airfoil_Name+'_yShift' + '+'
    AzShift = '+'+Airfoil_Name+'_zShift' + '+'
    expressions_list.append (format_exp(AxShift[1:-1:1], 'number', 0, Unit))
    expressions_list.append (format_exp(AyShift[1:-1:1], 'number', 0, Unit))
    expressions_list.append (format_exp(AzShift[1:-1:1], 'number', 0, Unit))

    XShift = PxShift + AxShift
    YShift = PyShift + AyShift
    ZShift = PzShift + AzShift
    for i in range (0, len(x)):
        New_Val = format_exp (Airfoil_Name + '_pt'+ str (i),'pt', 'point(' + XShift + Airfoil_Name + '_Chord' + '*' + str (x[i][0]) + ',' + YShift + Airfoil_Name + '_Chord' + '*' + str (y[i][1]) + ',' + ZShift  + Airfoil_Name + '_Chord'  + '*' + str (z[i][2]) + ')', Unit)
        expressions_list.append (New_Val)
        expressions_list101.append (Airfoil_Name + '_pt'+ str (i))

    write_exp_file (expressions_list, Part_Name + '_' + Airfoil_Name)
    write_txt_file (expressions_list101, Part_Name + '_' + Airfoil_Name)

def Airfoil_XZ (Part_Name,Airfoil_Name,filename, Unit):
#Airfoil_Name (Airfoil0, Aifoil_NACAxxx, etc)
#Part_Name (Wing_xxx,Vstabxxx, etc)
#filename ('NACA008.dat', etc)
#unit (Unitless, Degrees, MilliMeter, Inch, Feet, etc)
  
    from read_dat import Read_Dat
    val = Read_Dat (filename)
    x = val
    y = val
    z = val

    #convert that into an exp. file (type = point)
    from Expressions import format_exp, write_exp_file, write_txt_file

    #create a list of strings for the expressiosn
    expressions_list = list ()
    expressions_list101 = list ()

    #   Part Shift (Universal)
    PxShift = Part_Name +'_xShift'
    PyShift = Part_Name +'_yShift'
    PzShift = Part_Name +'_zShift'

    # change the 3 lines to comments outside testing
    expressions_list.append (format_exp(PxShift, 'number', 0, Unit))
    expressions_list.append (format_exp(PyShift, 'number', 0, Unit))
    expressions_list.append (format_exp(PzShift, 'number', 0, Unit))

    #   Airfoil Shift
    AxShift = '+'+Airfoil_Name+'_xShift' + '+'
    AyShift = '+'+Airfoil_Name+'_yShift' + '+'
    AzShift = '+'+Airfoil_Name+'_zShift' + '+'
    expressions_list.append (format_exp(AxShift[1:-1:1], 'number', 0, Unit))
    expressions_list.append (format_exp(AyShift[1:-1:1], 'number', 0, Unit))
    expressions_list.append (format_exp(AzShift[1:-1:1], 'number', 0, Unit))

    XShift = PxShift + AxShift
    YShift = PyShift + AyShift
    ZShift = PzShift + AzShift
    for i in range (0, len(x)):
        New_Val = format_exp (Airfoil_Name + '_pt'+ str (i),'pt', 'point(' + XShift + Airfoil_Name + '_Chord' + '*' + str (x[i][0]) + ',' + YShift + Airfoil_Name + '_Chord' + '*' + str (y[i][2]) + ',' + ZShift  + Airfoil_Name + '_Chord'  + '*' + str (z[i][1]) + ')', Unit)
        expressions_list.append (New_Val)
        expressions_list101.append (Airfoil_Name + '_pt'+ str (i))

    write_exp_file (expressions_list, Part_Name + '_' + Airfoil_Name)
    write_txt_file (expressions_list101, Part_Name + '_' + Airfoil_Name)

def Airfoil_YZ (Part_Name,Airfoil_Name,filename, Unit):
#Airfoil_Name (Airfoil0, Aifoil_NACAxxx, etc)
#Part_Name (Wing_xxx,Vstabxxx, etc)
#filename ('NACA008.dat', etc)
#unit (Unitless, Degrees, MilliMeter, Inch, Feet, etc)
  
    from read_dat import Read_Dat
    val = Read_Dat (filename)
    x = val
    y = val
    z = val

    #convert that into an exp. file (type = point)
    from Expressions import format_exp, write_exp_file, write_txt_file

    #create a list of strings for the expressiosn
    expressions_list = list ()
    expressions_list101 = list ()

    #   Part Shift (Universal)
    PxShift = Part_Name +'_xShift'
    PyShift = Part_Name +'_yShift'
    PzShift = Part_Name +'_zShift'

    # change the 3 lines to comments outside testing
    expressions_list.append (format_exp(PxShift, 'number', 0, Unit))
    expressions_list.append (format_exp(PyShift, 'number', 0, Unit))
    expressions_list.append (format_exp(PzShift, 'number', 0, Unit))

    #   Airfoil Shift
    AxShift = '+'+Airfoil_Name+'_xShift' + '+'
    AyShift = '+'+Airfoil_Name+'_yShift' + '+'
    AzShift = '+'+Airfoil_Name+'_zShift' + '+'
    expressions_list.append (format_exp(AxShift[1:-1:1], 'number', 0, Unit))
    expressions_list.append (format_exp(AyShift[1:-1:1], 'number', 0, Unit))
    expressions_list.append (format_exp(AzShift[1:-1:1], 'number', 0, Unit))

    XShift = PxShift + AxShift
    YShift = PyShift + AyShift
    ZShift = PzShift + AzShift
    for i in range (0, len(x)):
        New_Val = format_exp (Airfoil_Name + '_pt'+ str (i),'pt', 'point(' + XShift + Airfoil_Name + '_Chord' + '*' + str (x[i][2]) + ',' + YShift + Airfoil_Name + '_Chord' + '*' + str (y[i][0]) + ',' + ZShift  + Airfoil_Name + '_Chord'  + '*' + str (z[i][1]) + ')', Unit)
        expressions_list.append (New_Val)
        expressions_list101.append (Airfoil_Name + '_pt'+ str (i))

    write_exp_file (expressions_list, Part_Name + '_' + Airfoil_Name)
    write_txt_file (expressions_list101, Part_Name + '_' + Airfoil_Name)

#test case
#Airfoil_XZ ('WingNuts', 'n64212', 'n64212.dat', 'Inch')

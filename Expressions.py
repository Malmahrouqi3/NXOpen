#Expressions.py

def format_exp (Name, t ='number',val=0, u=''): #name, type (number, str, bool, int, point, vector, list), formula or value (sin(b*10), 10), unit (Unitless, Degrees, MilliMeter, Inch, Feet, etc)
#For Vectors and Point, val should be a list 

#type of input
  if t == 'number' or t == 'int':   #Number or Intgar Expression
    Type = ''
    if u == '':
       Unit = ''
    else:
      Unit = ('['+u+']')
  
  elif t == 'str':     #String Expression
      Type = '(String) '
  
  elif t == 'bool':    #Boolen Expression
      Type = '(Boolen) '

  elif t == 'pt':      #Point Expression
    Type = '(Point) '
    val = str (val)
    Formula = 'point(' + val [1:-2:1] + ')'
    if u == '':
      Unit = ''
    else:
      Unit = ('['+u+']')

  elif t == 'vt':      #Vector Expression
    Type = '(Vector) '
    val = str (val)
    Formula = 'vector('+val [1:-2:1]+')'
    if u == '':
      Unit = ''
    else:
       Unit = ('['+u+']')

  elif t == 'lt':      #List Expression
    Type = '(List) '
    val = str (val)
    Formula = ('{'+val [1:-2:1]+'}')
    if u == '':
      Unit = ''
    else:
      Unit = ('['+u+']')

  #if the expression is equal to a number/point/vector/list convert to a string
  if type (val) != "str":
    Formula = str (val)
    
  return (Type+Unit+Name+'='+Formula)

#General Format of expressions
#// Version:  3
#[unit]name=formula       if unitless, omit [unit]. if boolen or string, use (boolen)/(string) followed by a space
#e.g.
#[MilliMeter]Airfoil_Horiz_Shift = Wing_Airfoil0_x

#write an exp file
def write_exp_file (IN, file_name): #input should be a list of formatted String expressions
  with open(file_name+".exp", "w") as f:
    f.write("// Version:  3" + "\n")
    for item in IN:
      f.write(item + "\n")

def write_txt_file (IN, file_name): #input should be a list of formatted String expressions
  with open(file_name+".txt", "w") as f:
    for item in IN:
      f.write(item + "\n")

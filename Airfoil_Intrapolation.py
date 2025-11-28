## Given cst weight lists for the tip and root airfoils
## Convert that to additional airfoils while averaging the y-values

def airfoil_intra (r1,r2,t1,t2,n,name)
import numpy as np

# n is the number of all airfoils including root and tip (e.g. 200 intermediate airfoils + root and tip)
# name is the first segment of each .dat filename
# root airfoil weights (upper then lower surfaces)
r = cst_para(r1,r2)
# tip airfoil weights (upper then lower surfaces)
t = cst_para(t1,t2)
a = r # set of coordinates

i = np.linspace(0, n, n, endpoint = True)
for i in range (0,n):
 a[1] = t*i/n + r[]*(end-i)/n


# write all airfoils
def write_airfoil (IN, filename): #input should be a list of formatted String expressions
  with open(file_name+".dat", "w") as f:
    f.write(file_name + "\n")
    for item in IN:
      f.write(item + "\n")

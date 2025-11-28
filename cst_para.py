#cst_para.py
#intended to define x-y points
#may need to double check to extract the z values
#------------
# Sample Weight Inputs
# w = [0.9, 0.2728,  -0.2292 ]
# w = [0.206, 0.9, 0.2292]
# w = [0.206, 0.2728, 0.2292]
#------------
def cst(w1,w2,n1):
  def Class_func (x, N1, N2): #coor, intitial val, N1, N2
      for i in range (0,len(x)):
          a = x[i]**N1
          b = (1-x[i])**N2
          x[i] = a*b
      return x
  #-----------------------
  #shape function
  def Shape_func (x, w, L): #coord, weights, No. of weights
      k = x
      for i in range (0,L):
          k [i] = Factor(n)/(Factor(i-1)*(Factor((n)-(i-1))))
      S = x
      for i in range (0,L):
          S[i] = 0
          for j in range (0,L):
              S[i] = S[i] + (w[j]*k[j]*x[i]**(j))*((1-x[i])**(n-(j)))
      return S
  #-----------------------
  ##shape function for the Y Coordinates
  ##def Shape_funcY (x, w1, w2, L): #coord, weights, No. of weights
  ##    k = x
  ##    for i in range (0,L):
  ##        k [i] = Factor(n)/(Factor(i-1)*(Factor((n)-(i-1))))
  ##
  ##    for i in range (0,L):
  ##        b = 0
  ##        for j in range (0,len(w1)):
  ##            for a in range (0,len(w2)):
  ##                b = b + (w1[j]*w2[a]*k[j]*x[i]**(j))*((1-x[i])**(n-(j)))
  ##        S[i] = b
  ##        print (b)
  ##    return S
  #-----------------------
  #factorial
  def Factor(n):
      val=1
      while n>=1:
          val = val * n
          n = n-1
      return  val
  #-----------------------
  from math import *
  import json
  import numpy as np

  # Defining Function
  L = 1000 # Length of the Body Overall
  n = n1/2 # Number of Datapoints
  X_coor = np.linspace (0,1,n)
  # Half Cosine Spacing
  for i in range (0,n):
      X_coor[i]= pi/n*(i);
      X_coor[i] = 0.5*(cos(X_coor[i])+1);
  #-----------------------
  #y_coord
  #Sectional Factors
  N1 = 0.5
  N2 = 1
  #Vertical Factors
  M1 = 0.5
  M2 = 0.5
  C_1 = Class_func(np.linspace (0,1,n), N1, N2)
  C_2 = Class_func(np.linspace (0,1,n), M1, M2)
  S_1 = Shape_func(np.linspace (0,1,n), w, len(w))
  Y_coor = np.linspace (0,1,n)
  for i in range (0,len(X_coor)):
      Y_coor[i] = C_1[i]*C_2[i]*S_1[i]
  ##-----------------------
  ##z coord
  ##T1 = 0.5
  ##T2 = 0.5
  ##Z_coor = np.linspace (0,1,n)
  ##C = Class_func(Z_coor, T1, T2)
  ##S = Shape_func(Z_coor, w, len(w))
  ##for i in range (0,len(X_coor)):
  ##    Z_coor[i] = C_1[i]*C_2[i]*S[i]

  return (X_coor, Y_coor)

if __name__ == '__main__':
    Read_Dat()

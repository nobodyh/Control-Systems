import numpy as np
import sympy as sp
import control
from sympy import *
x, y, z,s,k = symbols('x y z s k')
init_printing(use_latex=True)


    
s=control.TransferFunction.s

G= (s+1)/((s+2)*((s+4)))

(num,denum)=control.tfdata(G)
print(num)
print(denum)
x=np.extract((np.mod(denum,1)==0),denum)
p=np.poly1d(list(x))
print(p)


r=np.roots(p)
print(r)
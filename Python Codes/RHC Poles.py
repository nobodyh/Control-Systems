import numpy as np
import sympy as sp
import control

s=control.TransferFunction.s

G= (1)/((s+2)*(s+4))

print(G)

(num,denum)=control.tfdata(G)

x=np.extract((np.mod(denum,1)==0),denum)
p=np.poly1d(list(x))
r=np.roots(p)

"""s=np.poly1d([1,12,58,144,393,1332,2236,1200,0])#Enter the coefficients in the order of the highest power
print(s,"\n")
r=np.roots(s)"""

for i in range(len(r)):
    print("\n",(np.around(r[i],2)))
r=np.around(r,2)
   
def poles(r):
    A=np.zeros(len(r))
    B=np.zeros(len(r))
    for i in range(0,len(r),1):
        A[i]=np.real(r[i])
        B[i]=np.imag(r[i])
    RHP=0
    LHP=0
    JW=0
    for i in range(0,len(r),1):
        if(A[i]>0):
            RHP+=1
        elif(A[i]<0):
            LHP+=1
        elif(A[i]==0):
            JW+=1
    print("\nLHP:",LHP,"RHP:",RHP,"jw:",JW)

poles(r) 
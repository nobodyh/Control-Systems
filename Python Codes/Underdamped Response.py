import quantiphy as q
import numpy as np

case=1
if(case==1):

    x=np.poly1d([1,15,100])
    print(x[2],x[1],x[0])

    b=x[0]
    wn=np.sqrt(b)
    a=x[1]
    z=np.divide(a,np.multiply(2,wn))
    print("z: ",z,"wn: ",wn)
    Tp=np.divide(np.pi,np.multiply(wn,np.sqrt(np.subtract(1,np.power(z,2)))))

    Ts=np.divide(4,np.multiply(z,wn))

    OS=np.multiply(100,np.divide(1,np.exp(np.divide(np.multiply(z,np.pi),np.sqrt(np.subtract(1,np.power(z,2)))))))

    Tr=1.76 * (z**3) - 0.417*(z**2) + 1.039*z +1

    print("Tp:",Tp,"s","Ts:",Ts,"s","O.S(%):",OS,"%","Tr:",Tr,"s")

elif(case==2):
    a=2
    b=1
    z=np.cos(np.arctan(np.divide(b,a)))
    wn=np.sqrt(np.add(np.power(a,2),np.power(a,2)))
    
    Tp=np.divide(np.pi,b)
    OS=np.multiply(100,np.divide(1,np.exp(np.divide(np.multiply(z,np.pi),np.sqrt(np.subtract(1,np.power(z,2)))))))
    Ts=np.divide(4,a)
    Tr=1.76 * (z**3) - 0.417*(z**2) + 1.039*z +1
    
    print("Tp:",Tp,"s","Ts:",Ts,"s","O.S(%):",OS,"%","Tr:",Tr,"s")



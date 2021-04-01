import numpy as np

def location(a,b):
    print("Location of Poles: ",np.round(-a,2),"+- j(",np.round(b,2),")")

def f1(Ts,Tp):
    a=float(np.divide(4,Ts))
    b=float(np.divide(np.pi,Tp))
    location(a,b)

def f2(OS,Ts):
    a=float(np.divide(4,Ts))
    e=float(np.divide(-np.log(OS/100),np.sqrt(np.add(np.power(np.pi,2),np.power(np.log(OS/100),2)))))
    
    wn=float(np.divide(a,e))
    b=float(np.multiply(wn,np.sqrt(np.subtract(1,np.power(e,2)))))
    location(a, b)

def f3(OS,Tp):
    b=np.divide(np.pi,Tp)
    e=float(np.divide(-np.log(OS/100),np.sqrt(np.add(np.power(np.pi,2),np.power(np.log(OS/100),2)))))
    
    wn=float(np.divide(b,np.sqrt(np.subtract(1,np.power(e,2)))))
    a=float(np.divide(4,np.multiply(b,e)))
    location(a, b)
    
print("Given Parameters:\n1.(Ts,Tp)\n2.(%OS,Ts)\n3.(%OS,Tp)")    
choice=int(input("Enter the choice(1/2/3): "))

if(choice==1):
    Ts=float(input("Enter Ts(s):"))
    Tp=float(input("Enter Tp(s):"))
    f1(Ts,Tp)

elif(choice==2):
    OS=float(input("Enter O.S(%):"))
    Ts=float(input("Enter Ts(s):"))
    f2(OS,Ts)

elif(choice==3):
    OS=float(input("Enter O.S(%):"))
    Tp=float(input("Enter Tp(s):"))
    f1(OS,Tp)
        
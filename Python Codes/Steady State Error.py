import numpy as np

print("1.Given Kv and Damping Ratio\n2.Given Steady State Error and Natural frequency:")
choice=int(input("Choose(1/2):"))

if (choice==1):
    Kv=float(input("Enter Kv: "))
    Z=float(input("Enter Damping Ratio:"))
    wn=np.multiply(np.multiply(2,Z),Kv)
    wn=np.around(wn,2)
    a=np.multiply(np.multiply(2,Z),wn)
    a=np.around(a,2)
    K=np.multiply(a,Kv)
    print("Natural Frequency: ",wn,"\na:",a,"\nK:",K)

elif(choice==2):
    wn=float(input("Enter Natural Frequency: "))
    SSE=float(input("Enter steady state error:"))
    Z=float(np.divide(np.multiply(wn,SSE),2))
    print("Damping Ratio: ",Z)
    
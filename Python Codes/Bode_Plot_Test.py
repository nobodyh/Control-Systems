import numpy as np
import matplotlib.pyplot as plt
import control
import xlwings as xw

s=control.TransferFunction.s

G=(10*(1-(s/2)))/((1+(0.025*s))*((1+(s/500))**2))
print(G)
print(G(2))
print(control.pole(G))
print(control.zero(G))



mag,phase,w=control.bode(G,Hz=False,dB=True,Plot=True)




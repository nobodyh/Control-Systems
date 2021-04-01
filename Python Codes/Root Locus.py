import numpy as np
from matplotlib import pyplot as plt 
import control

s=control.TransferFunction.s
G = (((s+6))/((s**3)*(s+5)))
rlist, klist = control.root_locus(G, kvect=None, xlim=[-6,1], ylim=None, plotstr=None, Plot=True, PrintGain=True, grid=True)
plt.grid(color='blue', linestyle='-.', linewidth=0.5)
plt.show()
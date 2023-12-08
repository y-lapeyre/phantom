import numpy as np
import matplotlib.pyplot as plt


print(np.cos(np.pi))

Hwarp = 1
Rwarp = 4
incl = 5 * np.pi / 180

def tilt1(R, Hwarp=Hwarp, Rwarp=Rwarp, incl=incl):
    if (R < Rwarp-Hwarp):
        inc =  0.
        c = 'k'

    elif (R < Rwarp + 3 * Hwarp):
        inc = np.arcsin(0.5*(1.+np.sin(np.pi/(2.*Hwarp)*(R-Rwarp)))*np.sin(incl))
        c = 'b'
    #elif (R < Rwarp + Hwarp):
        #inc = np.arcsin(0.5*(1.+np.sin(np.pi/(2.*Hwarp)*(-R+Rwarp)))*np.sin(incl))
        #c = 'r'
        #inc = incl*(0.5*np.tanh((R-Rwarp)/1.) +0.5) #TROP MOCHE
    else:
        inc = 0.
        c = 'k'
    
    return inc, c

Rarr = np.linspace(1, 10, 100)
tilt = []
color = []

for R in Rarr:
    beta, c = tilt1(R)
    tilt.append(beta)
    color.append(c)

plt.scatter(Rarr, tilt, c=color, marker="x")
plt.xticks(np.arange(0, 10, 0.5), rotation=45)
plt.minorticks_on()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()

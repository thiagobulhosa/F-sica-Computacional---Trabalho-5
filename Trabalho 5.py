import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def fun (t,y,q,m,B,E):
    f = np.empty_like (y)

    f[0] = y[1]
    f[1] = (q/m)*B*y[3]

    f[2] = y[3]
    f[3] = (q/m)*(E-(B*y[1]))
    return f

q=1
m=1
B=1
E=1
y0  = [0,0,0,0]
te  = np.linspace (0, 50, 1000)
ts  = (te.min(), te.max())
s   = solve_ivp (fun, t_span=ts, y0=y0, t_eval=te, args=(q,m,B,E), rtol=1.e-10, atol=1.e-10)

R=np.sqrt((s.y[0]-te)**2+(s.y[2]-1)**2)
plt.plot (s.y[0], s.y[2], '.b')
plt.plot (te,R,"red")
plt.show ()
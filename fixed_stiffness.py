import numpy as np
import matplotlib.pyplot as plt
from utils.params import *
from scipy.integrate import odeint

# Constructing M, C and H matrices
M = (m_foot * l_foot**2)/3
C = Bh + Br
H = Br + Bh + C

# list to store values
theta_list = [theta]
theta_dot_list = [theta_dot]
kr_list = []
kh_list = []
tau_r_list = []
theta_ddot_list = []



def calc_theta_d(t,mov):
    if t<=2:
        tht =  0.244346*(20*t**3 - 15*t**4 + 3*t**5)/16 - 0.122173
    else:
        tht =  0.122173
    if mov == 1:
        return tht
    else:
        return -tht

def fixed_AIC(y, t, kr_bar, tau_e, M, C, m_foot, l_foot_com, mov ):

    theta_d = calc_theta_d(t, mov)
    theta_e = theta_d - y[0]
    G = -m_foot * 9.81 *l_foot_com * np.cos(y[0])
    noise = np.random.randint(0, 1)
    kh = noise + np.exp(np.log(101)/3*t) - 0.5
    tau_r = (kr_bar*(theta_e) - Br* y[1] + tau_e)
    tau_h = kh*theta_e - Bh * y[1]
    theta_ddot = (1/M)*(tau_r + tau_h - C*y[1] - G)
    print('tauh', tau_h)
    theta_ddot_list.append(theta_ddot)

    return [y[1], theta_ddot]


# specify the number of movements
n_movements = 2

for movement in range(n_movements):
    t = np.linspace(0, 3, 300) 
    if movement % 2 == 0:
        # going up
        mov = 1
        tau_e1 = -1*tau_e
    else:
        # going down
        mov =2
        tau_e1 = tau_e
    sol = odeint(fixed_AIC, [theta_list[-1], theta_dot_list[-1]], t, args=(kr_bar, tau_e, M, C, m_foot, l_foot_com, mov))
    theta_list += list(sol[:,0])
    theta_dot_list += list(sol[:,1])

theta_d = []
for movement in range(n_movements):
    if movement % 2 == 0:
        # going up
        mov = 1
    else:
        # going down
        mov =2
    theta_d += [calc_theta_d(q,mov) for q in t]

plt.plot(theta_d)
plt.plot(theta_list)
plt.show()

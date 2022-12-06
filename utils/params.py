import numpy as np

Br = 1
beta= 0.0005
f = 0.9
g = 0.1
theta_adm = 0.0244346
tau_e = 3
kr_bar = 125
kf = 0.1
m_foot = 1.2122
m_calf = 3.8874
l_foot = 0.2569
l_calf = 0.4157
Bh = 2.51
m_act = 3.5
phi = 0.0872665
l_calf_com = 0.75 * l_calf
l_foot_com = 0.5 * l_foot

# initial params
theta = -0.1309
theta_dot = 0
theta_ddot = 0
alpha = 1
timestep = 0.1
Emax = -np.inf
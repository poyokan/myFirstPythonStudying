import numpy as np
from numpy import sin
from numpy import pi
from numpy import cos
import time

#np.info(sin)




# start = time.time()
# omega0x,omega0y=np.array([0]),np.array([0])

# thetax,thetay=np.array([0]),np.arrya([0])

# omegax =omega0x / cos(np.deg2rad(thetax))
# omegay =omega0y / cos(np.deg2rad(thetay))

# omega = (omegax,omegay)
# endtime = time.time() - start

def calc_omega(omega0,theta):
    omega0x,omega0y = omega0[0],omega0[1]
    thetax,thetay=theta[0],theta[1]

    omegax = omega0x / cos(np.deg2rad(thetax))
    omegay = omega0y / cos(np.deg2rad(thetay))

    omega = (omegax,omegay)

    return omega

# data1 = 0
# data2 = np.array((0,0))

# print(data1,":",type(data1))
# print(data2,":",type(data2))


# start = time.time()

# omega0_1 = (5,5)
# theta_1 = (0,0)

# omega_1 = calc_omega(omega0_1,theta_1)
# end= time.time()

# print(omega0_1)
# print(end - start)



# start = time.time()

# omega0_2 = np.array((5,5))
# theta_2 = np.array((2,2))

# omega_2 = calc_omega(omega0_2,theta_2)

# end = time.time()

# print(omega_2)
# print(end - start)


print(np.array(1))

print(np.array((1,1)))

print(np.array(np.array((1,1))))

print(np.array([1,1]))

print(type(np.array((1,1))))
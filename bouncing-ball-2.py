#https://physics.stackexchange.com/questions/256468/model-formula-for-bouncing-ball
from math import sqrt
import matplotlib.pyplot as plt
from  ball_opencv import free_fall
import cv2
import numpy as np
import time

aaaa= free_fall()
h0 = 600         # m/s
v = 0          # m/s, current velocity
g = 10         # m/s/s
t = 0          # starting time
dt = 0.1    # time step
rho = 0.75     # coefficient of restitution
tau = 0.10     # contact time for bounce
hmax = h0      # keep track of the maximum height
h = h0
hstop = 1   # stop when bounce is less than 1 cm
freefall = True # state: freefall or in contact
t_last = -sqrt(2*h0/g) # time we would have launched to get to h0 at t=0
vmax = sqrt(2 * hmax * g)
H = []
T = []
start_time=time.time()
while(hmax > hstop):
  if(freefall):
    hnew = h + v*dt - 0.5*g*dt*dt
    if(hnew<0):
      t = t_last + 2*sqrt(2*hmax/g)
      freefall = False
      t_last = t + tau
      h = 0
    else:
      t = t + dt
      v = v - g*dt
      h = hnew
  else:
    t = t + tau
    vmax = vmax * rho
    v = vmax
    freefall = True
    h = 0
  hmax = 0.5*vmax*vmax/g
  current_time=time.time()
  H.append(h)
  T.append(current_time-start_time)
  print(int(h),"-- ",t)
  rendered=aaaa.step(255,int(h0-h),h0,current_time-start_time)
  cv2.imshow( 'im', rendered )
  cv2.waitKey(1)

print("stopped bouncing at t=%.3f\n"%(t))

plt.figure()
plt.plot(T, H)
plt.xlabel('time')
plt.ylabel('height')
plt.title('bouncing ball')
plt.show()
# gaussian distribution
# defined by mean (my) and variance (sigma_squared)
# f(x) = 1/(sqrt(2*pi*math.pow(sigma, 2.0))) * exp(-0.5 * (x - math.pow(mu,2.0))/math.pow(sigma,2.0))
# large variance => wide spread distribution  => more uncertain
# large variance => thin spread distribution  => less uncertain

import math
# first calculation with a kalman filter
def kalman(x, mu, sigma_squared):
  y = (1.0 / math.sqrt(2.0 * math.pi * sigma_squared)
       * math.exp(-0.5 * (math.pow(x - mu, 2.0) / sigma_squared)))
  return y

# SENSING UPDATE (update): updated gaussian from two gaussians (measurement update step)
def sensor_update(mean1, var1, mean2, var2):
  new_mean = (1.0 / (var1 + var2)) * ((var2 * mean1) + (var1 * mean2))
  new_var = 1.0 / ((1.0 /var1) + (1.0 /var2))
  return [new_mean, new_var]

# MOTION UPDATE (prediciton):
def motion_update(mean1, var1, mean2, var2):
  new_mean = mean1 + mean2
  new_var = var1 + var2   
  return [new_mean, new_var]
    
#main
"""
## Test Kalmanfilter 
x = 8
mu = 10
sigma_squared = 4
print kalman(x, mu, sigma_squared)
"""
"""
## Test sensor and motion update
print sensor_update(10., 8., 13., 2.)
print motion_update(8., 4., 10., 6.)
"""

measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0.
sig = 10000.

#Please print out ONLY the final values of the mean
#and the variance in a list [mu, sig]. 
update = sensor_update
predict = motion_update

# Insert code here
for i in range(len(measurements)):
    [mu, sig] = update(mu, sig, measurements[i], measurement_sig)
    [mu, sig] = predict(mu, sig, motion[i], motion_sig)

print [mu, sig]

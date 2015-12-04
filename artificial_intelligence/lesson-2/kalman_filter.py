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
    
#main
x = 8
mu = 10
sigma_squared = 4
print kalman(x, mu, sigma_squared)


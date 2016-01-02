#!/usr/bin/env python

# Make a robot called myrobot that starts at
# coordinates 30, 50 heading north (pi/2).
# Have your robot turn clockwise by pi/2, move
# 15 m, and sense. Then have it turn clockwise
# by pi/2 again, move 10 m, and sense again.
#
# Your program should print out the result of
# your two sense measurements.
#
# Don't modify the code below. Please enter
# your code at the bottom.

from math import *
import random


class robot_motion:
  def __init__(self, turn, forward):
    self.turn_ = turn
    self.forward_ = forward

landmarks  = [[20.0, 20.0], [80.0, 80.0], [20.0, 80.0], [80.0, 20.0]]
world_size = 100.0


class robot:
    def __init__(self):
        self.x = random.random() * world_size
        self.y = random.random() * world_size
        self.orientation = random.random() * 2.0 * pi
        self.forward_noise = 0.0;
        self.turn_noise    = 0.0;
        self.sense_noise   = 0.0;

    def set(self, new_x, new_y, new_orientation):
        if new_x < 0 or new_x >= world_size:
            raise ValueError, 'X coordinate out of bound'
        if new_y < 0 or new_y >= world_size:
            raise ValueError, 'Y coordinate out of bound'
        if new_orientation < 0 or new_orientation >= 2 * pi:
            raise ValueError, 'Orientation must be in [0..2pi]'
        self.x = float(new_x)
        self.y = float(new_y)
        self.orientation = float(new_orientation)


    def set_noise(self, new_f_noise, new_t_noise, new_s_noise):
        # makes it possible to change the noise parameters
        # this is often useful in particle filters
        self.forward_noise = float(new_f_noise);
        self.turn_noise    = float(new_t_noise);
        self.sense_noise   = float(new_s_noise);


    def sense(self):
        Z = []
        for i in range(len(landmarks)):
            dist = sqrt((self.x - landmarks[i][0]) ** 2 + (self.y - landmarks[i][1]) ** 2)
            dist += random.gauss(0.0, self.sense_noise)
            Z.append(dist)
        return Z


    def move(self, turn, forward):
        if forward < 0:
            raise ValueError, 'Robot cant move backwards'

        # turn, and add randomness to the turning command
        orientation = self.orientation + float(turn) + random.gauss(0.0, self.turn_noise)
        orientation %= 2 * pi

        # move, and add randomness to the motion command
        dist = float(forward) + random.gauss(0.0, self.forward_noise)
        x = self.x + (cos(orientation) * dist)
        y = self.y + (sin(orientation) * dist)
        x %= world_size    # cyclic truncate
        y %= world_size

        # set particle
        res = robot()
        res.set(x, y, orientation)
        res.set_noise(self.forward_noise, self.turn_noise, self.sense_noise)
        return res

    def Gaussian(self, mu, sigma, x):

        # calculates the probability of x for 1-dim Gaussian with mean mu and var. sigma
        return exp(- ((mu - x) ** 2) / (sigma ** 2) / 2.0) / sqrt(2.0 * pi * (sigma ** 2))


    def measurement_prob(self, measurement):

        # calculates how likely a measurement should be

        prob = 1.0;
        for i in range(len(landmarks)):
            dist = sqrt((self.x - landmarks[i][0]) ** 2 + (self.y - landmarks[i][1]) ** 2)
            prob *= self.Gaussian(dist, self.sense_noise, measurement[i])
        return prob



    def __repr__(self):
        return '[x=%.6s y=%.6s orient=%.6s]' % (str(self.x), str(self.y), str(self.orientation))



def eval(r, p):
    sum = 0.0;
    for i in range(len(p)): # calculate mean error
        dx = (p[i].x - r.x + (world_size/2.0)) % world_size - (world_size/2.0)
        dy = (p[i].y - r.y + (world_size/2.0)) % world_size - (world_size/2.0)
        err = sqrt(dx * dx + dy * dy)
        sum += err
    return sum / float(len(p))


####   DON'T MODIFY ANYTHING ABOVE HERE! ENTER CODE BELOW ####

def particle_filter(old_particle, motion, observation, num_particles):
  p = old_particle
  ########
  ## move particles
  p2 = []
  for i in range(num_particles):
      p2.append(p[i].move(motion.turn_, motion.forward_))
  assert(len(p) == num_particles)
  p = p2

  ########
  ## sense and weight
  w = []
  for i in range(num_particles):
    w.append(p[i].measurement_prob(observation))
  assert(len(w) == num_particles)

  ########
  ## normalize
  W = sum(w)
  w_norm = []
  for i in range(num_particles):
    w_norm.append(w[i]/W)

  assert(abs(sum(w_norm) - 1.0) <= 0.000001)
  prob = w_norm

  ########
  ## rasampling selection

  # my implementation
  """
  p3 = []
  accu = 0.0
  rand_idx = int(random.uniform(0, N-1))
  for i in range(num_particles):
    x = random.uniform(0, sum(prob))
    idx = rand_idx
    accu = prob[rand_idx]
    #print "x",x
    while x > accu:
      #print x, accu
      idx = (idx + 1) % num_particles
      accu += prob[idx]
    p3.append(p[idx])
    #print len(p3)
  p = p3
  print p
  """
  # thrun wheel

  p3 = []
  idx = int(random.uniform(0, num_particles-1))
  beta = 0
  max_prob = max(prob)
  for i in range(num_particles):
    beta = beta + random.random() * 2 * max_prob
    while prob[idx] < beta:
      beta = beta - prob[idx]
      idx = (idx + 1) % num_particles
    p3.append(p[idx])
  p = p3

  #smart wheel implementation
  """
  p3 = []
  for i in range(num_particles):
     r = random.uniform(0, sum(prob))
     s = 0.0
     for index in range(len(prob)):
         s += w[index]
         if r < s: break
     p3.append(p[index])
  p = p3
  print p
  """
  return p


##################
### Exercise 1 ###
##################
# Make a robot called myrobot that starts at
# coordinates 30, 50 heading north (pi/2).
# Have your robot turn clockwise by pi/2, move
# 15 m, and sense. Then have it turn clockwise
# by pi/2 again, move 10 m, and sense again.
#
# Your program should print out the result of
# your two sense measurements.
"""
myrobot = robot()
myrobot.set(30,50,pi/2)
myrobot = myrobot.move(-pi/2,15.0)
z_one = myrobot.sense()
print z_one
myrobot = myrobot.move(-pi/2,10.0)
z_two = myrobot.sense()
print z_two
"""
##################
### Exercise 2 ###
##################
# Add Noise
# Forawrd = 5.0, turn_noise = 0.1, sense_noise = 5.0
"""
myrobot = robot()
myrobot.set_noise(5.0, 0.1, 5.0)
myrobot.set(30.0, 50.0, pi/2)
myrobot = myrobot.move(-pi/2, 15.0)
z_one = myrobot.sense()
print z_one
myrobot = myrobot.move(-pi/2,10.0)
z_two = myrobot.sense()
print z_two
"""

###################################
### Exercise 3.1, 3.2, 3.3, 3.4 ###
###################################
# 3.1. initialize 1000 particles
# 3.2. move
# 3.3. importance weight
# 3.4. normalize weights

T = 10
N = 1000
particles = []

########
## initialize particles
my_real_robot = robot()
for i in range(N):
    r = robot()
    r.set_noise(0.05, 0.05, 5.0) ### required for measurement_prob(Z)
    particles.append(r)

########
## define motion
motions = robot_motion(0.1, 5.0)


########
## move and sense of the actual robot
for i in range(T):
  my_real_robot.move(motions.turn_, motions.forward_)
  Z = my_real_robot.sense()
  particles = particle_filter(particles, motions, Z, N)
  print eval(my_real_robot, particles) ## print "correctness"
#print particles


##################
### Exercise 4 ###
##################
# Probability of not seeing p3
"""
p = [0.6, 1.2, 2.4, 0.6, 1.2]
n = []
N= len(p)
p_sum = sum(p)

for i in range(N):
  n.append(p[i] / p_sum)

assert( abs(sum(n) - 1.0) <= 0.000001)
not_p3 = (1.0 - n[2])
prob_not_p3 = not_p3 ** N # Probability of not seeing p3 in 5 consecutive draws
print prob_not_p3
"""

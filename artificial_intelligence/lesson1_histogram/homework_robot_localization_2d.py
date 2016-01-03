# The function localize takes the following arguments:
#
# colors:
#        2D list, each entry either 'R' (for red cell) or 'G' (for green cell)
#
# measurements:
#        list of measurements taken by the robot, each entry either 'R' or 'G'
#
# motions:
#        list of actions taken by the robot, each entry of the form [dy,dx],
#        where dx refers to the change in the x-direction (positive meaning
#        movement to the right) and dy refers to the change in the y-direction
#        (positive meaning movement downward)
#        NOTE: the *first* coordinate is change in y; the *second* coordinate is
#              change in x
#
# sensor_right:
#        float between 0 and 1, giving the probability that any given
#        measurement is correct; the probability that the measurement is
#        incorrect is 1-sensor_right
#
# p_move:
#        float between 0 and 1, giving the probability that any given movement
#        command takes place; the probability that the movement command fails
#        (and the robot remains still) is 1-p_move; the robot will NOT overshoot
#        its destination in this exercise
#
# The function should RETURN (not just show or print) a 2D list (of the same
# dimensions as colors) that gives the probabilities that the robot occupies
# each cell in the world.
#
# Compute the probabilities by assuming the robot initially has a uniform
# probability of being in any cell.
#
# Also assume that at each step, the robot:
# 1) first makes a movement,
# 2) then takes a measurement.
#
# Motion:
#  [0,0] - stay
#  [0,1] - right
#  [0,-1] - left
#  [1,0] - down
#  [-1,0] - up

#############################################
### Update Probabilities with Observation ###
#############################################
def normalize(mat):
  mat_sum = 0
  for i in range(len(mat)):
    mat_sum = mat_sum + sum(mat[i])
  #sqprint mat_sum 
  for i in range(0, len(mat)):
    for j in range(0, len(mat[0])):
      mat[i][j] = mat[i][j]/mat_sum
  #show(mat)
  #print "line"  
  return mat

# sense
def update(probability_vect, world_vect, observation, sensor_right):
  #assert len(probability_vect) == len(world_vect)
  
  pHit = sensor_right
  pMiss = (1.0 - pHit)
  n = len(probability_vect)
  ## weight
  for i in range(0, n):
    for j in range(0, len(probability_vect[0])):
      if world_vect[i][j] == observation:
        probability_vect[i][j] = probability_vect[i][j] * pHit
      else:
        probability_vect[i][j] = probability_vect[i][j] * pMiss
  #    hit = (observation == world_vect[i])
  #    probability_vect[i] = probability_vect[i] * ((hit * pHit + (1-hit) * pMiss))
    ## normalize
  probability_vect = normalize(probability_vect)  
  
  #probability_assertion(probability_vect)
  return probability_vect

########################################
### Inaccurate Robot Motion Function ###
### mv     - movement
### p_vect - probability vector
########################################
def move(p_matrix, mv, p_move): 
  assert type(mv[0]) == int
  assert type(mv[1]) == int
  #assert (abs(sum(p_matrix) - 1.0) <= eps)
  """
  res_matrix = []
  if(mv[0] != 0):
    for i in range(len(p_matrix)):
      res_matrix.append([])
      for j in range(len(p_matrix[0])):
        s =     p_matrix[(i - mv[0]) % len(p_matrix)][j] * p_move
        s = s + p_matrix[i % len(p_matrix)][j] * (1.0 - p_move)      
        res_matrix[i].append(s)
  elif(mv[1] != 0):
    for i in range(len(p_matrix)):
      res_matrix.append([])
      for j in range(len(p_matrix[0])):
        s =     p_matrix[i][(j - mv[1]) % len(p_matrix[i])]  * p_move
        s = s + p_matrix[i][j % len(p_matrix[i])] * (1.0 - p_move)      
        res_matrix[i].append(s)
  else:
    res_matrix = p_matrix
  """
  p_res = [[0.0 for row in range(len(colors[0]))] for col in range(len(colors))]
  
  for i in range(len(p_matrix)):
    for j in range(len(p_matrix[i])):
      p_res[i][j] = ((p_move * p_matrix[(i - mv[0]) % len(p_matrix)][(j - mv[1]) % len(p_matrix[i])]) 
                      + ((1.0 - p_move) * p_matrix[i][j])) 
  #res_vect = normalize(res_vect)
  #assert len(res_vect) == len(p_vect)
  #probability_assertion(res_vect)
  #return res_matrix
  return p_res
#####################
### Main Function ###
#####################

def localize(colors,measurements,motions,sensor_right,p_move):
  # initializes p to a uniform distribution over a grid of the same dimensions as colors
  pinit = 1.0 / float(len(colors)) / float(len(colors[0]))
  p = [[pinit for row in range(len(colors[0]))] for col in range(len(colors))]
    
  # >>> Insert your code here <<<
  #print "Initial:"
  #show(p)
  for i in range(len(motions)):
    p = move(p, motions[i], p_move)
    #print "Round "+ str(i) + " move:"
    #show(p)
    p = update(p, colors, measurements[i], sensor_right)
    #print "Round "+ str(i) + " update:"
    #show(p)  
  return p

def show(p):
  rows = ['[' + ','.join(map(lambda x: '{0:.5f}'.format(x),r)) + ']' for r in p]
  print '[' + ',\n '.join(rows) + ']'
    
#############################################################
# For the following test case, your output should be 
# [[0.01105, 0.02464, 0.06799, 0.04472, 0.02465],
#  [0.00715, 0.01017, 0.08696, 0.07988, 0.00935],
#  [0.00739, 0.00894, 0.11272, 0.35350, 0.04065],
#  [0.00910, 0.00715, 0.01434, 0.04313, 0.03642]]
# (within a tolerance of +/- 0.001 for each entry)

colors = [['R','G','G','R','R'],
          ['R','R','G','R','R'],
          ['R','R','G','G','R'],
          ['R','R','R','R','R']]
measurements = ['G','G','G','G','G']
motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]
p = localize(colors,measurements,motions,sensor_right = 0.7, p_move = 0.8)
show(p) # displays your answer
"""
colors = [['R', 'G'],
          ['R', 'R'],
          ['G', 'R'],
          ['R', 'G'],
          ['G', 'G']]
measurements = ['R', 'R', 'G', 'G', 'G', 'R']
motions = [[0, 0], [-1, 0], [0, 1], [0, -1], [0, 1], [1, 0]]
sensor_right = 0.99
p_move = 0.97
p = localize(colors,measurements,motions,sensor_right = 0.7, p_move = 0.8)
show(p) # displays your answer
"""

"""
test=[[1,2,3,4],
      [5,6,7,8],
      [9,10,11,12]]
check=[[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12]]
       
var = move(test,[0,1],1.0)
show(var)
"""

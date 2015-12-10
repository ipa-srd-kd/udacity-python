import sys


eps = sys.float_info.epsilon
#### equal distribution over 5 Positions ####
#p=[0.2, 0.2, 0.2, 0.2, 0.2]
#print p
sys.float_info.epsilon


#############################
### Probability Assertion ###
#############################
def probability_assertion(vect):
  for i in range(len(vect)):
    assert 0 <= vect[i] <= 1
  assert abs(sum(vect)-1) <= eps



#############################################
#### equal distribution over n Positions ####
#############################################
#p=[]
#n = 5
#for i in range (0,n):
#  p.append(1.0/n)    
#print p

#############################
### Initial Distribution ####
#############################

def initial_probability(n):
  assert n > 0
  ### function
  probability_vect = []
  for i in range(0, n):
    probability_vect.append(1.0/n)
  assert (len(probability_vect) == n)
  probability_assertion(probability_vect)
  return probability_vect

#############################################
### Update Probabilities with Observation ###
#############################################
def normalize(vect):
  vect_sum = sum(vect)
  for i in range(0, len(vect)):
    vect[i] = vect[i]/vect_sum  
  return vect

# sense
def update(probability_vect, world_vect, observation):
  assert len(probability_vect) == len(world_vect)
  
  pHit = 0.6
  pMiss = 0.2
  n = len(probability_vect)
  ## weight
  for i in range(0, n):
    if world_vect[i] == observation:
      probability_vect[i] = probability_vect[i] * pHit
    else:
      probability_vect[i] = probability_vect[i] * pMiss
#    hit = (observation == world_vect[i])
#    probability_vect[i] = probability_vect[i] * ((hit * pHit + (1-hit) * pMiss))
  ## normalize
  probability_vect = normalize(probability_vect)  
  
  probability_assertion(probability_vect)
  return probability_vect

######################################
### Accurate Robot Motion Function ###
######################################

# movement =  0       -> no movement
# movement =  1.. n   -> 1..n step(s) to the right
# movement = -1 .. -n -> 1..n step(s) to the left   
def move(prob_vect, movement): 
  assert type(movement) == int
  assert (abs(sum(prob_vect) - 1.0) <= eps)
  res_vect=[]
  if movement == 0:
    res_vect = prob_vect   
  else:
    for i in range(len(prob_vect)):
      res_vect.append(prob_vect[(i - movement) % len(prob_vect)])
  res_vect = normalize(res_vect)
  assert len(res_vect) == len(prob_vect)
  probability_assertion(res_vect) 
  return res_vect

########################################
### Inaccurate Robot Motion Function ###
### mv     - movement
### p_vect - probability vector
########################################
def move_inacc(p_vect, mv): 
  #motion_model = [0.1, 0.8, 0.1]
  assert type(mv) == int
  assert (abs(sum(p_vect) - 1.0) <= eps)
  pExact = 0.8
  pUndershoot = 0.1
  pOvershoot = 0.1
  res_vect=[]
  for i in range(len(p_vect)):
    s =     p_vect[((i-1) - mv) % len(p_vect)] * pUndershoot
    s = s + p_vect[(i - mv)     % len(p_vect)] * pExact
    s = s + p_vect[((i+1) - mv) % len(p_vect)] * pOvershoot    
    res_vect.append(s)
  
  res_vect = normalize(res_vect)
  assert len(res_vect) == len(p_vect)
  probability_assertion(res_vect)
  return res_vect

#####################
### Main Function ###
#####################

'''
world = ["green", "red", "red", "green", "green"]
n = len(world)
probabilities = initial_probability(n)
print("World:    "+str(world))
print("Initial:        "+str(probabilities))
print("number of Cell: "+str(n))

## P(probabilities | observation)  Posterior Distribution:
observation_vect = ["red", "red", "green", "green"]
for i in range(len(observation_vect)):
  probabilities = update(probabilities, world, observation_vect[i])
  print("Observation:    "+str(observation_vect[i]))
  print(str(i)+". Update:      "+str(probabilities))      
'''
## Test accurate motion model
'''
print "Shifting test"
alias = [0, 0, 1, 0, 0]
movement = [3, 2, 1, 0, -1, -2, -3]
for i in range(len(movement)):
  print str(movement[i])+": "+str(move(alias, movement[i]))
'''
## Test inaccurate motion model
'''
#inacc_test_vect = initial_probability(5)
inacc_test_vect =[1, 0, 0, 0, 0]
for i in range(1000):
  inacc_test_vect = move_inacc(inacc_test_vect,1)
print inacc_test_vect
'''
## Test with motion
world = ["green", "red", "red", "green", "green"]
n = len(world)
prob = initial_probability(n)
measurements = ["green", "red", "red", "green"]
motions = [1,1,1,1]

for i in range(len(motions)):
  prob = update(prob, world, measurements[i])
  prob = move(prob, motions[i])
  print str(i)+". "+str(prob)


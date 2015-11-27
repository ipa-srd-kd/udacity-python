import sys
#### equal distribution over 5 Positions ####
#p=[0.2, 0.2, 0.2, 0.2, 0.2]
#print p

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
  assert (abs(sum(probability_vect) - 1.0) <= sys.float_info.epsilon)
  return probability_vect

#############################################
### Update Probabilities with Observation ###
#############################################


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
  probability_sum = sum(probability_vect)
  for i in range(0, n):
    probability_vect[i] = probability_vect[i]/probability_sum  
  assert (abs(sum(probability_vect) - 1.0) <= sys.float_info.epsilon)
  return probability_vect

###############################
### Robot Movement Function ###
###############################

# movement =  0       -> no movement
# movement =  1.. n   -> 1..n step(s) to the right
# movement = -1 .. -n -> 1..n step(s) to the left   
def move(prob_vect, movement): 
  assert type(movement) == int
  res_vect=[]
  if movement == 0:
    return prob_vect   
  for i in range(len(prob_vect)):
    res_vect.append(prob_vect[(i - movement) % len(prob_vect)])
  return res_vect


#####################
### Main Function ###
#####################

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


print "Shifting test"
alias = [0, 0, 1, 0, 0]
movement = [3, 2, 1, 0, -1, -2, -3]
for i in range(len(movement)):
  print str(movement[i])+": "+str(move(alias, movement[i]))
print()


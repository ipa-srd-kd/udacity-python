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

########################################
### Observation                     ####
### [green,red,red,red,green,green] ####
########################################

def initial_probability(n):
  assert n > 0
  ### function
  probability_vect = []
  for i in range(0, n):
    probability_vect.append(1.0/n)
  assert (len(probability_vect) == n)
  assert (abs(sum(probability_vect) - 1.0) <= sys.float_info.epsilon)
  return probability_vect

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
    


world = ["green", "red", "red", "green", "green"]
print("World:    "+str(world))
n = len(world)
print("number of Cell: "+str(n))
## Prior:
probabilities = initial_probability(n)
print("Initial:        "+str(probabilities))

## P(probabilities | observation)  Posterior Distribution:
observation_vect = ["red", "red", "green", "green"]
for i in range(len(observation_vect)):
  print("Observation:    "+str(observation_vect[i]))
  probabilities = update(probabilities, world, observation_vect[i])
  print(str(i)+". Update:      "+str(probabilities))      



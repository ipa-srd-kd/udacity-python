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
  probability_vect = []
  for i in range(0, n):
    probability_vect.append(1.0/n)
  assert (len(probability_vect) == n)
  assert (abs(sum(probability_vect) - 1.0) <= sys.float_info.epsilon)
  return probability_vect

def update(probability_vect, observation_vect):
  assert len(probability_vect) == len(observation_vect)
  n = len(probability_vect)
  for i in range(0, n):
    if observation_vect[i] == "green":
      probability_vect[i] = probability_vect[i] * 0.2
    elif observation_vect[i] == "red":
      probability_vect[i] = probability_vect[i] * 0.6
    else:
      probability_vect[i] = probability_vect[i] * 0.2
  # normalize
  probability_sum = sum(probability_vect)
  for i in range(0, n):
    probability_vect[i] = probability_vect[i]/probability_sum
  assert (abs(sum(probability_vect) - 1.0) <= sys.float_info.epsilon)
  return probability_vect
    


observations = ["green", "red", "red", "green", "green"]
print("Observation:    "+str(observations))
n = len(observations)
print("number of Cell: "+str(n))
probabilities = initial_probability(n)
print("Initial:        "+str(probabilities))
probabilities = update(probabilities, observations)
print("1. Update:      "+str(probabilities))      


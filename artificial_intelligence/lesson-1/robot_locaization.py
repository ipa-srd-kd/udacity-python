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
  probability_vector = []
  for i in range(0, n):
    probability_vector.append(1.0/n)
  assert (len(probability_vector) == n)
  assert ((sum(probability_vector) - 1) <= sys.float_info.epsilon)
  return probability_vector

def update(probability_vect, observation_vect):
  assert len(probability_vect) == len(observation_vect)
  n = len(probability_vect)
  for i in range(0, n):
    if observation_vect[i] == "green":
      probability_vect[i] = probability_vect[i] * 0.6
    elif observation_vect[i] == "red":
      probability_vect[i] = probability_vect[i] * 0.2
    else:
      probability_vect[i] = probability_vect[i] * 0.2
  return probability_vect
    


observations = ["green", "red", "red", "green", "green"]
print observations
n = len(observations)
print n
probabilities = initial_probability(n)
print "Initial: "+str(probabilities)
probabilities = update(probabilities, observations)
print "First Update: "+str(probabilities)      


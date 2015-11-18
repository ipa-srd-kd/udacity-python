# naive way: straight forward

cpt = (3,4)
mpt = (3,4)

def distanceToOrigin(p):
  from math import floor, sqrt
  return floor(sqrt(p[0]**2 + p[1]**2))
  
CartesianDistanceToOrigin = distanceToOrigin

def ManhattanDistanceToOrigin(p):
  return abs(p[0]) + abs(p[1])

print("Cartesian: "+str(CartesianDistanceToOrigin(cpt)))
print("Manhattan: "+str(ManhattanDistanceToOrigin(mpt)))


# naive way: name space
#
#import manhattan
#import cartesian
#
#CARTESIAN, MANHATTAN = 0, 1
#cpt = (CARTESIAN, 3, 4)
#mpt = (MANHATTAN, 3, 4)
#pt=mpt
#
#if pt[0] == CARTESIAN:
#  print(cartesian.distanceToOrigin(pt))
#elif pt[0] == MANHATTAN:
#  print(manhattan.distanceToOrigin(pt))
#else:
#  raise TypeError, pt 


# Lambda Expression
from math import floor, sqrt
cpt = (3,4, lambda p: floor(sqrt(p[0]**2 + p[1]**2)))
mpt = (3,4, lambda p: abs(p[0]) + abs(p[1]))
print "Cartesian: "+str(cpt[2](cpt))
print "Manhattan: "+str(mpt[2](mpt))

# struct replacement

class cartesian:
  x, y = 0, 0
  def distanceToOrigin(self):
    from math import floor, sqrt
    return floor(sqrt(self.x**2 + self.y**2))

class manhattan:
  x, y = 0, 0
  def distanceToOrigin(self):
    return abs(self.x) + abs(self.y)
    
cpt = cartesian()
cpt.x, cpt.y = 3, 4

mpt = manhattan()
mpt.x, mpt.y = 3, 4
print "Cartesian: "+str(cpt.distanceToOrigin())
print "Manhattan: "+str(mpt.distanceToOrigin())

# smarter:

class point:
  def __init__(self, x=0, y=0):
    self.x, self.y = x, y
    
class cartesian(point):
  def distanceToOrigin(self):
    return floor(sqrt(self.x**2 + self.y**2))
class manhattan(point):
  def distanceToOrigin(self):
    return abs(self.x) + abs(self.y)
    
    


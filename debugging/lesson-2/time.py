class Time:
  def __init__(self, h = 0, m = 0, s = 0):
    self._hours   = h
    self._minutes = m
    self._seconds = s
    
  def hours(self):
    return self._hours
    
  def minutes(self):
    return self._minutes
    
  def seconds(self):
    return self._seconds
    
  def __repr__(self):
    return "{:02d}:{:02d}:{:02d}".format(self.hours(), self.minutes(), 
           self.seconds())
           
           
t = Time(13, 0, 0)
print t

t = Time(-1, -2, -3)
print t

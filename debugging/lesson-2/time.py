class Time:
  def __init__(self, h = 0, m = 0, s = 0):
    assert 0 <= int(h) <= 23
    assert 0 <= int(m) <= 59
    assert 0 <= int(s) <= 60
  
    self._hours   = int(h)
    self._minutes = int(m)
    self._seconds = int(s)
    
  def hours(self):
    return self._hours
    
  def minutes(self):
    return self._minutes
    
  def seconds(self):
    return self._seconds
    
  def __repr__(self):
    return "{:02d}:{:02d}:{:02d}".format(self.hours(), self.minutes(), 
           self.seconds())
           
           


#t = Time(-1, -2, -3)
#print t

#t = Time("two minutes past midnight")


# accepted inputs #
###################

time_vect=[Time(13, 0, 0), 
           Time(3.14, 0, 0)] 


for time_obj in time_vect:
  print time_obj

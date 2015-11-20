class Time:
  def __init__(self, h = 0, m = 0, s = 0):
    assert 0 <= int(h) <= 23
    assert 0 <= int(m) <= 59
    assert 0 <= int(s) <= 60
  
    self._hours   = int(h)
    self._minutes = int(m)
    self._seconds = int(s)
    
  def invariant_check(self):
    assert 0 <= self.hours() <= 23
    assert 0 <= self.minutes() <= 59
    assert 0 <= self.seconds() <= 60
  
  def hours(self):
    return self._hours
    
  def minutes(self):
    return self._minutes
    
  def seconds(self):
    return self._seconds
    
  def __repr__(self):
    return "{:02d}:{:02d}:{:02d}".format(self.hours(), self.minutes(), 
           self.seconds())
     
  def seconds_since_midnight(self):
    return self.hours() * 3600 + self.minutes() * 60 + self.seconds()
    
  def advance(self, s):
    self.invariant_check()
    old_seconds = self.seconds_since_midnight()
    
    # some complex code
    
    self.invariant_check()
    assert(self.seconds_since_midnight() )
           
           


#t = Time(-1, -2, -3)
#print t

#t = Time("two minutes past midnight")


# accepted inputs #
###################

time_vect=[Time(13, 0, 0), 
           Time(3.14, 0, 0)] 


for time_obj in time_vect:
  print time_obj

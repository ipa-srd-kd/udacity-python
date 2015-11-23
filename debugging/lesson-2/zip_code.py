class ZIPCode:
  #US only
  def __init__(self, zip):
    self._zip = zip
    self.checkRep()
  
  def zip(self):
    return self._zip
    
  def checkRep(self):
    assert len(self.zip()) == 5
    for i in range (0,5):
      assert '0' <= self._zip[i] <= '9' 
      
      
ZIPCode("12345")

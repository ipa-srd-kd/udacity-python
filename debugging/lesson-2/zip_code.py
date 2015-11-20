class ZIPCode:
  #US only
  def __init__(self, zip):
    self._zip = zip
    self.checkRep()
  
  def zip(self):
    return self._zip()
    
  def checkRep(self):
    assert ...

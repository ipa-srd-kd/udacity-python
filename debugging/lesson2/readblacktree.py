class RedBlackTree:
  def checkRep(self): # invariant
    assert self.rootHasNoParent()
    assert self.rootIsBlack()
    assert self.tressIsAcyclic()
    assert self.parentsConsistent()
    assert self.equalNumber Of BlackNodesOnSubtrees()
    assert self.redNodesHaveOnlyBlackChildren()
    
  def rootHasNodParent(self):
    return self._root.parent is None
  
  def insert(self, x):
    self.checkRep()
    #
    #
    #
    self.checkRep()
  

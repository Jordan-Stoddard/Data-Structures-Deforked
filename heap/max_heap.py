class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    pass

  def delete(self):
    pass

  def get_max(self):
    pass

  def get_size(self):
    pass

  def _bubble_up(self, index):
    # keep bubbling up until we've either reached the top of the heap
    # or we've reached a point where the parent is higher priority.
    while index > 0:
      # On a single bubble_up iteration:
        # get the parent index
        parent = (index -1 ) // 2
        # compare the child against the value of the parent.
        # if the child's value is higher prio than it's parents value:
        if self.storage[index] > self.storage[parent]:
          # swap them.
          self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
          # update the child's index to be the new index it is now at.
          index = parent
        # otherwise, child is at a valid spot
        else:
          # stop bubbling
          break

  def _sift_down(self, index):
    pass

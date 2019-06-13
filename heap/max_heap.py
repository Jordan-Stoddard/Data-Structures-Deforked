class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    #append value to end of array.
    # bubble the new element up the heap until it is at a valid spot.
    self.storage.append(value)
    self._bubble_up(len(self.storage)-1)

  def delete(self):
    # save a reference to the old priority element so we can return it.
    # overwrite the old priority element with the last element in the array.
    # Remove the last element from the array (cause we don't want multiple copies)
    # sift down the element at index 0.
    pass

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    # return len(self.storage)

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

# heap = Heap()
# heap.insert(2)
# heap.insert(100)
# heap.insert(5)
# heap.insert(3)
# heap.insert(100)
# heap.insert(100)
# heap.insert(101)
# print(heap.get_max())
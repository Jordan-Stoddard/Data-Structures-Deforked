class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    #append value to end of array.
    # bubble the new element up the heap until it is at a valid spot.
    self.storage.append(value)
    self._bubble_up(len(self.storage)-1)

  def delete(self):
    # save the old prio and return it.
    # overwrite the old priority element with the last element in the array.
    # Remove the last element from the array (cause we don't want multiple copies)
    # sift down the element at index 0.
    old_prio = self.storage[0]
    self.storage[0], self.storage[-1] = self.storage[-1], self.storage[0]
    del self.storage[-1]
    self._sift_down(0)
    return old_prio

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

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
    # While the index is less than the length of the array, iterate.
    while index < len(self.storage)-1:
      left_child = (2*index) + 1
      right_child = (2*index) + 2
      # Check if there is an element at the left_child index, if not break.
      try:
        a = self.storage[left_child]
      except IndexError:
        break
      try:
        b = self.storage[right_child]
      except IndexError:
        pass

      # First check if the parent is less than both the children nodes.
      # if it is, check if the left_child is greater than or equal to the right_child
      # if it is, swap the parent and the left_child and set the index to be the left_child.
      # then start the next iteration.
      # otherwise, swap the parent and the right_child, set the index to be the right_child
      # then start the next iteration.
      try:
        if self.storage[index] < self.storage[left_child] and self.storage[index] < self.storage[right_child]:
          if self.storage[left_child] >= self.storage[right_child]:
            self.storage[index], self.storage[left_child] = self.storage[left_child], self.storage[index]
            index = left_child
            continue
          else:
            self.storage[index], self.storage[right_child] = self.storage[right_child], self.storage[index]
            index = right_child
            continue
      except IndexError:
        pass

      # If the parent node is not less than both of it's children
      # Check to see if the parent is less than the left child
      # if it is, swap the parent and the left_child, set the index to left_child
      # and continue to the next iteration.
      # Otherwise, continue down the function.
      try:
        if self.storage[index] < self.storage[left_child]:
          self.storage[index], self.storage[left_child] = self.storage[left_child], self.storage[index]
          index = left_child
          continue
      except IndexError:
        pass

      # If the parent node is not less than both of it's children
      # Check to see if the parent is less than the right_child
      # if it is, swap the parent and the right_child, set the index to right_child
      # and continue to the next iteration.
      # Otherwise, continue down the function.
      try:
        if self.storage[index] < self.storage[right_child]:
          self.storage[index], self.storage[right_child] = self.storage[right_child], self.storage[index]
          index = right_child
          continue
      except IndexError:
        pass

      # If none of these conditions are met, it means the parent is greater than both children
      # And so we break out of the loop.
      break

heap = Heap()
heap.insert(6)
heap.insert(8)
heap.insert(10)
heap.insert(9)
heap.insert(1)
heap.insert(9)
heap.insert(9)
heap.insert(5)
print(heap.storage)
heap.delete()
print(heap.storage)
heap.delete()
print(heap.storage)
heap.delete()
print(heap.storage)
heap.delete()
print(heap.storage)
heap.delete()
print(heap.storage)




# print(heap.get_max())
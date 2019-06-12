class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # Don't forget to wrap the value in a node.

    # 1. compare the element against the current node's value
    # 2. based on the result of the comparison, go left or right
    # 3. If we find an empty spot, park the value there.
    # 4. Otherwise, go back to step 1.

    # What is the base case going to be?
    # base case: we found an empty spot where we can add the value.

    if value < self.value:
      # if value is less we go left
      # if there is no left child, we can park this node here.
      if not self.left:
        self.left = BinarySearchTree(value)
        #recurse on the left child
      else:
        self.left.insert(value)
    elif value >= self.value:
      # if value is greater than or equal to we go right
      # if there is no left child, we can park this node here.
      if not self.right:
        self.right = BinarySearchTree(value)
      # If there is a node here, we go back to the beginning of insert to check the node at the value of the node that is already parked here.
      else:
        self.right.insert(value)

  def contains(self, target):
    pass

  def get_max(self):
    pass

  def for_each(self, cb):
    pass
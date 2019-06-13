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
        # recurse on the left child
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
  # base case: target == self.value return True
    if target == self.value:
      return True
    
  # If we've traversed down to a node where there is no right or left node, return False
    if not self.right and not self.left:
        return False
      
    # if the target is greater than the current value then go into if statement.
    if target > self.value:
      # Once in the if statement, check if there is a self.right, if there isn't
      # We know the target isn't in the tree, because it's greater than the current value.
      # so return false.
      if not self.right:
        return False
      # Otherwise, recursively call contains on the right node, which starts us over at
      # The beginning of this function, but at the node to the right.
      else:
        return self.right.contains(target)
        # Repeat the above but on the left side if target is less than self.value.
    elif target < self.value:
      if not self.left:
        return False
      else:
        return self.left.contains(target)

  def get_max(self):
    # If the BTS doesn't have anything at the root, return error message.
    # else, set current_max to be self.value.
    if not self.value:
      return 'You can only call get_max on a BTS that has at least one value.\n Try inserting a value first.'
    else:
      current_max = self.value
    # Because higher numbers will always be to the right, we only have to check nodes to the right.
    # First check if there is a node to the right, if there isn't, it means there is no greater
    # value, so then we just return the current_max.
    if not self.right:
      return current_max
    
    # If there is a value to the right, check to see if it is greater to than the current max.
    # If it is, recursively call get_max on the the right hand node.
    # Otherwise, just return the current_max, because we know that this is now the greatest node.
    if self.right.value > current_max:
      return self.right.get_max()
    else:
      return current_max

  def for_each(self, cb):
    # inside for_for each we build a helper function called traverse, that takes in a node.
    # We then call traverse, and pass in the current node (which should be the root node)
    def traverse(node): 
      # If the current node is None return out of traverse.
      if not node:
        return
      # call the cb function passing in the current node.value
      cb(node.value)
      # Recursively call traverse on the left node
      traverse(node.left)
      # Recursively call traverse on the right node.
      traverse(node.right)
    # for_each retruns traverse, passing in the root node.
    return traverse(self)
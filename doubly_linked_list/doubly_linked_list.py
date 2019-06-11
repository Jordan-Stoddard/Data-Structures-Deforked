"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is pointing to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is pointing to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    new_node = ListNode(value)

    if not self.head and not self.tail:
      self.head = new_node
      self.tail = new_node
      self.length += 1
    elif self.head is self.tail:
      self.head = new_node
      self.head.next = self.tail
      self.length += 1
    else:
      old_head = self.head
      self.head = new_node
      self.head.next = old_head
      old_head.prev = self.head
      self.length += 1


  def remove_from_head(self):
    # If the list is empty
    if not self.head and not self.tail:
      return None
    # If the list only has one item in it.
    elif self.head is self.tail:
        old_head = self.head
        self.head = None
        self.tail = None
        self.length -= 1
        return old_head.value
    else:
        old_next = self.head.next
        self.head = old_next
        self.head.next = old_next.next
        self.tail.prev = None

  def add_to_tail(self, value):
    new_node = ListNode(value)
    # if the list is empty
    if not self.head and not self.tail:
        self.head = new_node
        self.tail = new_node
        self.length += 1
    # if the list only has one item
    elif self.head is self.tail:
        self.tail = new_node
        self.tail.prev = self.head
        self.head.next = self.tail
        self.length += 1
    else:
        old_tail = self.tail
        self.tail = new_node
        self.tail.prev = old_tail
        old_tail.next = self.tail
        self.length += 1

  def remove_from_tail(self):
    #if the list is empty
    if not self.head and not self.tail:
        return None
    # if the list only has one item
    elif self.head is self.tail:
        old_tail = self.tail
        self.head = None
        self.tail = None
        self.length -= 1
        return old_tail.value
    else:
        old_prev = self.tail.prev
        self.tail = old_prev
        self.tail.prev = old_prev.prev
        self.tail.next = None

  def move_to_front(self, node):
    # If the node put in is already the head node.
    if self.head == node:
      return
      # if there's only one node in the list.
    elif node.prev == self.head and node == self.tail:
      old_head = self.head
      self.head = node
      self.head.prev = None
      self.head.next = old_head
      self.tail = old_head
      self.tail.prev = self.head
      self.tail.next = None

    else:
        # Pull current item out of list.
      next_node = node.next
      prev_node = node.prev
      next_node.prev = node.prev
      prev_node.next = node.next
        # Set it to head
      old_head = self.head
      self.head = node
      self.head.next = old_head
      self.head.prev = None
      old_head.prev = self.head

  def move_to_end(self, node):
    # if the node put in is already the tail node.
    if self.tail == node:
      return
    # if there's only one item in the list
    elif node.next == self.tail and node == self.head:
      old_tail = self.tail
      self.tail = node
      self.tail.next = None
      self.tail.prev = old_tail
      self.head = old_tail
      self.head.prev = None
      self.head.next = self.tail
      
    else:
      # Pull current item out of list.
      next_node = node.next
      prev_node = node.prev
      next_node.prev = node.prev
      prev_node.next = node.next
        #Set it to tail
      old_tail = self.tail
      self.tail = node
      self.tail.next = None
      self.tail.prev = old_tail
      old_tail.next = self.tail

  def delete(self, node):
    #If there's only one item in the list.
    if node.next == None and node.prev == None:
      self.head = None
      self.tail = None
      self.length -= 1
      # If the node selected is the head node.
    elif self.head == node:
      old_head = self.head
      self.head = old_head.next
      self.head.next = old_head.next.next
      self.head.prev = None
      self.length -= 1
      # if the node selected is the tail node.
    elif self.tail == node:
      old_tail = self.tail
      self.tail = old_head.prev
      self.tail.prev = old_tail.prev.prev
      self.tail.next = None
      self.length -= 1
      # if there's only one item in the list.
    elif self.head.next == self.tail and self.tail.prev == self.head:
      self.head = node
      self.head.next = None
      self.head.prev = None
      self.tail = node
      self.tail.next = None
      self.tail.prev = None
    else:
      next_node = node.next
      prev_node = node.prev
      next_node.prev = node.prev
      prev_node.next = node.next
      self.length -= 1
    
  def get_max(self):
    # If the list is empty return None.
    if not self.head and not self.tail:
      return None
      # Set the current node
    current = self.head
      # set the current max value
    current_max = self.head.value
          #While node does not == None
    while current:
      # if the current value is greater than the current max
      # set the current max to be the current value and iterate to the next node
      if current.value > current_max:
        current_max = current.value
      current = current.next
      # Once we get to the end of the DLL, return current_max
    return current_max
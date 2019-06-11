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
    if not self.head and not self.tail:
      return None
    
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

    if not self.head and not self.tail:
        self.head = new_node
        self.tail = new_node
        self.length += 1

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
    if not self.head and not self.tail:
        return None
    
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
    if self.head == node:
      return
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
    if self.tail == node:
      return
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
    if node.next == None and node.prev == None:
      self.head = None
      self.tail = None
      self.length -= 1
    elif self.head == node:
      old_head = self.head
      self.head = old_head.next
      self.head.next = old_head.next.next
      self.head.prev = None
      self.length -= 1
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
    pass


# DLL = DoublyLinkedList(ListNode(1))
# DLL.add_to_tail(33)
# DLL.add_to_tail(24)
# DLL.add_to_tail(25)
# node_1 = DLL.head
# print(node_1.value)
# node_2 = DLL.head.next
# print(node_2.value)
# node_3 = node_2.next
# print(node_3.value)
# node_4 = node_3.next
# print(node_4.value)

# node_2.delete()

# print(node_1.value)
# print(node_2.value)
# print(node_3.value)
# print(node_4.value)







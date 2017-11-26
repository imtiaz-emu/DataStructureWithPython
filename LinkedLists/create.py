class Node:
  
  def __init__(self, data):
    self.data = data
    self.next = None  # Assign next value to null


class LinkedList:

  def __init__(self):
    self.head = None  # Assign head value to null


llist = LinkedList()  # create a new linkedList
llist.head = Node(1)  # Add the first Node
second = Node(2)  # Add the second Node
third = Node(3)   # Add the third Node

# Every Node has data, but no reference to the next node.
llist.head.next = second  # Refer next node of Head
second.next = third # Refer next node of Second

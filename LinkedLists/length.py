class Node:
  
  def __init__(self, data):
    self.data = data
    self.next = None  # Assign next value to null


class LinkedList:

  def __init__(self):
    self.head = None  # Assign head value to null
    
  # Traverse the linkedlist
  def printList(self):
    temp_head = self.head
    while(temp_head):
      print(temp_head.data)
      temp_head = temp_head.next
    
  def insertAtBeginning(self, data):
    current_head = llist.head
    llist.head = Node(data)
    llist.head.next = current_head
    
  def nodeLengthItr(self):
    count = 0
    head = self.head
    while(head is not None):
      head = head.next
      count += 1
    print("Iterative Count =", count)
    
  def nodeLengthRec(self, head):
    if head is None:
      return 0
    else:
      return 1 + self.nodeLengthRec(head.next)
    
llist = LinkedList()  # create a new linkedList
llist.head = Node(10)  # Add the first Node
second = Node(12)  # Add the second Node
third = Node(13)   # Add the third Node

# Every Node has data, but no reference to the next node.
llist.head.next = second  # Refer next node of Head
second.next = third # Refer next node of Second

llist.insertAtBeginning(9)
llist.insertAtBeginning(8)

llist.nodeLengthItr()
print("Recursive Count =", llist.nodeLengthRec(llist.head))
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
  
  def insertAtEnd(self, data):
    new_node = Node(data)
    current_head = llist.head
    if(current_head.next == None):
      current_head.next = new_node
    else:
      while(current_head.next):
        current_head = current_head.next
      current_head.next = new_node
  
  def insertInMiddle(self, prevNode, newNode):
    if(prevNode is None):
      return
    newNode.next = prevNode.next
    prevNode.next = newNode
  
  def delete(self, node):
    currentHead = self.head
    if(currentHead is not None):
      if(currentHead.data == node.data):
        self.head = currentHead.next
        currentHead = None
        return
    
    while(currentHead is not None):
      if currentHead.data == node.data:
        break
      prevNode = currentHead
      currentHead = currentHead.next

    if (currentHead == None):
      return

    prevNode.next = currentHead.next
    currentHead = None
    
llist = LinkedList()  # create a new linkedList
llist.head = Node(10)  # Add the first Node
second = Node(12)  # Add the second Node
third = Node(13)   # Add the third Node

# Every Node has data, but no reference to the next node.
llist.head.next = second  # Refer next node of Head
second.next = third # Refer next node of Second

llist.insertAtBeginning(9)
llist.insertAtEnd(15)
llist.insertInMiddle(third, Node(14))
print("Before Delete")
llist.printList()

llist.delete(Node(14))
print("After Delete")
llist.printList()
class Node:
  
  def __init__(self, data):
    self.data = data
    self.next = None  # Assign next value to null


class LinkedList:

  def __init__(self):
    self.head = None  # Assign head value to null

  def printList(self):
    temp_head = self.head
    while(temp_head):
      print(temp_head.data)
      temp_head = temp_head.next


def sortAndMerge(n1, n2):
  if (n1 == None):
    return n2
  if (n2 == None):
    return n1

  if (n1.data <= n2.data):
    n1.next = sortAndMerge(n2, n1.next)
    return n1
  else:
    n2.next = sortAndMerge(n1, n2.next)
    return n2


llist_1 = LinkedList()
llist_1.head = Node(11)
second = Node(22)
third = Node(33)
llist_1.head.next = second
second.next = third

llist_2 = LinkedList()
llist_2.head = Node(1)
second = Node(4)
third = Node(29)
fourth = Node(35)
llist_2.head.next = second
second.next = third
third.next = fourth

print("list 1:")
llist_1.printList()
print("list 2:")
llist_2.printList()
print("Sorted Merge: ")
sortAndMerge(llist_2.head, llist_1.head)

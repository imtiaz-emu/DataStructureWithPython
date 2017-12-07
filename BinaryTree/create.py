class Node:

  def __init__(self, key):
    self.root = key
    self.left = None
    self.right = None


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

'''
It'll generate a tree like:

          1
        /   \
      2       3
    /   \
  4       5

'''
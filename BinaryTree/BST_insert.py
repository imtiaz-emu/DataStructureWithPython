class Node:

  def __init__(self, key):
    self.data = key
    self.left = None
    self.right = None

def insert(root, node):
  if root == None:
    root = node
  else:
    if(root.data > node.data):
      if(root.left == None):
        root.left = node
      else:
        insert(root.left, node)
    else:
      if (root.right == None):
        root.right = node
      else:
        insert(root.right, node)

def inOrder(root):

  if root:
    inOrder(root.left)
    print(root.data)
    inOrder(root.right)

root = Node(8)
insert(root, Node(3))
insert(root, Node(10))
insert(root, Node(2))
insert(root, Node(5))
insert(root, Node(6))


inOrder(root)

'''
It'll generate a tree like:

              8
            /   \
          3       10
        /  \    /
      2      5 6

'''


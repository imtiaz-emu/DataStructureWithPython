class Node:

  def __init__(self, key):
    self.root = key
    self.left = None
    self.right = None

# Root - Left - Right
def preOrder(root):

  if root:
    print(root.root)
    preOrder(root.left)
    preOrder(root.right)

# Left - Right - Root
def postOrder(root):

  if root:
    postOrder(root.left)
    postOrder(root.right)
    print(root.root)

# Left - Root - Right
def inOrder(root):

  if root:
    inOrder(root.left)
    print(root.root)
    inOrder(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

'''
Generated output for the above tree will be:
  Preorder Traversal : 1 2 4 5 3
  Inorder Traversal  :  4 2 5 1 3
  Postorder Traversal : 4 5 2 3 1
'''

preOrder(root)
postOrder(root)
inOrder(root)
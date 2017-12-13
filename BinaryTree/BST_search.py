class Node:

  def __init__(self, key):
    self.root = key
    self.left = None
    self.right = None


def search(node, key):
  if(node == None or node.root == key):
    return node
  elif (node.root < key):
    return search(node.right, key)

  return search(node.left, key)

root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(2)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(15)

print(search(root, 15))

'''
It'll generate a tree like:

              8
            /   \
          3       10
        /  \    /  \
      2      5 6    15

'''
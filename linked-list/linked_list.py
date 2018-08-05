class Node:
	def __init__(self):
		self.data = data
    		self.pointer = pointer
    
	def __str__(self):
    		return str(self.data)
    
class LinkedList():
  def __init__(self, head=None):
    self.head = None
  
  def insert(self, data):
    new_node = Node(data)
    new_node.pointer = self.head
    self.head = new_node

  def size(self):
    current = self.head
    count = 1
    while current != None:
      count = count + 1
      current = current.pointer
    return count

  def search(self, target):
    current = self.head
    while current:
      if current.data == target:
        return current
      else:
        current = current.pointer
    if current is None:
      return None

if __name__ == "__main__":
  ll = LinkedList(20)
  ll.insert(30)
  ll.insert(40)
  print(ll.head.data, ll.head.pointer)
  print(ll.size)
  print(ll.search(30))
  print(ll.search(50))

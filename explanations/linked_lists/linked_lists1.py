class Node:
    def __init__(self,d ,n = None):
        self.data = d
        self.next_node = n 


    def get_next(self):
        return self.next_node
    
    def set_next(self,new_next):
        self.next_node = new_next

    
    def get_data(self):
        return self.data
    
    def set_data(self,new_data):
        self.data = new_data



class Linked_list:
    def __init__(self,root=None):
        self.root = root #Node
        self.size = 0


    
    def get_size(self):
        return self.size

    def add(self, data):
        new_node = Node(data,self.root)
        self.root = new_node
        self.size += 1

    def remove(self,data):
        current_node = self.root # we keep track of the current node

        prev_node= None # keep track of the prev node

        while current_node:
            if current_node.get_data() == data:
                if prev_node:
                    prev_node.set_next(current_node.get_next())
                else:
                    self.root = current_node.get_next()
                self.size -= 1
                return True
            else:
                prev_node = current_node
                current_node = current_node.get_next()
        return False
    
    def find(self,data):
        current_node = self.root
        while current_node:
            if current_node.get_data() == data:
                return f"Found: {current_node.get_data()}"
            else:
                current_node = current_node.get_next()
        return None


    def traversal(self):
        current_node = self.root
        while current_node:
            print(current_node.get_data())
            current_node = current_node.get_next()


    def __str__(self):
        return f"Linked list size {self.size}"
    
    


linked_list = Linked_list()

linked_list.add(5)
linked_list.add(8)
linked_list.add(12)

print(linked_list.remove(12))
linked_list.traversal()
#print(linked_list.find(8))


    
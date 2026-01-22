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

    # challenges

    def traversal(self):
        current_node = self.root
        while current_node:
            print(current_node.get_data())
            current_node = current_node.get_next()
    
    def insert_end(self,data):
        current_node = self.root
        
        while current_node:
            if current_node.get_next() == None:
                new_node = Node(data,None)
                current_node.set_next(new_node)
                self.size += 1

                return f"Added: {data} to the end"
                
            current_node = current_node.get_next()
            
        
    def find_middle(self):
        fast = self.root
        slow = self.root
        
        while fast and fast.get_next(): # we allways check befor moving
            
            fast = fast.get_next()
            fast = fast.get_next()
            
            slow = slow.get_next()
        return f"Middle: {slow.get_data()}"
    
    #get the last element of the list

    def get_last_element(self):
        current_node = self.root

        while current_node:
            if current_node.get_next() == None:
                return f"last element: {current_node.get_data()}"

            current_node = current_node.get_next()


    def get_size_by_walking(self):
        steps = 0
        current_node = self.root
        while current_node:
            steps += 1
            current_node = current_node.get_next()
        return f"steps(size): {steps}"
    
    def get_second_to_last(self):
        current_node = self.root
        prev_node = None

        while current_node:
            if current_node.get_next() == None:
                if prev_node:
                    return f"second To last: {prev_node.get_data()}"
                else:
                    return None
            prev_node = current_node
            current_node = current_node.get_next()

    def delete_from_end(self):
        current_node = self.root
        prev_node = None

        while current_node:
            if current_node.get_next() == None:
                if prev_node:
                    prev_node.set_next(None)
                else:
                    self.root = None
                self.size -= 1
                return "Data removed from the end"

            prev_node = current_node    
            current_node = current_node.get_next()

    def find_kth_element(self,k):
        fast = self.root
        slow = self.root

        for _ in range(k):
            if fast.get_next() != None:
                fast = fast.get_next()
        
        while fast:
            fast = fast.get_next()
            slow = slow.get_next()

        return slow.get_data()
    
    






            


linked_list = Linked_list()

linked_list.add(5)
linked_list.add(8)
linked_list.add(12)
linked_list.add(10)

print(linked_list.insert_end(80))
print(linked_list.insert_end(25))
#print(linked_list.delete_from_end())

#print(linked_list.find_middle())

#print(linked_list.get_last_element())

#print(linked_list.get_size_by_walking())
print(linked_list.find_kth_element(1))
#print(linked_list.get_second_to_last())
#linked_list.traversal()
#print(linked_list.get_size())

#print(linked_list.remove(12))
#linked_list.traversal()
#print(linked_list.find(8))


    
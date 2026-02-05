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


    def get_root(self):
        return self.root
    

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
        
        while fast and fast.get_next(): # we allways check before moving
            
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
            fast = fast.get_next()

        
        while fast:
            fast = fast.get_next()
            slow = slow.get_next()
        
        return f"kth elemt = {slow.get_data()}"

    def insert_after_given_value(self,target, num_to_insert):
        current_node = self.root
        

        while current_node:
            if current_node.get_data() == target:
                new_node = Node(num_to_insert,current_node.get_next())
                current_node.set_next(new_node)
                return "Inserted"

            current_node = current_node.get_next()

    def find_kth_from_start(self, k_from_start):
        counter = 0
        current_node = self.root

        while current_node:
            if counter == k_from_start:
                return current_node.get_data()
            
            counter += 1
            current_node = current_node.get_next()

    def are_the_same(self,linked_list_a, linked_list_b):
        pointer_a = linked_list_a.get_root()
        pointer_b = linked_list_b.get_root()

        while pointer_a and pointer_b:
            if pointer_a.get_data() != pointer_b.get_data():
                return False
            pointer_a = pointer_a.get_next()
            pointer_b = pointer_b.get_next()

        if pointer_a == None and pointer_b == None:
            return True

        return False
    

    def find_node(self,data_to_find):
        current_node = self.root

        while current_node:
            if current_node.get_data() == data_to_find:
                return current_node 
            current_node = current_node.get_next()

    def get_last_node(self):
        current_node = self.root

        while current_node:
            if current_node.get_next() == None:
                return current_node
            current_node = current_node.get_next()


    def find_shared_node(self,linked_list_a, linked_list_b):
        pointer_a = linked_list_a.get_root()
        pointer_b = linked_list_b.get_root()

        # this is known as two pointer switching
        while pointer_a != pointer_b:
            
            if pointer_a == None:
                pointer_a = linked_list_b.get_root()
            else:
                pointer_a = pointer_a.get_next()


            if pointer_b == None:
                pointer_b = linked_list_a.get_root()
            # if the pointer is not null we just move
            # if we update and move at the same time we skip the root id the next linked list
            else:
                pointer_b = pointer_b.get_next()
            
        

        # all the time we use pointers we only perform one operation at the time either we move or update, never the two,

        if pointer_a == pointer_b:
            return pointer_b.get_data()
        
        return False
    

    def swap_neighboring_nodes(self):
        current_node = self.root
        next_node = current_node.get_next()

        while current_node and current_node.get_next():
            
            if next_node:
                temp = current_node.get_data()
                current_node.set_data(next_node.get_data())
                next_node.set_data(temp)
            
            current_node = current_node.get_next().get_next() # we advance twice
            
            
            if current_node != None:
                next_node = current_node.get_next()


    def move_tail_to_head(self):
        
        current_node = self.root
        prev_node = None


        while current_node:
            if current_node.get_next() == None and self.root:
                current_node.set_next(self.root)
                prev_node.set_next(None)
                self.root = current_node
                return "shifted"
            prev_node = current_node
            current_node = current_node.get_next()


    def move_tail_to_head_nodes(self):
        current_node = self.root
        prev_node = None
        next_node = None

        while current_node:

            next_node = current_node.get_next()
            current_node.set_next(prev_node)
            prev_node = current_node
            current_node = next_node


        self.root = prev_node



        
            
            

        


            


    


        

linked_list_a = Linked_list()
#linked_list_b = Linked_list()

linked_list_a.add(4)
linked_list_a.add(3)
linked_list_a.add(2)
linked_list_a.add(1)


"""
linked_list_a.add(5)
linked_list_a.add(4)
linked_list_a.add(3)
linked_list_a.add(2)
linked_list_a.add(1)
"""
#linked_list_a.swap_neighboring_nodes()

#linked_list_a.traversal()

#intersection_node = linked_list_a.find_node(4)
#linked_list_b.get_last_node().set_next(intersection_node)

linked_list_a.move_tail_to_head_nodes()

linked_list_a.traversal()
#linked_list_a.traversal()
#linked_list_b.traversal()

#print(linked_list_a.find_shared_node(linked_list_a,linked_list_b))

#print(linked_list.are_the_same(linked_list,linked_list_b))

#linked_list.add(50)
#linked_list.add(40)
#linked_list.add(30)
#linked_list.add(20)
#linked_list.add(10)

#print(linked_list.find_kth_from_start(2))
#print(linked_list.find_kth_element(2))
#linked_list.add(5)
#linked_list.add(3)
#linked_list.add(1)
#linked_list.insert_after_given_value(3,4)

#print(linked_list.insert_end(80))
#print(linked_list.insert_end(25))
#print(linked_list.delete_from_end())

#print(linked_list.find_middle())

#print(linked_list.get_last_element())

#print(linked_list.get_size_by_walking())
#print(linked_list.find_kth_element(1))
#print(linked_list.get_second_to_last())
#linked_list.traversal()
#print(linked_list.get_size())

#print(linked_list.remove(12))
#linked_list.traversal()
#print(linked_list.find(8))


    
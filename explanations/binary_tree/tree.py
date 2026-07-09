class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    def inorder_traversal(self):
        # as far left as posible when we cant we print and 
        # Move to the right node and move again as left as posible 

        if self.left:
            self.left.inorder_traversal()
        print(self.value)

        if self.right:
            self.right.inorder_traversal()

        # we allways go first to the smallest values

    def preorder_traversal(self):
        #almost the same as inorder, the only difference is that we print as soon as we reach a node 
        print(self.value)
        if self.left:
            self.left.preorder_traversal()

        if self.right:
            self.right.preorder_traversal()

    def postorder_traversal(self):
        # We get as deep as posible then we print
        
        if self.left:
            self.left.postorder_traversal()

        if self.right:
            self.right.postorder_traversal()
        print(self.value)

    # inorder vs preorder vs postorder 
    """
    Inorder: we print the smallest values first, a.k.a the leaves and we print backwards.

    Preorder: Same traversal as Inorder but we print as soon as we reach a node , a.k.a we print the nodes in the order in which they appear , MOVING left first.

    Postorder: we go as deep as posible then we print, we don't print soemthing until the child nodes are explored.

    As we can see the traversals are the same, the only thing that changes is when we print and therefore the order of such prints changes.
    """


    #find function

    def find(self, value):
        if value < self.value: # we go to the left
            if not self.left :
                return False 
            else:
                return self.left.find(value)
        elif value > self.value: # we go right
            if not self.right:
                return False
            else:
                return self.right.find(value)
        else: # if the value is the same as the current node
            return True





        

tree = TreeNode(6)
tree.insert(5)
tree.insert(2)
tree.insert(4)
tree.insert(1)
tree.insert(2)
tree.insert(4)
tree.insert(19)
tree.insert(29)
tree.insert(11)
tree.insert(4)
tree.insert(2)

#tree.inorder_traversal()
#tree.preorder_traversal()

#tree.postorder_traversal()


print(tree.find(2))











        
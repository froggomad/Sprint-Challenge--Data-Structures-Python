class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare the input value with the value of the Node
        # if value < Node's value
            # we need to go left

            # if we see there is no left, wrap value in BSTNode
            # and park it
            # if there's no node to compare the input to,
                # we can wrap the value in a BSTNode and park it
                # otherwise there is a child
                # call the left child's `insert` method
        #otherwise, value >= Node's value...
            # we need to go right
            # if we see there is no right, wrap value in BSTNode
            # and park it
            # otherwise there is a child
            # call the right child's insert method

        if value < self.value:

            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):    

        if target == self.value:
            return True

        if target < self.value and self.left is not None:
            return self.left.contains(target)

        elif target > self.value and self.right is not None:
            return self.right.contains(target)
            
        else:
            return False
               

    # Return the maximum value found in the tree
    # Head down the right side of the tree and find the max
    def get_max(self):

        if self.right is None:
            return self.value

        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):

        fn(self.value)

        if self.left:
            self.left.for_each(fn)

        if self.right:
            self.right.for_each(fn)

    def iterative_breadth_first_for_each(self, fn):        
        from collections import deque

        # using a queue (FIFO Left-To-Right)
        queue = deque()
        queue.append(self)

        while len(queue) > 0:            
            current = queue.popleft()
            fn(current.value)

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)   

        

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node:            
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)
            

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        print(node.iterative_breadth_first_for_each(lambda x: print(f"{x}")))

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        print(node.iterative_depth_first_for_each(lambda x: print(f"{x}")))

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
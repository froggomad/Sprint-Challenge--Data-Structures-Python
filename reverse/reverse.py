class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def for_each(self, fn):
        if self.next_node:
            fn(self)

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def is_empty(self):
        return self.head == None

    def reverse_list(self, node, prev): 
        if self.is_empty():
            return
        # reach the final node and make it the head
        if node.next_node == None: 
            self.head = node
            # Update the next node to previous one
            node.next_node = prev
            return          
        # store the next node
        next = node.next_node
  
        # update the next node to point to the previous one
        node.next_node = prev

        #call on the stored node
        self.reverse_list(next, node)
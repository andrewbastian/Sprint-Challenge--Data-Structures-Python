class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if the value is less than the current node's value
        if value < self.value:
            # does the current node have a left child?
            if self.left:
                self.left.insert(value)
            # otherwise, it doesn't have a left child
            # we can park the new node here
            else:
                self.left = BSTNode(value)
        # otherwise the value is greater or equal to the current node's value
        else:
            # does the current node have a right child?
            if self.right:
                # if it does, call the right child's `insert` method to repeat
                # the process
                self.right.insert(value)
            # otherwise, it doesn't have a right child
            # we can park the new node here
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check if the current node is the target value
        if self.value == target:
            return True
        # check if current node value is less than target value
        # check the right node.
        # if right node is empty check the left node
        # if the left node is empty return final answer `False`
        elif self.value < target:
            if self.right is None:
                return False
            else:
                return BSTNode.contains(self.right, target)
        else:
            if self.left is None:
                return False
            else:
                return BSTNode.contains(self.left, target)

    # Return the maximum value found in the tree
    def get_max(self):
        # check if this is the last right value in the tree,
        # if it is that node holds the highest value
        # if not run the function on the next node to the right
        if self.right is None:
            return self.value
        return BSTNode.get_max(self.right)

    # Call the function `fn` on the value of each node
    # This method doesn't return anything
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

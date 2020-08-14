# Task 3. Reverse a Linked List

"""
Inside of the `reverse` directory, you'll find a basic implementation of
a Singly Linked List. _Without_ making it a Doubly Linked List
(adding a tail attribute), complete the `reverse_list()` function within
`reverse/reverse.py`.

For example,
```
1->2->3->None
```
would become...
```
3->2->1->None
```

While credit will be given for a functional solution,
only optimal solutions will earn a ***3*** on this task.
"""


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

    def reverse_list(self, node, prev):
        if self.head is None or node.get_next() is None:
            self.head = node
            return
        # reverse the rest
        self.reverse_list(node.get_next(), prev=None)
        temp = node.get_next()
        temp.set_next(node)
        node.set_next(None)
        node.next_node = None

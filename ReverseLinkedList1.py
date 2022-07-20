class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(head: Node) -> Node:
    previous = None
    current = head
    next = None

    while (current is not None):
        next = current.next
        current.next = previous
        previous = current
        current = next

    head = previous
    return head

head = [1, 2, 3, 4, 5]
reverse(head)
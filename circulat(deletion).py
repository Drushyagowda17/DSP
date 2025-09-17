class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def delete_at_beg(self):
        if not self.head:
            print("List is empty!")
            return
        if self.head.next == self.head:  
            self.head = None
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next

    def delete_at_end(self):
        if not self.head:
            print("List is empty!")
            return
        if self.head.next == self.head: 
            self.head = None
        else:
            current = self.head
            while current.next != self.head:
                prev = current
                current = current.next
            prev.next = self.head

    def delete_at_pos(self, pos):
        if not self.head:
            print("List is empty!")
            return
        if pos == 1:
            self.delete_at_beg()
            return
        current = self.head
        count = 1
        while count < pos - 1 and current.next != self.head:
            current = current.next
            count += 1
        if current.next == self.head:
            print("Position out of range")
            return
        current.next = current.next.next

    def display(self):
        if not self.head:
            return
        current = self.head
        while True:
            print(current.data, end="-->")
            current = current.next
            if current == self.head:
                break
        print()

cll = CircularLinkedList()

cll.head = Node(10)
second = Node(20)
third = Node(30)
cll.head.next = second
second.next = third
third.next = cll.head  

print("Original Circular Linked List:")
cll.display()

cll.delete_at_beg()
print("\nAfter deleting from the beginning:")
cll.display()

cll.delete_at_end()
print("\nAfter deleting from the end:")
cll.display()

cll.delete_at_pos(1)
print("\nAfter deleting at position 1:")
cll.display()

cll.delete_at_pos(5)  


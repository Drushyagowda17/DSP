class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beg(self, data):
        temp = Node(data)
        if not self.head:
            self.head = temp
            temp.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = temp
            temp.next = self.head
            self.head = temp

    def insert_at_end(self, data):
        temp = Node(data)
        if not self.head:
            self.head = temp
            temp.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = temp
            temp.next = self.head

    def insert_at_pos(self, data, pos):
        temp = Node(data)
        if pos == 1:
            self.insert_at_beg(data)
        else:
            current = self.head
            count = 1
            while count < pos - 1 and current.next != self.head:
                current = current.next
                count += 1
            if current.next != self.head:
                temp.next = current.next
                current.next = temp

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
cll.insert_at_beg(10)
cll.insert_at_end(20)
cll.insert_at_end(30)
cll.insert_at_pos(15, 2)
cll.display()

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



class SinglyLinkedList:
    def __init__(self):      #SINGLY LINKED LIST
        self.head = None

   
    def insert_at_beg(self, data):
        new_node = Node(data)
        new_node.next = self.head       #INSERTING AT BEGINNING
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return                  #APPEND AT END
    
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_pos(self, data, position):
        if position < 1:
            print("Position must be >= 1")
            return                          #INSERT AT GIVEN POSITION
        new_node = Node(data)

        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return                                #INSERT AT BEGINNING 

        current = self.head
        count = 1

        while current is not None and count < position - 1:
            current = current.next
            count += 1

            if current is None:
             print("Position out of range")                     #MOVE THE NODE TO BEFORE INSERTION POINT
            return
        new_node.next = current.next
        current.next = new_node

    def dab(self):
        if self.head is None:
            print("no nodes")
        return                                                      #DELETEION AT BEGINNING
        current = self.head
        if current.next:
            self.head = current.next
        else:
            self.head=None
    
    def dae(self):
        previous = None
        current = self.head
        while current:                                                     #DELETION t END
            previous = current
            current = current.next
        previous.next=None

    def dap(self,position):
        if position<1:
            print("> or = 1")
            return
        
        if position ==1:
            self.head = None                                                           #DELETION AT POSITION
            return
        
        if self.head is None:
            print("empty")
        return
    
        previous =None
        current = self.head
        count =1
        while current is not None and count <= postion-1:
            previous = current
            current=current.next
            count+=1
            previous.next = current.next


    def traverse(self):
        if self.head is None:
            print("Linked List is empty")
            return
        current = self.head                                 #TRAVERSAL
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


if __name__=="__main__":
    ll=SinglyLinkedList()
    ll.append(50)
    ll.append(56)
    ll.append(65)
    ll.traverse()
    ll.insert_at_beg(11)
    ll.insert_at_pos(88,4)
    ll.insert_at_pos(77,1)
    ll.traverse()
    ll.dab()
    ll.dap(5)
    ll.dae()
    ll.traverse()

class Queue:
    def __init__(self):
        self.queue = []
    
    def is_empty(self):
        return f"Queue Empty: {len(self.queue)==0}"
    
    def enqueue (self ,data):
        self.queue.append(data)
        print(f" added :{data}")

    def dequeue(self):
        if len(self.queue)==0:
            print("Queue is empty")
        else:
            self.queue.pop(0)
            print(f"removed : {self.queue[0]}")
    def size(self):
        print( f" length of queue is : {len(self.queue)}")

    def display(self):
            print(f"queue is : {self.queue}")     

if __name__=="__main__":
    q = Queue()
    n=int(input("Enter elements:"))
    for i in range(n):
        q.enqueue(int(input(f"Enter number {i+1}:")))       
    q.display()
    q.dequeue()
    q.size()
    q.display()
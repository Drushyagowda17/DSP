class Stack:
    def __init__(self):
        self.stack=[]
    
    def push(self,item):
        self.stack.append(item)
        print(f"pushed:{item}")
        
    def pop(self):
        if self.is_empty():
            return "stack is empty"
        return f"popped:{self.stack.pop()}"
        
    def peek(self):
        if self.is_empty():
            return"stack is empty"
        return f"Top:{self.stack[-1]}"
        
    def is_empty(self):
        return len(self.stack)==0
    
    def display(self):
        print("stack(top->bottom):",self.stack[::-1])
 
    def size(self):
        return len(self.stack)
    
    def even(self):
        for i in range(self.size()):
            if (i+1) % 2 ==0:
                print(self.stack[i])
            else:
                continue

    def compeven(self):
      for i in range(0,len(self.stack),2):
          print(self.stack[i])              

    
if __name__=="__main__":
    s=Stack()
    n=int(input("Enter the numbers:"))
    for i in range(n):
        s.push(int(input(f"Enter number {i+1}:")))
    s.display()
    
    print(s.size())
    print(s.is_empty())
    print(s.peek())
    s.display()
   # s.even()
    s.compeven()
        

        

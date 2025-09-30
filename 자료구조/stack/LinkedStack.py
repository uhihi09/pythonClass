class Node:
    def __init__(self,elem,link=None):
        self.data=elem
        self.link=link

class LinkedStack:
    def __init__(self):
        self.top = None
    
    def isEmpty(self):
        return self.top == None
    
    def push(self,item):
        self.top = Node(item,self.top)
        
    def peek(self):
        if not self.isEmpty():
            return self.top.data
    
    def pop(self):
        if not self.isEmpty():
            data = self.top.data
            self.top = self.top.link
            return data
    
    def size(self):
        node = self.top
        count = 0
        while not node == None:
            node - node.link
            count += 1
        return count
    
    def __str__(self):
        arr = []
        node = self.top
        while not node == None:
            arr.append(node.data)
            node = node.link
        return str(arr)


if __name__ == "__main__":
    s = LinkedStack()
    
    print("스택: ",s)
    msg = input("문자열 입력: ")
    for c in msg:
        s.push(c)
    
    print("스택: ",s)
    
    print("문자열 출력: ",end="")
    while not s.isEmpty():
        print(s.pop(),end="")
    print()
    print("스택: ",s)
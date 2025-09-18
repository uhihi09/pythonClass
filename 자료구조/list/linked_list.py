class Node:
    def __init__(self, elem,next=None):
        self.data = elem
        self.link = next
class LinkedList:
    def __init__ (self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def isFull(self):
        return False

    def getNode(self, pos):
        if pos < 0:
            return None
        node = self.head
        while pos > 0 and node != None:
            node = node.link
            pos -= 1
        return node
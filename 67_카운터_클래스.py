class Counter:
    def __init__(self):
        self.count = 0
    
    def reset(self,initValue):
        self.count = initValue
    
    def increment(self):
        self.count += 1
    
    def get(self):
        return self.count

a = Counter()
b = Counter()

a.reset(0)
a.increment()
print(a.get)

b.reset(100)
b.increment()
print(b.get())
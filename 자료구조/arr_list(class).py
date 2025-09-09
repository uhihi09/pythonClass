class ArrayList:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def insert(self, pos, e):
        if not self.isFull() and 0 <= pos <= self.size:
            for i in range(self.size, pos, -1):
                self.array[i] = self.array[i - 1]
            self.array[pos] = e
            self.size += 1
        else:
            print("리스트 overflow 또는 유효하지 않은 삽입 위치")
            exit()

    def delete(self, pos):
        if not self.isEmpty() and 0 <= pos < self.size:
            e = self.array[pos]
            for i in range(pos, self.size - 1):
                self.array[i] = self.array[i + 1]
            self.size -= 1
            return e
        else:
            print("리스트 underflow 또는 유효하지 않은 위치")
            exit()

    def getEntry(self, pos):
        if 0 <= pos < self.size:
            return self.array[pos]
        else:
            return None

    def __str__(self):
        return str(self.array[0:self.size])

if __name__ == "__main__":
    L = ArrayList()

    print("최초 ", L)
    L.insert(0, 5)
    print("삽입", L)
    L.insert(1, 2)
    print("삽입", L)
    L.insert(0, 3)
    print("삽입", L)
    L.insert(L.size, 5)
    print("삽입", L)
    L.insert(3, 2)
    print("삽입x5", L)

    L.delete(3)
    print("삭제(2)", L)

    L.delete(L.size - 1)
    print("삭제(E)", L)

    L.delete(5)
    print("삭제(0)", L)
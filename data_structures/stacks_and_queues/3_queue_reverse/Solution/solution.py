class Stack:
    def __init__(self):
        self.data = []

    def isempty(self):
        if len(self.data) == 0: return True
        return False

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

class Queue:
    def __init__(self):
        self.data = []

    def isempty(self):
        if len(self.data) == 0: return True
        return False

    def enQueue(self, item):
        self.data.insert(0, item)

    def deQueue(self):
        return self.data.pop()

def Reverse(Q):
    S = Stack()
    while not Q.isempty():
        S.push(Q.deQueue())
    while not S.isempty():
        Q.enQueue(S.pop())

S = Stack() 
Q = Queue()
Q.enQueue(5)
Q.enQueue(4)
Q.enQueue(3)
Q.enQueue(2)
Q.enQueue(1)
Reverse(Q)
print(Q.data)
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue():
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        return str(self.__dict__)

    def printme(self):
        currentPtr = self.first
        q = []
        while currentPtr != None:
            q.append(currentPtr.data)
            currentPtr = currentPtr.next
        return q

    def enqueue(self,data):
        newData = Node(data)
        if self.first == None:
            self.first = newData
            self.last = self.first
            self.length += 1
        else:
            self.last.next = newData
            self.last = newData
            self.length += 1

    def dequeue(self):
        currentPtr = self.first
        self.first = currentPtr.next
        self.length -= 1

    def peek(self):
        return self.first.data


m = Queue()
m.enqueue("s")
m.enqueue("h")
m.enqueue("y")
print(m)
m.dequeue()
print(m.peek())
print(m.printme())
class Queue():
    MAX = 100

    def __init__(self, size):
        if size <= self.MAX:
            self.size = size
            self.front = -1
            self.rear = size
            self._queue = []
        else:
            print("Maximus sized exceeded")

    def addele(self, element):
        if self.size > 0:
            self._queue.append(element)
            self.front += 1
            self.size -= 1
            self.rear -= 1
        else:
            print("Overflow")

    def delele(self):
        if self.front >= 0:
            element = self._queue[self.front]
            self._queue.remove(element)
            self.front -= 1
            print(element)
            return element
        else:
            print("Underflow")
            return -9999
        print(self._queue)


queue = Queue(100)
queue.addele(1)
queue.addele(2)
queue.addele(3)
queue.delele()
queue.delele()
queue.delele()

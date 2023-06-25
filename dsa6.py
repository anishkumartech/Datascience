class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        else:
            raise IndexError("Queue is empty. Cannot dequeue an element.")

    def isEmpty(self):
        return len(self.queue) == 0


queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue.dequeue())  # Output: 10
print(queue.isEmpty())  # Output: False
print(queue.dequeue())  # Output: 20
print(queue.dequeue())  # Output: 30
print(queue.isEmpty())  # Output: True

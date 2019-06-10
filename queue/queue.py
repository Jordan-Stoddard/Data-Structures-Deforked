import collections

class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = collections.deque()

    def enqueue(self, item):
        self.storage.appendleft(item)
        self.size += 1
    
    def dequeue(self):
        try:
            return self.storage.pop()
        except IndexError:
            return None

    def len(self):
        return len(self.storage)

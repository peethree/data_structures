class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)
        

    def pop(self):
        if len(self.items) > 0:
            item = self.items[-1]
            self.items.remove(item)
            return item

    def peek(self):
        if len(self.items) > 0:
            return self.items[-1]

    def size(self):
        return len(self.items)

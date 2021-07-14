# enque and deque

class Queue_implementation():
    def __init__(self) -> None:
        self.data = []

    def is_empty(self):
        return self.data == []

    def iterate_queue(self):
        for _ in self.data:
            print(_)
    
    def count_queue(self):
        return len(self.data)

    def enque(self,item):
        return self.data.insert(0,item)

    def deque(self):
        return self.data.pop()



q = Queue_implementation()


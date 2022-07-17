from exceptions import Empty
class LinkedQueue:
    class _Node:
        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self,e):
        new = self._Node(e,None)
        if self.is_empty():
            self._head = new
        else:
            self._tail._next = new
        self._tail = new
        self._size = self._size + 1

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is Empty")
        value = self._head._element
        self._head = self._head._next
        self._size = self._size - 1
        if self.is_empty():
            self._tail = None
        return value

    def first(self):
        if self.is_empty():
            raise Empty("Queue is Empty")
        return self._head._element

    def display(self):
        temp = self._head
        while temp:
            print(temp._element, end=" --> ")
            temp = temp._next
        print()

ls = LinkedQueue()
ls.enqueue(10)
ls.enqueue(20)
ls.enqueue(30)
ls.enqueue(40)
ls.enqueue(50)
ls.display()
print("Popped:",ls.dequeue())
ls.display()
ls.enqueue(70)
ls.display()
print("Top Element:",ls.dequeue())
ls.display()
# Problema 4 – Stivă (20p)

class Stack:
    def __init__(self):
        self._data = []

    def push(self, x):
        self._data.append(x)
        pass

    def pop(self):
        self._data.pop()
        pass

    def peek(self):
        return self._data[len(self._data) - 1]

    def __repr__(self):
        return f"Stack({self._data})"

if __name__ == "__main__":
    s = Stack()
    s.push(5)
    s.push(7)
    print(s.__repr__())
    s.pop()
    print(s.__repr__())
    s.push(9)
    print(s.peek())  # 9
    print(s)

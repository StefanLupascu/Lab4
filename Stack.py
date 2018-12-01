class Stack:
    def __init__(self):
        self.container = []

    def push(self, element):
        self.container.append(element)

    def pop(self):
        self.container.pop(len(self.container) - 1)

    def print(self):
        print(self.container)
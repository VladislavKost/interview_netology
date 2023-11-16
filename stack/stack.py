class Stack:
    def __init__(self):
        self.stack_items = []

    def is_empty(self):
        return len(self.stack_items) == 0

    def push(self, el):
        self.stack_items.append(el)

    def pop(self):
        return self.stack_items.pop()

    def peek(self):
        if len(self.stack_items) > 0:
            return self.stack_items[-1]
        else:
            return None

    def size(self):
        return len(self.stack_items)

class StackUndo:
    def __init__(self):
        self.aktivitas = []

    def push(self, aktivitas):
        self.aktivitas.append(aktivitas)

    def pop(self):
        if self.aktivitas:
            return self.aktivitas.pop()
        return None

    def peek(self):
        if self.aktivitas:
            return self.aktivitas[-1]
        return None

    def is_empty(self):
        return len(self.aktivitas) == 0
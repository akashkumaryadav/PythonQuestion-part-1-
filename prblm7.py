class Register:
    MAX = 100

    def __init__(self, size):
        if size < self.MAX:
            self.cap = size
            self.stud = []
            self.top = -1
        else:
            print("Maximum size of 100 exceeded")

    def push(self, name):
        if self.top < self.cap:
            self.stud.append(name)
            self.top += 1
        else:
            print("Overflow")

    def pop(self):
        if len(self.stud) > 0:
            element = self.stud.pop()
            print(element)
            self.top -= 1
        else:
            print("Underflow")

    def display(self):
        if len(self.stud) > 0:
            [print(name) for name in self.stud]
        else:
            print("register is empty")


s = Register(3)
s.push("1")
s.push("2")
s.push("3")
s.display()
s.pop()
s.pop()
s.pop()
s.display()

class Adder():
    def __init__(self):
        """intitalizing the array with 0"""
        self.time = [0, 0]

    def readtime(self):
        self.time[0] = int(input("Enter number of hrs"))
        self.time[1] = int(input("Enter the number of minutes"))

    def addtime(self, t):
        print(f"Time 1:{self.time[0]}hrs, {self.time[1]}mins")
        print(f"Time 2:{t.time[0]}hrs, {t.time[1]}mins")
        c = list(map(lambda x, y: x + y, self.time, t.time))
        if c[1] > 60:
            c[0] += c[1] // 60
            c[1] = c[1] % 60
        self.time = c

    def displytime(self):
        print(f"Their sum is:{self.time[0]}hrs, {self.time[1]}mins")


a = Adder()
a.readtime()
b = Adder()
b.readtime()
b.addtime(a)
b.displytime()

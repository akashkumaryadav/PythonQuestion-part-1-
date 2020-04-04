import random


class Performance():

    def readmarks(self, number):
        """ you can chagne to this to take user input
         now it's just generating 60 random numbers between 0,number"""
        self.marks = [random.randint(0, 100) for _ in range(number)]

    def getmode(self):
        return self.mode

    def getfreqatmode(self):
        return self.frequency

    def calcmodeandfrequency(self):
        self.freq_table = {}
        for m in self.marks:
            self.freq_table[m] = self.marks.count(m)
        MAX = max(self.freq_table.values())
        self.mode = 0
        for marks, freq in self.freq_table.items():
            if freq == MAX:
                if marks > self.mode:
                    self.mode = marks
                    self.frequency = freq


cls = Performance()
cls.readmarks(60)
cls.calcmodeandfrequency()
print(f"Mode of data {cls.getmode()}")
print(f"Frequency of mode of data {cls.getfreqatmode()}")

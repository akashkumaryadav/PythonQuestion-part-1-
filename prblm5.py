class Product():
    def __init__(self, n, c, p):
        self.name = n
        self.code = c
        self.amount = p

    def display(self):
        print(f"Product {self.name}\nCode {self.code}\nAmount {self.amount}")


class Shop(Product):
    def __init__(self, name, code, price, d, t):
        super().__init__(name, code, price)
        self.day = d
        self.tax = t
        self.totalamount = 0
        self.fine = 0

    def compute(self):
        if self.day < 30 and self.day > 0:
            # totalamount = self.amount + service tax
            self.totalamount = self.amount + self.amount * self.tax + self.fine
        if self.day > 30:
            self.fine = self.amount * 2.5
            # totalamount = self.amount + service tax + fine
            self.totalamount = self.amount + self.amount * self.tax + self.fine

    def show(self):
        self.display()
        print(
            f"No. of Days {self.day} \nService Tax {self.amount * 12.5} \nFine {self.fine}")

        print(f"Total amount is {str(self.totalamount).rjust(10,' ')}")


p = Shop("toy", 101, 100, 31, 12.5)
p.compute()
p.show()

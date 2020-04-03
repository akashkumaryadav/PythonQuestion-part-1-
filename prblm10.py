def createfile():
    with open("ABC.dat", 'w') as file:
        file.write("pc=b100,up=200,q=3\n")
        file.write("pc=b200,up=200,q=2\n")
        file.write("pc=b300,up=200,q=3\n")
        file.write("pc=b400,up=200,q=4\n")
        file.write("pc=b500,up=200,q=5\n")


def checkavailability(pc):
    with open("ABC.dat") as file:
        pcode = pc
        for line in file.readlines():
            cline = line.split(",")
            price = cline[1][-3:]
            quantity = cline[2][-2:]
            if cline[0].__contains__(pcode):
                print(f"Product code is {pcode.ljust(20, ' ')}")
                print(f"Product UnitPrice is {price.ljust(20, ' ')}")
                print(f"Product quantity is {quantity.ljust(20, ' ')}")
                return "Available"
            else:
                return "Not available"


print(checkavailability("b100"))

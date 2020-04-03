"""
define a class with data members
@data members
len : length of word
wrd : orignal word
swapwrd : swapped word
sortwrd : sorted word
@methods
SwapSort() : Constructor
void readword() : to accept a word in upper case
void swapchar() : to swap first and last alphabet
void sortwrd()  : to sort the charchters
void diplay()   : display sortwrd swapwrd, wrd
"""


def main():
    class SwapSort():
        length = 0
        wrd = ""
        swapwrd = ""
        sortwrd = ""

        def __init__(self, wrd):
            self.length = len(wrd)
            self.readword(wrd)

        def readword(self, nwrd):
            if nwrd.isupper():
                self.wrd = nwrd
            else:
                print("\nWord should be in upper case only\n")

        def swapchar(self):
            bwrd = bytearray(self.wrd, encoding="utf")
            bwrd[0], bwrd[-1] = bwrd[-1], bwrd[0]
            self.swapwrd = bwrd.decode("utf")

        def sortword(self):
            self.sortwrd = "".join(sorted(self.wrd))

        def display(self):
            print(f'Orignal Word "{self.wrd}"')
            print(f'Sorted Word "{self.sortwrd}"')
            print(f'Word with swapped charachters "{self.swapwrd}"')

    word = input("Enter a word")
    s = SwapSort(word)
    # s.readword("NEWTEST")
    s.swapchar()
    s.sortword()
    s.display()


if __name__ == "__main__":
    main()

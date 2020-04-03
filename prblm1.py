def word_potential(stmnt):
    """proggram to arrange a sentence in a way that their potential
    will be in increading order"""
    terminators = [",", ".", "?", "!"]
    if stmnt[-1] in terminators:
        stmnt = stmnt[0:-1]
        list_of_word = stmnt.split()
        word_potential = {}
        for word in list_of_word:
            potential = 0
            frequency = list_of_word.count(word)
            for char in word:
                potential += ord(char)
            word_potential[potential] = (word, frequency)
    else:
        return "Invalid Statement"

    keys = list(word_potential.keys())
    keys.sort()
    finalstmnt = ""
    print(f"word | potential")
    for key in keys:
        for _ in range(word_potential[key][-1]):
            print(f"{word_potential[key][0].ljust(10)}{key}")
            finalstmnt += " "+word_potential[key][0]
    return finalstmnt.lstrip()


# statement = input("Enter a statement")
statement = "LOOK BEFORE YOU LEAP."
fs = word_potential(statement)
print(f"\nOUTPUT \n{fs}")

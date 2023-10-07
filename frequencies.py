"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for i in range(len(items)):
        items[i] = str(items[i])
    orderedSetItems = list(dict.fromkeys(items))
    for i in range(len(orderedSetItems)):
        frequencies[orderedSetItems[i]] = 0
    for key in (frequencies.keys()):
        for j in range(len(items)):
            if (key==items[j]):
                frequencies[key] = frequencies.get(key) + 1
    return frequencies

print(frequencies(["q","e","q","w"]))
print(frequencies(["4",5,4,"4"]))

'''
while True:
    try:
        print("Enter a list of strings separated by commas: ")
        inputStrings = [value for value in input().split(",")]
        orderedSetStrings = list(dict.fromkeys(inputStrings))
        dictStrings = {}
        for i in range(len(orderedSetStrings)):
            dictStrings[orderedSetStrings[i]] = 0
        for key in (dictStrings.keys()):
            for j in range(len(inputStrings)):
                if (key==inputStrings[j]):
                    dictStrings[key] = dictStrings.get(key) + 1
               
    except ValueError:
        print("Error with the value input")
    else:
        break       

print(inputStrings)
print(orderedSetStrings)
print(dictStrings)

'''
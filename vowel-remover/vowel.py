# Version 1
def removeVowel():
    string = input("Enter something: ")
    vowels = ["a", "e", "i", "o", "u"]
    newString = ""
    counter = 0
    while counter < len(string):
        if string[counter].lower() not in vowels:
            newString = newString + string[counter]
        counter = counter + 1
    print(newString)
    
# Version 2     
def newRemoveVowel():
    string = input("Enter anything: ")
    vowels = ["a", "e", "i", "o", "u"]
    newString = ""
    for i in list(string):
        if i.lower() not in vowels:
            newString = newString + i
    print(newString)

# Version 3
def print_without_vowels():
    s = input("Enter a string: ")
    return "".join(i for i in s if i.lower() not in 'aeiou')

removeVowel()
newRemoveVowel()
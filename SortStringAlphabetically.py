string = input("Enter the string to be sorted  alphabetically :")

words = [word.lower() for word in string.split()]
words.sort()

print("The sorted words are :")
for word in words :
    print(word)
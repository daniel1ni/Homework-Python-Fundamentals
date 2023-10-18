sentence = input("Please enter a sentence: ")
sentence_caps = sentence.upper()
print(sentence_caps)

paragraph = input("Please enter a paragraph: ")
print(f"The paragraph has {len(paragraph.split())} words")

wordsORdigits = input("Please enter a string: ")
print(wordsORdigits.isnumeric())

stringToChange = input("Please enter a string: ")
newString = stringToChange.replace('a', 'o')
print(newString)

fullName = input("Please enter your full name: ")
listOfNames = fullName.split()
initialLetter = [word[0] for word in fullName.split()]
initials = ''.join(initialLetter)
print(f"Your initials are: {initials}")

lastStringForThisHomework = input("Please enter one more string: ")
listOfThisString = lastStringForThisHomework.split()
print(f"The length of your string is: {len(listOfThisString)}")
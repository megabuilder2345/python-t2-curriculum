# Problem 1
# Ask the user for a sentence.
# Use a dictionary to count how many times each word appears.
# Print the dictionary.
# (Hint: split the sentence)
dictionary={}
user_input1=input("gimme a sentence: ").split()
for i in range(len(user_input1)):
    if user_input1[i] in dictionary:
        dictionary[user_input1[i]] += 1
    else:
        dictionary[user_input1[i]] = 1
print(dictionary)



# Problem 2
# Create a dictionary called capitals with states and their capitals.
# Ask the user for a state and print the capital.
# If not found, print "No data".
dictionary2={"washington": "olympia","oregon": "something"}
user_input2=input("gimme a state: ")
if user_input2 in dictionary2:
    print(dictionary2[user_input2])
else:
    print("no data")


# Problem 3
# Ask the user for a word.
# Print the letter that appears the most times.
# If there is a tie, print any one of them.
dictionary3={}
user_input3=input("gimme a word: ")
for i in range(len(user_input3)):
    if user_input3[i] in dictionary3:
        dictionary3[user_input3[i]] += 1
    else:
        dictionary3[user_input3[i]] = 1
print(max(dictionary3, key=dictionary3.get))



# Problem 4
# Create a dictionary called inventory with items and their quantity.
# Ask the user what item they want to buy and how many.
# If there are enough, subtract from the inventory and print the new inventory.
# Otherwise print "Not enough".
dictionary4={"legos": 1000000,"fried ham": 3141592658}
user_input4=input("gimme a item: ")
user_input5=int(input("gimme a qty of items: "))
if user_input4 in dictionary4:
    if user_input5 > dictionary4[user_input4]:
        print("not enough")
    else:
        dictionary4[user_input4] -= user_input5
        print(dictionary4[user_input4])

    


# Problem 5
# Ask the user for two words.
# Use dictionaries to check if they are anagrams (same letters, different order).
# Print "Anagram" or "Not anagram".
dictionary6={}
dictionary7={}
user_input6=input("gimme a word: ")
user_input7=input("gimme a word: ")
for i in range(len(user_input6)):
    if user_input6[i] in dictionary6:
        dictionary6[user_input6[i]] += 1
    else:
        dictionary6[user_input6[i]] = 1
for i in range(len(user_input7)):
    if user_input7[i] in dictionary7:
        dictionary7[user_input7[i]] += 1
    else:
        dictionary7[user_input7[i]] = 1
if dictionary6==dictionary7:
    print("anagram")
else:
    print("not anagram")
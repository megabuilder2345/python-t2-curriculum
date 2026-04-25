# Problem 1
# Ask the user for a word.
# Print the word reversed using slicing.
user_input1=input("gimme a word or else: ")
the_reversed_word=""
for i in range(len(user_input1)):
    the_reversed_word += (user_input1[(i+1)*-1])
print(the_reversed_word)



# Problem 2
# Ask the user for a word and a letter.
# Print how many times the letter appears in the word (case-insensitive).
user_input2=input("gimme a word or else: ")
user_input3=input("gimme a letter or else: ")
da_ammount = 0
for i in range(len(user_input2)):
    if user_input2[i] == user_input3:
        da_ammount+=1
print(da_ammount)


# Problem 3
# Ask the user for an email address like "name@example.com".
# Print only the part after the @ (example: "example.com").
user_input4=input("gimme your email address or else: ")
da_ammount = 0
for i in range(len(user_input4)):
    if user_input4[i] == "@":
        examplecom=i+1
        print(user_input4[examplecom:])



# Problem 4
# Ask the user for a word.
# Print the word without the first and last character.
user_input5=input("gimme a word or else: ")
up2u=""
for i in range(len(user_input5)):
    if i!=0 and i!=(len(user_input5))-1:
        up2u+=(user_input5[i])
print(up2u)


# Problem 5
# Ask the user for a sentence.
# Print "Long" if the sentence has more than 20 characters (including spaces),
# otherwise print "Short"
user_input6=input("gimme a sentence or else: ")
length=len(user_input6)
if length>=20:
    print("long")
else:
    print("short")
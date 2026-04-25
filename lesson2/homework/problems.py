# Problem 1
# Ask the user for a sentence.
# Print how many words it has.
# (Hint: split the sentence by spaces)
user_input1=input("gimme a sentence or else: ")
aof=user_input1.split()
print(len(aof))

# Problem 2
# Ask the user for a word.
# Build a new string that turns every vowel into "*".
# Example: "hello" -> "h*ll*"
user_input2=input("gimme a word or else: ")
v=user_input2.replace("a","*")
v=v.replace("e","*")
v=v.replace("i","*")
v=v.replace("o","*")
v=v.replace("u","*")
print(v)


# Problem 3
# Ask the user for a word.
# Print the first index where the letter "a" appears.
# If there is no "a", print -1.
user_input3=input("gimme a word or else: ")
aa=user_input3.find("a")
print(aa)



# Problem 4
# Ask the user for two words.
# Print the longer word. If they are the same length, print "Tie".
user_input4=input("gimme a word or else: ")
user_input5=input("gimme a word or else: ")
if len(user_input4) >len(user_input5):
    print(user_input4)
elif len(user_input4) < len(user_input5):
    print(user_input5)
else:
    print("tie")

# Problem 5
# Ask the user for a phrase.
# Build a new string that keeps only letters (remove spaces and punctuation).
# For this problem, remove commas and periods too.
x=False
y=""
user_input6=input("gimme a phrase or else: ")
for i in range(len(user_input6)):
    x=user_input6[i].isalpha()
    if x==True:
        y+=user_input6[i]
print(y)
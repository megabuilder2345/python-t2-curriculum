text = " hello, World! "
print("raw text is:", text)

print("length:", len(text)) # include spaces

print(text.lower()) #makes every thing lowercase
print(text.upper()) #makes every thing uppercase
print(text.title()) #title case

print(text.strip()) #removes spaces on the left and right
print(text.strip().lower())

messege = "banana bread"
print("count of a:", messege.count("a"))
print("count of 'bread':", messege.count("apple")) # index of first match (or -1 if nothing is found)

print(messege.replace("banana", "pumpkin")) # replace first parameter with the second parameter
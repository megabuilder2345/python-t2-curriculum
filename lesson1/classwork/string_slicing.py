word="pineapple"
print("the word is: " + word)

#strings are 0 indexed (first character is index 0)
print("First letter:", word[0])
print("Second letter: ", word[1])

# negative indexing starts from the end
print("last letter:", word[-1])
print("second to last letter:", word[-2])

#slicing word[start:stop] ([start, stop])
print(word[0:4])
print(word[4:9])

#shortcuts:
print(word[:4]) # from the beginning
print(word[4:]) # from the end
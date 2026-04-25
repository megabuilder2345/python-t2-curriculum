# Problem 1
# Ask the user for a number n.
# Print all multiples of 3 from 0 to n (including n if it is a multiple of 3).
n=int(input("gimme a number"))
for i in range(0, n + 1, 3):
    print(i)


# Problem 2
# Ask the user for a number n.
# Print the square of every number from 1 to n (1*1, 2*2, ...).
n=int(input("gimme a number"))
for i in range(1, n + 1):
    print(i*i)


# Problem 3
# Ask the user for a number n.
# Print the numbers from n down to 0 (counting down).
n = int(input("Enter a number: "))

for i in range(n, -1, -1):
    print(i)


# Problem 4
# Ask the user for a word.
# Build a new string that repeats the word 5 times with spaces in between.
# Example: "hi hi hi hi hi"
word = input("Enter a word: ")
result = (word + " ") * 5
print(result.strip())


# Problem 5
# Ask the user for a number n.
# Print how many numbers from 1 to n are even.
n = int(input("Enter a number: "))
count = n // 2
print("There are", count, "even numbers.")
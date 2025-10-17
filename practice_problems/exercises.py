# for i in range(10):
#     if i == 3 or i == 4 or i == 5:
#         continue
#     print(i)


# n = 10
# print("Range: ", n)

# for i in range(n+1):
#     print(i)

#

#  ⚙️ Task: Count how many times a number appears

# Goal:
# Ask the user for:
# A list of numbers (comma-separated)
# A target number
# Then print how many times that target number appears in the list.

# Example:
# Input numbers: 2, 4, 2, 5, 2, 7
# Target: 2
# Output: The number 2 appears 3 times.

inp = input("Numbers: ").split()
inp = [int(n) for n in inp]

print(inp)



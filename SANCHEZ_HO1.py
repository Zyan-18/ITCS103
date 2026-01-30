def get_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average



word = input("Enter a word:")
l = len(word)

numbers = []
for a in range(l):
    num = int(input(f"Enter a number {a+1}:"))
    numbers.append(num)

average = get_average(numbers)

print(numbers)
print(f"The length of the word is {l}.")
print(f"The average of the numbers is {average}.")

if l < average:
    print(f"The length of the word '{word}' is less than the average.")
elif l == average:
    print(f"The length of the word '{word}' is equal to the average.")
else:
    print(f"The length of the word '{word}' is greater than the average.")
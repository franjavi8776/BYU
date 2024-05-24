list_of_numbers = []
#print(list_of_numbers)
total = 0

print("Enter a list of numbers, type 0 when finished.")

number = -1
while number != 0:
    number = int(input("Enter number: "))

    if number != 0:
        list_of_numbers.append(number)

for num in list_of_numbers:
    total += num
print(f"This suma is {total}")

average = total / len(list_of_numbers)
print(f"The average is {average}")

#largest = max(list_of_numbers)
#print(f"The largest number is {largest}")
largest = -1
for num in list_of_numbers:
    if num > largest:
        largest = num
print(f"The largest number is {largest}")

smallest = 9999
for num in list_of_numbers:
    if num < smallest and num > 0:
        smallest = num
print(f"The smallest number is {smallest}")

n = len(list_of_numbers)
for i in range(n):
    for j in range(0, n-i-1):
        if list_of_numbers[j] > list_of_numbers[j+1]:
            list_of_numbers[j], list_of_numbers[j+1] = list_of_numbers[j+1], list_of_numbers[j]
print(list_of_numbers)
for num in list_of_numbers:
    print(num)

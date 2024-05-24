numbers_list = []
total = 0
print("Enter a lis of numbers, type 0 when finished")

number = -1
while number != 0:
    number = int(input("Enter a number: "))

    if number != 0:
        numbers_list.append(number)

for num in numbers_list:
    total += num
print(f"The sum is: {total}")

average = total / len(numbers_list)
print(f"The average is: {average:.2f}")

largest = -1
for num in numbers_list:
    if num > largest:
        largest = num
print(f"The largest number is: {largest}")

smallest = 999999999
for num in numbers_list:
    if num > 0 and num < smallest:
        smallest = num
print(f"The smallest number is: {smallest}")

sorted_numbers = sorted(numbers_list)
print(f"The sorted list is:")
for num in sorted_numbers:
    print(num)

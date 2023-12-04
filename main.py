# alvin ocasio jr
# 12/3/2023
# Problem 1

while True:
    print("Infinite")
#problem 2

counter = 0
L = []

while counter <= 10:
    L.append(counter)
    counter += 1

print(L)
# Problem 3

number_list = []
total_sum = 0

while total_sum <= 100:
    user_input = int(input("Enter a number: "))
    number_list.append(user_input)
    total_sum = sum(number_list)

print("Sum of numbers is greater than 100.")
print("List of numbers:", number_list)
# Problem 4
counter = 0
tens = []

while counter <= 50:
    if counter % 10 == 0:
        tens.append(counter)
    counter += 1

print("List of numbers divisible by 10:", tens)



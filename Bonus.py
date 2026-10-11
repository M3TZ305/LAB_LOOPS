
user_input = input("Enter a positive integer: ")
n = int(user_input)

total_sum = 0

for i in range(1, n + 1):
    
    if i % 2 == 0:

        total_sum = total_sum + i

print("The sum of even numbers between 1 and", n, "is", total_sum)
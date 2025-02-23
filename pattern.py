#1st question
for i in range (5, 0, -1):
    print(" " * (5-i) + "*" *i)
    
#2nd question
def print_hollow_square(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

print_hollow_square(5)





#3rd question
def find_unique_number(numbers):
    unique_number = None
    for number in numbers:
        if numbers.count(number) == 1:
            unique_number = number
            break
    return unique_number
numbers = [1,1, 2, 2, 3,3, 4, 5, 5]
unique_number = find_unique_number(numbers)
print("The unique number is:", unique_number)

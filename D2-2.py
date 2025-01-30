#  ****
#   ***
#    **
#     *  USER INPUT


size = int(input("Enter the size of the square: "))

for i in range(size, 0, -1):
    print(" " * (size - i) + "*" * i)
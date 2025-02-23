arr = [0,1,1,0,1,2,1,2,0,0,0,1]
arr.sort() 
print(arr)



arr = [0,1,1,0,1,2,1,2,0,0,0,1]


arr.sort()


ones_twos = [x for x in arr if x != 0] 
zeros = [x for x in arr if x == 0]


result = ones_twos + zeros

print(result)



arr = [0,1,1,0,1,2,1,2,0,0,0,1]
arr.sort()


zeros_twos = [x for x in arr if x %2== 0] 
ones = [x for x in arr if x %2== 1]


result = ones + zeros_twos

print(result)
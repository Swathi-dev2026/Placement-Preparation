nums = [10,20,30,40,50]
print(nums[0])
print(nums[2])
print("="*50)
#Traversing an array
nums = [10,20,30,40,50]

for num in nums:
    print("Travering an array:",num)    #"Give me each value directly."

for i in range(len(nums)):
    print(nums[i])                       #"Give me each index."
print("="*50)

#Find the sum
nums = [10,20,30,40,50]
total = 0

for num in nums:
    total = total + num

print(total)
print("="*50)                            #Also called ACCUMULATOR PATTERN

#Practice

nums = [5, 10, 15, 20, 25]

total = 0

for num in nums:
    total = total + num
print(total)
print("="*50)

# LARGEST NUM
nums = [12, 45, 7, 89, 23, 56]
largest = nums[0]

for num in nums:
    if num > largest:
        largest = num
print(largest)
print("="*50)

# SMALLEST NUM
nums = [12, 45, 7, 89, 23, 56]
smallest = nums[0]

for num in nums:
    if num < smallest:
        smallest = num
print(smallest)
print("="*50)
print("="*50)

# COUNT REPEATED NUM IN ARRAY
nums = [10, 20, 10, 30, 20, 10, 40]
count = 0

for num in nums:
    if num == 10:
        count = count + 1
print(count)
nums = [10,20,30,40,50]
print(nums[0])
print(nums[2])
print("="*50)
#Traversing an array
nums = [10,20,30,40,50]

for num in nums:
    print(num)                           #"Give me each value directly."

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


# COUNT REPEATED NUM IN ARRAY
nums = [10, 20, 10, 30, 20, 10, 40]
count = 0

for num in nums:
    if num == 10:
        count = count + 1
print(count)
print("="*50)

#Frequency Counting
nums = [10, 20, 10, 30, 20, 10, 40]
frequency = {}
for num in nums:
   if num in frequency:
       frequency[num] += 1
   else:
       frequency[num] = 1
print(frequency)
print("="*50)
print("="*50)

#SORTING
#sort()
nums = [5, 2, 8, 1, 3]
nums.sort()               #Ascending
print(nums)
nums.sort(reverse=True)   #Descending
print(nums)  
print("="*50) 
#sorted()
nums = [5, 2, 8, 1, 3]
new_nums = sorted(nums)
print(new_nums)
print(nums)
print("="*50) 

#Practice 1
nums = [45, 12, 89, 3, 67, 21]
nums.sort()
print(nums)
print("="*50) 

#Practice 2
nums = [45, 12, 89, 3, 67, 21]
nums.sort(reverse = True)
print(nums)
print("="*50) 

#TIME COMPLEXITY


#SECOND LARGEST
nums = [12, 45, 7, 89, 23, 56]
largest = nums[0]
second_largest = nums[0]
for num in nums:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest:
        second_largest = num
print(second_largest)
print("="*50) 

#MISSING NUMBER
nums = [1,2,3,5]
n = len(nums) + 1
expected_sum = 0
for i in range(1, n+1):
   expected_sum = expected_sum + i


actual_sum = 0
for num in nums:
    actual_sum = actual_sum + num

missing = expected_sum - actual_sum
print(missing)
print("="*50) 
print("="*50) 



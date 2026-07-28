#SLIDING WINDOW 
print ("sliding window")
nums = [2, 4, 6, 8]
window_sum = nums[0] + nums[1]
window_sum = window_sum - nums[0] + nums[2]
window_sum = window_sum - nums[1] + nums[3]
print(window_sum)


print("Loop version: ")
nums = [2, 9, 9, 8]
window_sum = nums[0] + nums[1]
max_sum = window_sum
for i in range(2 , len(nums)):
    window_sum = window_sum - nums[i - 2] + nums[i]
    if window_sum > max_sum:
        max_sum = window_sum
print(max_sum)  
print("="*50)

#Fixed size sliding window
nums = [2, 9, 9, 8, 5, 7]
k = 3
window_sum = 0

for i in range(k):                   #Calculate the first window
    window_sum += nums[i]
max_sum = window_sum

for i in range(k, len(nums)):         #Slide the window
    window_sum = window_sum - nums[i - k] + nums[i]

    if window_sum > max_sum:
        max_sum = window_sum
print(max_sum)
print("="*50)

#Minimum sum of any subarray
nums = [1, 2, 3, 4, 5, 6]
k = 3
window_sum = 0

for i in range(k):
    window_sum += nums[i]

min_sum = window_sum

for i in range(k, len(nums)):
    window_sum = window_sum - nums[i- k] + nums[i]

    if window_sum < min_sum:
        min_sum = window_sum
print (min_sum)
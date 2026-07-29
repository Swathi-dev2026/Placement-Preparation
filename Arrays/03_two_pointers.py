
#TWO POINTER
nums = [1, 2, 4, 6, 8, 9]
target = 10

left = 0
right = len(nums) - 1
while left < right:
    current_sum = nums[left] + nums[right]
    if current_sum == target:
        print("found")
        break
    elif current_sum < target:
        left += 1
    else:
        right -= 1
      
        



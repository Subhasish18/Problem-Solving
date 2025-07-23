def twoSum_optimized(nums: list[int], target: int) -> list[int]:
    num_map = {} 
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
 
  
#brute force solution  
#def twoSum(nums: list[int], target: int) -> list[int]:   
   # n = len(nums)
    #for i in range(n):   
       # for j in range(i + 1, n):     
           # if nums[i] + nums[j] == target:
               # return [i, j]
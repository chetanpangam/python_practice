'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
'''

def threeSum(nums):
    result = []
    nums.sort()
    for first in range(len(nums) - 1):
        if first > 0 and nums[first] == nums[first-1]:
            continue
        second = first + 1
        last = len(nums) - 1

        while second < last:
            temp_sum = nums[first] + nums[second] + nums[last]
            if temp_sum == 0:
                result.append([nums[first], nums[second], nums[last]])
                second += 1
                while second < last and nums[second] == nums[second - 1]:
                    second += 1
            elif temp_sum > 0:
                last -= 1
            else:
                second += 1 

        
    return result

nums = [-1,0,1,2,-1,-4]
print(nums, threeSum(nums))

nums = [0,1,1]
print(nums, threeSum(nums))
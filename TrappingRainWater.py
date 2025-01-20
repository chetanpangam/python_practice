"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

 

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 
"""

def trappedWater(heights):
    trapped_water = 0
    N = len(heights)
    left = [0] * N
    right = [0] * N
    left[0], right[N-1] = heights[0], heights[N-1]
    j = N - 2
    for i in range(1, N):
        left[i] = max(left[i-1], heights[i])
        right[j] = max(right[j+1], heights[j])
        j -= 1

    for h in range(N):
        trapped_water += (min(left[h], right[h]) - heights[h])

    return trapped_water

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(height, trappedWater(height))

height = [4,2,0,3,2,5]
print(height, trappedWater(height))
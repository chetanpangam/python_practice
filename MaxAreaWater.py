'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two 
endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.
'''

def maxArea(heights):
    max_area = -float("inf")

    start = 0
    end = len(heights) - 1
    temp_height = 0
    while start < end:
        temp_height = min(heights[start], heights[end])
        curr_area = temp_height * (end - start)

        if curr_area > max_area:
            max_area = curr_area
            curr_area = 0
        
        if temp_height == heights[start]:
            start += 1
        else:
            end -= 1

    return max_area

heights = [1,8,6,2,5,4,8,3,7]
print(heights, maxArea(heights=heights))

heights = [1,1]
print(heights, maxArea(heights=heights))
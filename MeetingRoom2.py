"""
Given an array of meeting time interval objects consisting of start and end times 
[[start_1,end_1],[start_2,end_2],...] (start_i < end_i), 
find the minimum number of days required to schedule all meetings without any conflicts.

Example 1:

Input: intervals = [(0,40),(5,10),(15,20)]

Output: 2
Explanation:
day1: (0,40)
day2: (5,10),(15,20)

Example 2:

Input: intervals = [(4,9)]

Output: 1
"""

import heapq

def meetingRooms(intervals):

    intervals = sorted(intervals, key=lambda x:x[0])
    heap_list = []
    max_rooms = -float('INF')

    for i in range(len(intervals)):
        while heap_list and intervals[i][0] >= heap_list[0]:
            heapq.heappop(heap_list)
        
        heapq.heappush(heap_list, intervals[i][1])
        max_rooms = max(max_rooms, len(heap_list))

    return max_rooms

intervals = [(0,40),(5,10),(15,20)]
print(intervals, meetingRooms(intervals))

intervals = [(4,9), (9,13)]
print(intervals, meetingRooms(intervals))
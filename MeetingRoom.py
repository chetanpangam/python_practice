"""
Given an array of meeting time interval objects consisting of start and end times 
[[start_1,end_1],[start_2,end_2],...] (start_i < end_i), 
determine if a person could add all meetings to their schedule without any conflicts.

Example 1:

Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation:
(0,30) and (5,10) will conflict
(0,30) and (15,20) will conflict

Example 2:

Input: intervals = [(5,8),(9,15)]

Output: true

Note:
(0,8),(8,10) is not considered a conflict at 8

"""

def canAttend(intervals):

    intervals = sorted(intervals, key=lambda x:x[0])
    end_time = intervals[0][1]
    for i in range(1, len(intervals)):
        if end_time > intervals[i][0]:
            return False
        
        end_time = intervals[i][1]

    return True

intervals = [(0,30),(15,20),(5,10)]
print(intervals, canAttend(intervals))

intervals = [(5,8),(9,15)]
print(intervals, canAttend(intervals))
'''
N meetings in a room
medium
greedy, sorting, lambda, maximize
'''

'''
Problem Statement: There is one meeting room in a firm. You are given two arrays, start and end each of size N.For an index ‘i’, start[i] denotes the starting time of the ith meeting while end[i]  will denote the ending time of the ith meeting. Find the maximum number of meetings that can be accommodated if only one meeting can happen in the room at a  particular time. Print the order in which these meetings will be performed.

Example:

Input:  N = 6,  start[] = {1,3,0,5,8,5}, end[] =  {2,4,5,7,9,9}

Output: 1 2 4 5
'''

class Solution:
    def maxMeetings(self, start, end, n):
        # 1. Picking the meeting that starts early won't help as the earlierst meeting can finish at end of the day as well
        #. 2. Picking meeting that has shortest duration also won't help as the shortest meeting can be between two longer but independent meetings blocking both of them
        # For ex. 3-4 (60min) will block 1-3:30 (150min) and 3:45-5 (75mins)
        # 3. But picking meeting that ends earliest will always help pick max meetings
        
        # Step 1 - Make one list with start end time paired together in a tuple
        meetings = [(start[i], end[i]) for i in range(0, n, 1)]
        
        # Step 2 - Sort them on end time
        meetings.sort(key=lambda x: x[1], reverse=False)
        
        # Step 3 - Keep track of last meeting's end time and meeting count (additionally the meetings we pick)
        last_meeting = 0
        count = 0
        selected_meetings = []
        
        # Step 4 - Iterate over the meetings and pick the ones that we can
        for meeting in meetings:
            if meeting[0] >= last_meeting:
                selected_meetings.append(meeting)
                count += 1
                last_meeting = meeting[1]
        
        # Step 5 - Return the count or selected meetings list, whatever is asked for
        return count
    
    
sol = Solution()
start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 5, 7, 9, 9]
n = 6
answer = sol.maxMeetings(start, end, n)
print('Answer:', answer)
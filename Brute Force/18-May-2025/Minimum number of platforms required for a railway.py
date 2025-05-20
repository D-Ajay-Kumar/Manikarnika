'''
Minimum number of platforms required for a railway
medium
greedy, min_heap, sorting, lambda, minimize
'''

'''
Problem Statement: We are given two arrays that represent the arrival and departure times of trains that stop at the platform. We need to find the minimum number of platforms needed at the railway station so that no train has to wait.

Examples 1:

Input: N=6, 
arr[] = {9:00, 9:45, 9:55, 11:00, 15:00, 18:00} 
dep[] = {9:20, 12:00, 11:30, 11:50, 19:00, 20:00}

Output:3
'''

import heapq

class Solution:
    def maxPlatforms(self, arr, dep):
        # Number of trains
        n = len(arr)
        
        # 1. Iterate over the trains and keep the dep time in a min heap
        # 2. For every train check if arrival time is greater than departure time of train that leaves earliest (min heap)
        # 3. If yes, then no need of another platform, pop the departure time from min heap and push the departure time of current train
        # 4. If no, then increase platforms and just push the new departure time
        
        # Just in case arrival time is not sorted, combine arr and dep and sort based on arrival time
        trains = [(arr[i], dep[i]) for i in range(0, n, 1)]
        trains.sort(key=lambda x: x[0], reverse=False)
        
        min_heap = []
        platforms = 0
        
        for arrival, departure in trains:
            # Initial case where no train has arrived or departed
            if not min_heap:
                heapq.heappush(min_heap, departure)
                platforms += 1
                continue
            
            # If earliest departing train is departing after the arrival of next train we need 1 more platform
            if min_heap[0] > arrival:
                platforms += 1
                # Just push new train's departure as earliest departing hasn't departed yet
                heapq.heappush(min_heap, departure)
            # Else if earliest departing has departed then we have a platform empty
            else:
                # Pop the earliest departing
                heapq.heappop(min_heap)
                # Push the departure of current train
                heapq.heappush(min_heap, departure)
                
        return platforms
    
    
sol = Solution()
arr = [900, 945, 955, 1100, 1500, 1800]
dep = [920, 1200, 1130, 1150, 1900, 2000]
answer = sol.maxPlatforms(arr, dep)
print(answer)
            
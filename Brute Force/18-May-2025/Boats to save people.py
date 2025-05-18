'''
Boats to save people
greedy, two_pointer, minimize
'''

'''
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

 

Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
'''

from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        '''
        1. Sort the array and have a left and right pointer
        2. Since boat limit is only 2, check if both left and right can go together
        3. If not then send the heavier person and someone left of current right can pair with the person where left currently is pointing at
        4. Also we know that no person is going to be heavier than boat limit so can send the heavier
        '''
        left, right = 0, len(people)-1

        people.sort()
        boats = 0

        while left <= right:
            # If both can go send both
            if people[left]+people[right] <= limit:
                left += 1
                right -= 1
            # Otherwise just send the heavier person
            else:
                right -= 1
            boats += 1

        return boats
                
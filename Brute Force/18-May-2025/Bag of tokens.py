'''
Bag of tokens
greedy, two_pointers, maximize
'''

'''
You start with an initial power of power, an initial score of 0, and a bag of tokens given as an integer array tokens, where each tokens[i] denotes the value of tokeni.

Your goal is to maximize the total score by strategically playing these tokens. In one move, you can play an unplayed token in one of the two ways (but not both for the same token):

Face-up: If your current power is at least tokens[i], you may play tokeni, losing tokens[i] power and gaining 1 score.
Face-down: If your current score is at least 1, you may play tokeni, gaining tokens[i] power and losing 1 score.
Return the maximum possible score you can achieve after playing any number of tokens.

 

Example 1:

Input: tokens = [100], power = 50

Output: 0

Explanation: Since your score is 0 initially, you cannot play the token face-down. You also cannot play it face-up since your power (50) is less than tokens[0] (100).
'''

from typing import List

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        '''
        1. Sort the array and have left and right pointer
        2. Face up from the left if there's enough power
        3. If not enough power then face down from right (max token)
        4. If there is a middle element (odd length) either handle that separately or have a max_power and keep track of max power to return at the end
        '''
        left, right = 0, len(tokens)-1
        score = 0

        tokens.sort()

        # Handling middle element case separately
        while left < right:
            # Face up if there's enough power available
            if power >= tokens[left]:
                # Reduce power
                power -= tokens[left]
                # Increase score
                score += 1
                # Move towards right
                left += 1
                continue

            # Else if we have score then face down
            elif score > 0:
                # Increase power consuming the right-most (largest)
                power += tokens[right]
                # Reduce score
                score -= 1
                # Move to left
                right -= 1
                continue
            
            # If we reached here then we neither have enough power to face up not enough score to face down and increase power, so return the current score
            break
            
        # For the middle element in odd length tokens array
        # Consider it only if we can face up and increase score
        # Otherwise facing down and reducing score for it won't do any good as there's nothing to left to consume after increasing power by facing down
        if left == right and (power >= tokens[left]):
            score += 1
        
        return score

        
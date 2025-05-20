'''
Reverse words in a string
medium
string, split, reverse
'''

'''
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "  the sky is    blue  "
Output: "blue is sky the"
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        '''
        1. Split the words in the sentence and make a new list
        2. Reverse the list
        3. Return a string by joining all elements in the list with a space
        '''

        # Break the words in the sentence
        words = s.split()

        # Reverse the list
        words.reverse()

        # Return by joining with a space
        return ' '.join(words)
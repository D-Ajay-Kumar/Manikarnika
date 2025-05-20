'''
Break a palindrome
medium
string, slicing, greedy
'''

'''
Given a palindromic string of lowercase English letters palindrome, replace exactly one character with any lowercase English letter so that the resulting string is not a palindrome and that it is the lexicographically smallest one possible.

Return the resulting string. If there is no way to replace a character to make it not a palindrome, return an empty string.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, a has a character strictly smaller than the corresponding character in b. For example, "abcc" is lexicographically smaller than "abcd" because the first position they differ is at the fourth character, and 'c' is smaller than 'd'.

 

Example 1:

Input: palindrome = "abccba"
Output: "aaccba"
Explanation: There are many ways to make "abccba" not a palindrome, such as "zbccba", "aaccba", and "abacba".
Of all the ways, "aaccba" is the lexicographically smallest.
'''

class Solution:
    def breakPalindrome(self, palindrome):
        '''
        1. If length of plaindrome is 1 or less then we cannot do anything
        2. We only traverse half the palindrome i.e. len//2 because other half is same
        3. We will find the first non 'a' char and replace it with 'a'
        4. If we do not find any non 'a' char then all chars are a, so replace last char with 'b' and return
        5. We only traverse till floor of len/2 because in an odd len string there will be a middle char and no matter what we replace the middle char of a palindrome with it will always be a palindrome
        6. So we only traverse till mid-1 in odd length string and if no non 'a' char is found then we replace last with 'b'
        '''
        
        palindrome_len = len(palindrome)
        
        # If len is 1 or less then cannot do anything
        if palindrome_len <= 1:
            return ''
        
        # Iterate till floor of mid of the string
        for i in range(0, palindrome_len//2, 1):
            # If non 'a' char then replace with 'a' and return
            if palindrome[i] != 'a':
                return palindrome[0:i] + 'a' + palindrome[i+1:]
            
        # If we reach here then string is all aaa or there's only a middle char that is non 'a' so replace last with 'b'
        return palindrome[0:-1] + 'b'
            
        
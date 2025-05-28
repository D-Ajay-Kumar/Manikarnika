'''
Decode string
medium
stack, string 
'''

'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
'''

class Solution:
    def decodeString(self, s: str) -> str:
        '''
        1. Before solving outter brackets we need to solve inner brackets which can be nested in two ways
            a. [ [] [] [] ]    OR    b. [ [ [] ] ]
        2. So the problem can be broken into smaller sub-problems of same nature
        3. So we can either form a tree with sub-problems giving solution to parent or do it with an explicit stack
        4. Create a stack and keep appending till we see a closing brack
        5. Once a closing bracket is found, pop all chars and then all digits
        6. Multiply chars with digits and append back in, this will solve the innermost problem leaving only alphabets for outter bracket
        7. At the end just concatenate all elements left in stack and return
        '''
        stack = []

        # Iterate over each char
        for char in s:
            # As long as it is not a closing bracket, keep appending
            if char != ']':
                stack.append(char)
            # When we find a closing brack
            else:
                # Pop all alphabets till the opening bracket is found and there will always be one as inputs are valid and we are in this loop because we found a closing bracket
                substring = ''
                while stack[-1] != '[':
                    # Append to beginning of sub string to maintain order
                    substring = stack.pop() + substring
                
                # Pop once more to remove the opening bracket
                stack.pop()

                # Now pop all digits to make the multiplier
                multiplier = ''
                # Here we need to make sure stack is not empty and the char we are popping is a number
                while stack and stack[-1].isdigit():
                    # Again append to start to maintain order
                    multiplier = stack.pop() + multiplier

                # Multiply substring and multiplier and put back in stack for outter brackets (if any)
                stack.append(int(multiplier) * substring)

        # There can be multiple substrings left in stack for example for case -
        # k[] k[]
        # So combine everything and return one string
        return ''.join(stack)
                

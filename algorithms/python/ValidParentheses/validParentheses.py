# Method 1: using index find the max first, and then process

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {"]": "[", "}": "{", ")": "("}
        
        for char in s:
            if char in mapping: 
                # -> key of dict (containsKey)
                
                top_element = stack.pop() if stack else '#'
                # -> value of stack
                # check if stack is null
                
                if top_element != mapping[char]:
                    return False
            else:
                stack.append(char)
                # using append for push
                
        return not stack
        # check if the stack is empty
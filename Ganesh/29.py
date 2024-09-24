class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        dict = {")":"(","}":"{","]":"["}
        if len(s)%2 != 0:
            return False
        for i in s:
            if i not in dict.keys():
                stack.append(i)
            elif len(stack) != 0:
                if dict[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else: 
                return False
        return len(stack) == 0
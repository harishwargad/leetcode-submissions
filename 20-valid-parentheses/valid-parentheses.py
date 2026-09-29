class Solution:
    def isValid(self, s: str) -> bool:
        map_s = {")": "(", "}": "{", "]": "["}
        stack = []

        for i in s:
            if i in map_s.values():
                stack.append(i)
            elif i in map_s.keys():
                if stack and stack[-1] == map_s[i]:
                    stack.pop()
                else:
                    return False
            else:
                return False

        return not stack
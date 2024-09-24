class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = strs[0]
        for i in strs:
            while s and not i.startswith(s):
                s = s[:-1]
        return s
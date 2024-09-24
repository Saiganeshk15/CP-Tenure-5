class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dup, a = list(), set()
        for i in nums:
            if i in a:
                dup.append(i)
            else :
                a.add(i)
        return dup
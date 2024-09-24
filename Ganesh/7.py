class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev, k = nums[0], 1
        for i in range(1, len(nums)):
            if nums[i] == prev:
                prev = nums[i]
                nums[i] = "_"
                continue
            prev = nums[i]
        f_ = None
        for i in range(1, len(nums)):
            if f_ == None and nums[i] == "_":
                f_ = i
            if nums[i] != "_" and f_ != None:
                k += 1
                nums[f_], nums[i] = nums[i], nums[f_]
                f_ += 1
            elif nums[i] != "_":
                k += 1
        return k
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 1
        prev = nums[0]
        for n in nums:
            if n != prev:
                nums[k] = n
                k +=1
            else: 
                pass
            prev = n
        print(k)
        return k
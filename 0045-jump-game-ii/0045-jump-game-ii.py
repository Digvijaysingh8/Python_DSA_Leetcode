class Solution:
    def jump(self, nums: list[int]) -> int:
        j=0
        cur_end=0
        far=0

        for i in range(len(nums)-1):

            far=max(far,i+nums[i])

            if i == cur_end:
                j+=1
                cur_end=far
        return j        
        
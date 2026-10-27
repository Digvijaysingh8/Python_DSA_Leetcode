class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        a=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                l=j+1
                r=len(nums)-1

                while l<r:
                    k=nums[i]+nums[j]+nums[l]+nums[r]

                    if k==target:
                        c=sorted([nums[i],nums[j],nums[l],nums[r]])

                        if c not in a:
                            a.append(c)
                        l+=1
                        r-=1
                    elif k<target:
                        l+=1
                    else:
                        r-=1
        return a                        
    
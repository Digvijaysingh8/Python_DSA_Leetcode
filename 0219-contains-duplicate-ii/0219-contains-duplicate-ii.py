class Solution:
    def containsNearbyDuplicate(self, a: list[int], k: int) -> bool:
        d={}
        for i in range(len(a)):
            if a[i] not in d:
                d[a[i]]=i
            else:
                s=abs(d[a[i]]-i) 
                if s<=k:
                    return True
                d[a[i]]=i    
        else:
            return False          

                
        
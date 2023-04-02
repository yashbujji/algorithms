class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        merged = []
        i=0
        j=0

        while(i < len(nums1) and j < len(nums2)):
            if(nums1[i][0] == nums2[j][0]):
                merged.append([nums1[i][0],nums1[i][1]+nums2[j][1]])
                i=i+1
                j=j+1
            elif(nums1[i][0] < nums2[j][0]):
                merged.append(nums1[i])
                i+=1
            else:
                merged.append(nums2[j])
                j=j+1
        print(merged)
        if(i<len(nums1)):
           merged = merged + nums1[i:]
        if(j<len(nums2)):
            merged = merged + nums2[j:]
        
        return merged

    

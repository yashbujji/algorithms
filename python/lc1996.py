from sortedcontainers import SortedList
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: x[0]) # Step 1
        sl, ans, n, arr = SortedList(), 0, len(properties), []
        for i in range(n): # Step 2
            curr_att, curr_def = properties[i]
            if i == 0 or properties[i-1][0] == curr_att: # Step 3
                arr.append(curr_def)
            else: # Step 4
                for d in arr: 
                    sl.add(d)
                arr = [curr_def]
            idx = sl.bisect_left(curr_def) # Step 6 and 7
            ans += idx # Step 8
            if idx != 0:
                for _ in range(idx): sl.pop(0) # Step 8 removal part
        return ans
    #1996
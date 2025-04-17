# Observation 1: Anagrams must be of the same length
# Observation 2: Anagrams must contain the same set of characters
# Observation 3: Anagrams must contain the same frequency for each character

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map = {}
        for c in s:
            if c not in map:
                map[c] = 1
            else:
                map[c] = map[c] + 1
        
        map_2 = {}
        for c in t:
            if c not in map_2:
                map_2[c] = 1
            else:
                map_2[c] += 1
        
        for c in s:
            if c not in map or c not in map_2:
                return False
            if map_2[c] != map[c]:
                return False
        return True

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         c_s = Counter(s)
#         c_t = Counter(t)
# 
#         return c_s == c_t

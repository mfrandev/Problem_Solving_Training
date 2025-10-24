# Observation 1: Anagrams must be of the same length
# Observation 2: Anagrams must contain the same set of characters
# Observation 3: Anagrams must contain the same frequency for each character

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sm = {}
        tm = {}
        for i in range(len(s)):
            sm[s[i]] = 1 + sm.get(s[i], 0)
            tm[t[i]] = 1 + tm.get(t[i], 0)
        for s in sm:
            if s not in tm or sm[s] != tm[s]:
                return False
        return True

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         c_s = Counter(s)
#         c_t = Counter(t)
# 
#         return c_s == c_t

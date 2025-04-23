"""
# Observation 1: We need a good way to check if two string are anagrams.
# Observation 2: Our policy is for each window, if our strings are anagrams, we add the lefmost index to our solution.
# Observation 3: Only work to do is define how we check for anagrams and enforce our policy.
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_anagram_profile = Counter(p)
        s_anagram_profile = Counter(s[:len(p)])
        solution = []
        for i in range(len(s) - len(p) + 1):
            if p_anagram_profile == s_anagram_profile:
                solution.append(i)
            s_anagram_profile[s[i]] -= 1
            if s_anagram_profile[s[i]] == 0:
                del s_anagram_profile[s[i]]
            if i + len(p) < len(s):
                s_anagram_profile[s[i + len(p)]] += 1
        return solution
        

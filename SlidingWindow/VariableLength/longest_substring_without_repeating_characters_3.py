def lengthOfLongestSubstring(self, s):
        l = 0
        longest = 0
        my_set = set()
        for r in range(len(s)):
            while s[r] in my_set: # Invariant: if the "next" character is repeated, shrink the left side of the window until it is unique
                my_set.remove(s[l])
                l += 1
            my_set.add(s[r])
            longest = max(longest, r-l+1)
        return longest

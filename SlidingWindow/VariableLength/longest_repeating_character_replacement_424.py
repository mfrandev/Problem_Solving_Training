def characterReplacement(self, s: str, k: int) -> int:
    longest = 0
    l = 0
    freq = [0] * 26 # Map all upper-case letters to range [0-25]
    for r in range(len(s)):
        freq[ord(s[r]) - 65] += 1 # Increase freq of current char by 1 
        # Invariant is defined by "window_size - most_frequent_char > num_allowed_replacements"
        # This works because as the frequency counter is maintained, the "most frequent" character in a substring is generic and doesn't
        while (r-l+1) - max(freq) > k: # If this update means the invariant is violated
            freq[ord(s[l]) - 65] -= 1 # Shrink the window and decrement the frequency of the "removed" characters
            l += 1
        longest = max(longest, (r-l+1)) # Save the longest window size thus far
    return longest    
            

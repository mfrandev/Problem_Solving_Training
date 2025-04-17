def findRepeatedDnaSequences(self, s):
    ans = set()
    seen = set() 
    
    if len(s) < 10:
        return list(ans)
    
    curr_seq = s[0:10] # Save the initial sequence
    seen.add(curr_seq)
    for i in range(10, len(s)): # Iterate with a fixed length of 10
        curr_seq = curr_seq[1:] + s[i] # Get the current sequence
        if curr_seq in seen and not curr_seq in ans: # If a repeat sequence, mark it as such
            ans.add(curr_seq)
        else: # If not a repeat sequence, then mark it as seen
            seen.add(curr_seq)

    return list(ans)

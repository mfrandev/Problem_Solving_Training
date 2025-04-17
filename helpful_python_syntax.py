# 1. Create a frequency count (of characters)
# Counter can take a list, set, string, dictionary, and more as an argument
from collections import Counter
count_1 = Counter({'a', 'b', 'a', 'b', 'c', 'a'})

# 2. Sets 
set_1 = Set()
set_1.add('A')
is_in_set_1 = 'A' in set_1
set_1.remove('A')

# 3. Mapping ASCII character ranges into a set of indicies
freq = [0] * 26 # Makes an array of length 26 filled with '0'
ch = 'W' # Assume we only want to index uppercase letters
freq[ord(ch) - ord('A')] # 65 is 'A' and 97 is 'a'

# 4. Slice indexing
string_1 = "abcdefghijklmno"
print(string_1[:10]) # Will print "abcdefghij" so range [left:right)

# 5. Iterating over a dict
dict_1 = {'A': 1, 'B': 2, 'C': 3}
for key, value in dict_1.items() # Use dict.items() to iterate over all of the key value pairs
    print(key, value)
    
# 6. Change a set to a list
list(set_1) # Just use the list constructor

# 7. Represent infinities using
min_inf = float('-inf')
max_inf = float('inf')

# 8. Sort an array in-place
my_arr = [0, 4, 2, 1, 6, 2]
my_arr.sort()

# 9. Sort an array in-place in reverse order
my_arr.sort(reverse=True)

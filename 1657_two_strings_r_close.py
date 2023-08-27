from collections import Counter
# 1657. Determine if Two Strings Are Close
# https://leetcode.com/problems/determine-if-two-strings-are-close/description/

def close_strings(word1, word2):
     
    if len(word1)!= len(word2) or set(word1) != set(word2):
        return False

    c1 = Counter(word1)
    c2 = Counter(word2)


    return Counter(c1.values()) == Counter(c2.values())



'''
Input: word1 = "abc", word2 = "bca"
Output: true
'''
assert(close_strings("abc", "bca"))
'''
Input: word1 = "a", word2 = "aa"
Output: false
'''
assert(close_strings("a", "aa")==False)
'''
Input: word1 = "cabbba", word2 = "abbccc"
Output: true
'''
assert(close_strings("cabbba", "abbccc"))



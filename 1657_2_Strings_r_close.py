from collections import Counter
# 1657. Determine if Two Strings Are Close
# https://leetcode.com/problems/determine-if-two-strings-are-close/description/

def main():
    
    '''
    Input: word1 = "abc", word2 = "bca"
    Output: true
    '''
    print(close_Strings("abc", "bca"))

    '''
    Input: word1 = "a", word2 = "aa"
    Output: false
    '''
    print(close_Strings("a", "aa"))

    '''
    Input: word1 = "cabbba", word2 = "abbccc"
    Output: true
    '''
    print(close_Strings("cabbba", "abbccc"))

def close_Strings(word1, word2):
     
    if len(word1)!= len(word2) or set(word1) != set(word2):
        return False

    c1 = Counter(word1)
    c2 = Counter(word2)


    return Counter(c1.values()) == Counter(c2.values())

main()
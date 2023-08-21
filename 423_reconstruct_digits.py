
def originalDigits(s: str) -> str:
    num = [0]*10    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    num[0] = s.count('z')
    num[2] = s.count('w')
    num[4] = s.count('u')
    num[6] = s.count('x')
    num[8] = s.count('g')

    num[3] = s.count('h') - num[8]
    num[5] = s.count('f') - num[4]
    num[7] = s.count('s') - num [6]
    num[1] = s.count('o') - num[0] - num[2] - num[4]
    num[9] = s.count('i') - num[5] - num[6] - num[8]

    #result = ''
    #for i in range(10):
    #    result += str(i) * num[i]
    
    # Using comprehension
    result = ''.join(str(i) * num[i] for i in range(10))
    return result

assert(originalDigits('owoztneoer') == '012')
assert(originalDigits('fviefuro') == '45')
assert(originalDigits('xsi') == '6')
'''
https://leetcode.com/problems/reconstruct-original-digits-from-english/

423. Reconstruct Original Digits from English
Medium
757
2.5K
Companies
Given a string s containing an out-of-order English representation of digits 0-9, return the digits in ascending order.

 

Example 1:

Input: s = "owoztneoer"
Output: "012"
Example 2:

Input: s = "fviefuro"
Output: "45"
 

Constraints:

1 <= s.length <= 105
s[i] is one of the characters ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"].
s is guaranteed to be valid.
'''
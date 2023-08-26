def decode_string(s):
    stack = []

    for char in s:
        if char != "]":
            stack.append(char)
        else:
            text = getText(stack)
            count = getNumber(stack)
            stack.append(count * text)

    return "".join(stack)

# assume there is an end character in the stack
def getText(stack, end="["):
    text = ""
    char = stack.pop()
    while char != end:
        text = char + text
        char = stack.pop()

    return text

def getNumber(stack):
    digits = ""
    while stack and stack[-1].isdigit():
        digits = stack.pop() + digits

    return int(digits)


assert(decode_string("3[a]2[bc]") == "aaabcbc")
assert(decode_string("3[a2[c]]") == "accaccacc")
assert(decode_string("2[abc]3[cd]ef") == "abcabccdcdcdef")
assert(decode_string("12[a3[cd]]") 
       == "acdcdcdacdcdcdacdcdcdacdcdcdacdcdcdacdcdcdacdcdcdacdcdcdacdcdcdacdcdcdacdcdcdacdcdcd")
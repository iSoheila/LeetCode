def remove_stars(s):
    stack = []

    for c in s:
        if c == "*":
            stack.pop()
        else:
            stack.append(c)
    return "".join(stack)

print(remove_stars("leet**cod*e"))
assert(remove_stars("leet**cod*e") == "lecoe")
print(remove_stars("erase*****"))
assert(remove_stars("erase*****") == "")

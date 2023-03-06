"""Given a string of a-z, ( and ) characters, return a valid string with minimum number of ( and ) chars removed, so that
the brackets in the string is balanced.
"""


def min_balanced(s):
    # index of open brackets
    stack = []
    remove_index = set()

    # If we find an open bracket, push the index in the stack
    # If we find a closing bracket, pop the last index of the stack because this matches the closing bracket
    # If the stack is empty, the closing bracket needs to be removed.
    # At the end, if the stack is not empty, those open brackets need to be removed as well.
    for i, char in enumerate(s):
        if char == "(":
            stack.append(i)
        elif char == ")":
            if not stack:
                remove_index.add(i)
            else:
                stack.pop()

    remove_index.update(stack)
    s = list(s)
    return "".join([v for i, v in enumerate(s) if i not in remove_index])


def main():
    assert min_balanced("(abc(d)") in ["abc(d)", "(abcd)"]
    assert min_balanced("))((") == ""


if __name__ == "__main__":
    main()

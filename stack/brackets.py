"""Check if a string has balanced brackets."""


def is_matching(s):
    stack = []
    close_to_open = {"}": "{", ")": "(", "]": "["}
    for bracket in s:
        if bracket in close_to_open:
            if not stack:
                return False
            last = stack.pop()
            matched_open = close_to_open[bracket]
            if last != matched_open:
                return False
        else:
            stack.append(bracket)
    return len(stack) == 0


def main():
    assert is_matching("{[()]}")
    assert not is_matching("{[)]}")
    assert not is_matching("{([)]}")


if __name__ == "__main__":
    main()

def permutations(arr):
    """Calculate permutations of items on a list

    Base Case: n = 1 -> return the single item (as a list)
    General Case: for every item in list, remove it from the list. Get the permutations of this list recursively. Then
    append the removed item (arr[i]) to each of lists in the result.
    """
    n = len(arr)
    if n <= 1:
        return [arr]

    result = []
    for i in range(n):
        perms = permutations(arr[:i] + arr[i + 1:])
        for p in perms:
            result.append(p + [arr[i]])

    return result


def combinations(items, k):
    """Generate k-length combinations from items, with len(items) >= k."""
    output = []

    def helper(arr, start):
        if len(arr) == k:
            output.append(arr)
        else:
            for i in range(start, len(items)):
                helper(arr + [items[i]], i + 1)

    helper([], 0)
    return output

Monotonic stacks are used in several common patterns on LeetCode, particularly for problems involving the nearest greater or smaller elements. Here are some typical patterns:

### 1. Nearest Greater Element to the Right
**Problem:** For each element in an array, find the nearest greater element to its right.

**Example Problem:** "Next Greater Element I" (LeetCode 496)

**Pattern:**
- Iterate through the array from left to right.
- Maintain a decreasing stack (elements are pushed such that they form a decreasing sequence).
- For each element, pop elements from the stack until you find an element greater than the current element.
- The current element becomes the next greater element for the popped elements.

### 2. Nearest Greater Element to the Left
**Problem:** For each element in an array, find the nearest greater element to its left.

**Example Problem:** Similar to "Next Greater Element I", but considering the left side.

**Pattern:**
- Iterate through the array from right to left.
- Maintain a decreasing stack.
- For each element, pop elements from the stack until you find an element greater than the current element.
- The current element becomes the next greater element for the popped elements.

### 3. Nearest Smaller Element to the Right
**Problem:** For each element in an array, find the nearest smaller element to its right.

**Example Problem:** "132 Pattern" (LeetCode 456)

**Pattern:**
- Iterate through the array from left to right.
- Maintain an increasing stack (elements are pushed such that they form an increasing sequence).
- For each element, pop elements from the stack until you find an element smaller than the current element.
- The current element becomes the next smaller element for the popped elements.

### 4. Nearest Smaller Element to the Left
**Problem:** For each element in an array, find the nearest smaller element to its left.

**Example Problem:** "Largest Rectangle in Histogram" (LeetCode 84)

**Pattern:**
- Iterate through the array from right to left.
- Maintain an increasing stack.
- For each element, pop elements from the stack until you find an element smaller than the current element.
- The current element becomes the next smaller element for the popped elements.

### 5. Largest Rectangle in Histogram
**Problem:** Given an array representing the heights of bars in a histogram, find the area of the largest rectangle that can be formed.

**Example Problem:** "Largest Rectangle in Histogram" (LeetCode 84)

**Pattern:**
- Iterate through the heights of the histogram bars.
- Maintain a stack to store indices of the bars.
- When encountering a shorter bar, calculate the area of rectangles with heights of bars from the stack.
- Continue this until the stack is empty to ensure all possible rectangles are considered.

### 6. Trapping Rain Water
**Problem:** Given an array representing the height of bars, compute how much water can be trapped after raining.

**Example Problem:** "Trapping Rain Water" (LeetCode 42)

**Pattern:**
- Use two pointers or a stack to determine the left and right bounds for the trapped water.
- Maintain the stack to keep track of the bars.
- Calculate trapped water based on the heights of the bars and the current height.

### Example Code Snippets

#### Nearest Greater Element to the Right

```python
def next_greater_elements(arr):
    stack = []
    result = [-1] * len(arr)
    
    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            index = stack.pop()
            result[index] = arr[i]
        stack.append(i)
    
    return result

# Example usage
arr = [2, 1, 2, 4, 3]
print(next_greater_elements(arr))  # Output: [4, 2, 4, -1, -1]
```

#### Largest Rectangle in Histogram

```python
def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    heights.append(0)  # Add a sentinel value to pop all remaining bars in the stack
    
    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)
    
    heights.pop()  # Remove the sentinel value
    return max_area

# Example usage
heights = [2, 1, 5, 6, 2, 3]
print(largest_rectangle_area(heights))  # Output: 10
```

These patterns and examples cover some of the most common use cases for monotonic stacks in algorithmic problems.
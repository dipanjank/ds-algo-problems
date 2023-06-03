When to use Dynamic Programming
-------------------------------

* "overlapping subproblems": smaller versions of the original problem that are re-used multiple times.
* "optimal substructure": an optimal solution can be formed from optimal solutions to the overlapping subproblems 
of the original problem.

Greedy vs. DP
-------------
If a problem is asking for the maximum/minimum/longest/shortest of something, the number of ways to do something, 
or if it is possible to reach a certain point, it is probably greedy or DP. 
Although, in general, if the problem has constraints that cause decisions to affect other decisions, 
such as using one element prevents the usage of other elements, then we should consider using dynamic programming 
to solve the problem. These two characteristics can be used to identify if a problem should be solved with DP.

DP Framework
------------
1. A function or data structure that will compute/contain the answer to the problem for every given state.
2. Recurrence relation to transition between states.
3. Base cases.

Top-down vs Bottom Up
---------------------
* top-down DP uses recursion and memoization.
* Bottom up DP starts at the base cases, uses arrays, one dimension per state variable.

Multi-Dimensional DP
--------------------

The following are common things to look out for in DP problems that require a state variable:

* An index along some input. This is usually used if an input is given as an array or string. 
* A second index along some input. Sometimes, you need two index state variables, say i and j. In some questions, 
these variables represent the answer to the original problem if you considered the input starting at index 
i and ending at index j.
* Explicit numerical constraints given in the problem. For example, "you are only allowed to complete 
k transactions", or "you are allowed to break up to k obstacles", etc.
* Variables that describe statuses in a given state. For example "true if currently holding a key, false if not", 
"currently holding k packages" etc.

More pattern: https://leetcode.com/discuss/study-guide/1490172/Dynamic-programming-is-simple

How to convert top-down to bottom-up DP

* Create a k-dimensional DP array, where k is the number of arguments in your top-down solution. 
These are the parameters that define each DP state, and the length of each dimension in the DP array should be 
large enough to contain all possible values.
* Create a series of nested for-loops to iterate over all of the possible DP states. 
Make sure to adjust the direction of iteration according to the base cases, you want to visit the base case first. 
Sometimes this requires a little bit of critical thinking, but with practice selecting the correct order in which 
to iterate over the states will become easier.
* Copy and paste everything from your top-down recursive function into the innermost for-loop.
Anywhere you have return some_value change that to dp[i][j][k] = some_value and then continue. Here, i, j, and k are 
just the variables from your for loop that define the current dp state.
* Change all calls to the recursive function from dp(0, 0, 0) to dp[0][0][0] (be mindful when you create your DP array, 
it makes things easier if you have each dimension be in the same order as your variables in the original 
recursive function, i.e. if your top down approach was dp(index, score) you want your array to be dp[index][score])
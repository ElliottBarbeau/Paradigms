def fibonacci_recursion(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)

#top-down
def fibonacci_memoization(n, table):
    if n not in table:
        table[n] = fibonacci_memoization(n-1, table) + fibonacci_memoization(n-2, table)
    
    return table[n]

#tbottom-up, O(n) time and space
def fibonacci_tabulation(n, table):
    for i in range(2, n + 1):
        table[i] = table[i-1] + table[i-2]

    return table[n]

t = {0:1, 1:1}
print(fibonacci_memoization(10, t))
print(fibonacci_tabulation(100000, t))
# Example 1 - O(1)

for i in range(100):
    print(i)

# Time Complexity: O(1)
# Space Complexity: O(1)

# Example 2 - O(n)

def display(n):
    for i in range(n):
        print(i)

# Time Complexity: O(n)
# Space Complexity: O(1)

# Example 3 - O(n)

def build_list(n):
    nums = []

    for i in range(n):
        nums.append(i)

    return nums

# Time Complexity: O(n)
# Space Complexity: O(n)

# Example 4 - O(n²)
'''
for i in range(n):
    for j in range(n):
        print(i, j)

# Time Complexity: O(n²)
# Space Complexity: O(1)
'''
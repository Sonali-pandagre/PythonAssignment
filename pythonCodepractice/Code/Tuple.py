"""
add two tuple and output should be (4,6)
"""

t1 = (1, 2)
t2 = (3, 4)

result = tuple(map(sum, zip(t1, t2)))

print(result)


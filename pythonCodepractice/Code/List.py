""""x=[2,7,3,99,12]
output should be [12,7,3,99,2] swap first last element in the list without using temporary variable"""

x=[2,7,3,99,12]
x[0],x[-1]=x[-1],x[0]
print(x)

def print_pattern(rows):
    current_no=1
    for i in range(1, rows+1):
       for j in range(1, i+1):
            print(current_no, end=" ")
            current_no+=1
       print()
print_pattern(4)

def count_elements(input_list):
    element_counts ={}
    for element in input_list:
          element_counts[element] = element_counts.get(element, 0) + 1
    return element_counts
input_list = [1, 2, 1, 2, 32, 1, 2, 3, 1, 23, 3, 5, 5]
output_dict = count_elements(input_list)
print(output_dict)

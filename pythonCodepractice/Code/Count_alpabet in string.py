def count_alphabets(input_string):

    alphabet_counts = {}
    for char in input_string:
        if char.isalpha():

            char = char.upper()

            alphabet_counts[char] = alphabet_counts.get(char, 0) + 1
    output_string = ""
    for char, count in alphabet_counts.items():
           output_string += f"{count}{count}"

    return output_string


input_str= "Telephone"
output_str= count_alphabets(input_str)
print(output_str)



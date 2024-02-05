# Write a function, which returns odd index value from given string append those characters to list
# Ex: Capgemini
def odd(input_string):
    result_list = [input_string[i] for i in range(1, len(input_string), 2)]
    return result_list

given_string = "Capgemini"
result_characters = odd(given_string)
print(f"Characters at odd indices in '{given_string}': {result_characters}")

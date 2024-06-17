def count_numbers_and_strings(data_structure):
    total_numbers = 0

    if isinstance(data_structure, (int, float)):
        total_numbers += data_structure
    elif isinstance(data_structure, str):
        total_numbers += len(data_structure)
    elif isinstance(data_structure, list) or isinstance(data_structure, tuple) or isinstance(data_structure, set):
        for item in data_structure:
            total_numbers += count_numbers_and_strings(item)
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            total_numbers += count_numbers_and_strings(key)
            total_numbers += count_numbers_and_strings(value)

    return total_numbers


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(count_numbers_and_strings(data_structure))
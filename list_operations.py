def list_operations(numbers):
    list_sum = sum(numbers)
    average = list_sum / len(numbers) if len(numbers) > 0 else 0
    max_value = max(numbers) if numbers else None
    return list_sum, average, max_value

def reverse_list(my_list):
    return my_list[::-1]


numbers = [1, 5, 3, 8, 2]
print(list_operations(numbers))  # Output: (19, 3.8, 8)

my_list = ['a', 'b', 'c']
print(reverse_list(my_list))  # Output: ['c', 'b', 'a']

def create_unique_sequence(numbers):
    sorted_numbers = sorted(numbers)
    sequence = [sorted_numbers[i] + i for i in range(len(sorted_numbers))]
    return sequence

numbers = [15, 8, 6, 2,11,22]
unique_sequence = create_unique_sequence(numbers)
print("Unique sequence:", unique_sequence)
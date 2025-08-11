def data_cleaner(num_str):
    # Convert the string to int, which automatically removes leading zeros
    return int(num_str)

# Example usage:
input_str = "0123"
output_int = data_cleaner(input_str)
print(output_int)  # Output: 123

def right_circular_shift(state):
    # Convert hex strings to integers
    state_matrix = [[hex_to_int(cell) for cell in row] for row in state]

    for i in range(1, 4):
        # Extract the current row
        current_row = state_matrix[i]
        # Perform the right circular shift
        shifted_row = current_row[-i:] + current_row[:-i]
        # Update the state with the shifted row
        state_matrix[i] = shifted_row

    # Convert back to hex strings
    output_matrix = [[int_to_hex(cell) for cell in row] for row in state_matrix]

    return output_matrix

def hex_to_int(hex_value):
    return int(hex_value, 16)

def int_to_hex(int_value):
    return hex(int_value)[2:].upper().zfill(2)

# Example usage:
state_matrix = [
    ['53', '65', '76', '89'],
    ['0A', '1B', '2C', '3D'],
    ['4E', '5F', '70', '81'],
    ['92', 'A3', 'B4', 'C5']
]

right_shifted_state = right_circular_shift(state_matrix)
print("After right circular shift:")
for row in right_shifted_state:
    print(row)

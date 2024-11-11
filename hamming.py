def calculate_parity_bits(data):
    m = len(data)
    r = 0

    # Calculate the number of parity bits needed
    while (2 ** r) < (m + r + 1):
        r += 1

    # Create an array to hold the encoded data
    encoded_data = ['0'] * (m + r)

    # Place the data bits in the encoded data array
    j = 0
    for i in range(1, m + r + 1):
        if (i & (i - 1)) == 0:  # If i is a power of 2
            continue
        encoded_data[i - 1] = data[j]
        j += 1

    # Calculate parity bits
    for i in range(r):
        parity_position = 2 ** i
        parity_value = 0
        for j in range(1, m + r + 1):
            if j & parity_position == parity_position:
                parity_value ^= int(encoded_data[j - 1])
        encoded_data[parity_position - 1] = str(parity_value)

    return ''.join(encoded_data)

def decode_hamming(encoded_data):
    m = len(encoded_data)
    r = 0

    # Calculate the number of parity bits
    while (2 ** r) < m:
        r += 1

    # Check for errors
    error_position = 0
    for i in range(r):
        parity_position = 2 ** i
        parity_value = 0
        for j in range(1, m + 1):
            if j & parity_position == parity_position:
                parity_value ^= int(encoded_data[j - 1])
        if parity_value != 0:
            error_position += parity_position

    if error_position != 0:
        print(f"Error detected at position: {error_position}")
        # Correct the error
        encoded_data = list(encoded_data)
        encoded_data[error_position - 1] = '1' if encoded_data[error_position - 1] == '0' else '0'
        encoded_data = ''.join(encoded_data)
        print(f"Corrected data: {encoded_data}")

    return encoded_data

# Example usage of Hamming Code
if __name__ == "__main__":
    data = input("Enter the data bits (e.g., 1011): ")
    encoded = calculate_parity_bits(data)
    print(f"Encoded data with Hamming Code: {encoded}")

    # Simulate an error for testing
    error_index = int(input("Enter the position of the bit to flip (1-indexed, 0 for no error): "))
    if error_index > 0:
        encoded = list(encoded)
        encoded[error_index - 1] = '1' if encoded[error_index - 1] == '0' else '0'
        encoded = ''.join(encoded)

    print(f"Received data: {encoded}")
    decoded = decode_hamming(encoded)
def xor(dividend, divisor):
    """Perform XOR operation between two binary strings."""
    result = []
    for i in range(len(divisor)):
        result.append(str(int(dividend[i]) ^ int(divisor[i])))
    return ''.join(result)

def crc(data, divisor):
    """Calculate the CRC remainder for the given data and divisor."""
    # Append zeros to the data
    data = data + '0' * (len(divisor) - 1)
    n = len(divisor)
    
    # Perform the division
    remainder = data[:n]
    for i in range(len(data) - len(divisor) + 1):
        if remainder[0] == '1':
            remainder = xor(remainder, divisor) + data[n + i]
        else:
            remainder = remainder[1:] + data[n + i] if (n + i) < len(data) else remainder[1:] + '0'
    
    return remainder

def encode_crc(data, divisor):
    """Encode the data using CRC."""
    remainder = crc(data, divisor)
    # The codeword is the original data plus the CRC remainder
    codeword = data + remainder
    return codeword

def check_crc(received_data, divisor):
    """Check if the received data has errors using CRC."""
    remainder = crc(received_data, divisor)
    return remainder == '0' * (len(divisor) - 1)

# Example usage
if __name__ == "__main__":
    data = input("Enter the data bits (e.g., 1101011011): ")
    divisor = input("Enter the divisor (e.g., 1011): ")

    # Encode the data
    codeword = encode_crc(data, divisor)
    print(f"Encoded data (codeword): {codeword}")

    # Simulate receiving the data (you can introduce an error here)
    received_data = input("Enter the received data (codeword): ")

    # Check for errors
    if check_crc(received_data, divisor):
        print("No error detected in the received data.")
    else:
        print("Error detected in the received data.")
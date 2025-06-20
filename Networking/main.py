def calculate_parity_bits(data):
    n = len(data)
    r = 0
    while (2**r) < (n + r + 1):
        r += 1
    return r

def position_parity_bits(data, r):
    j = 0
    k = 0
    m = len(data)
    n = m + r
    result = ''
    for i in range(1, n + 1):
        if i == (2**j):
            result += '0'
            j += 1
        else:
            result += data[k]
            k += 1
    return result

def calculate_parity_values(arr, r):
    n = len(arr)
    for i in range(r):
        x = (2**i)
        parity = 0
        for j in range(1, n + 1):
            if j & x == x:
                parity ^= int(arr[j - 1])
        arr = arr[:x-1] + str(parity) + arr[x:]
    return arr

def detect_and_correct(arr, r):
    n = len(arr)
    error_pos = 0
    for i in range(r):
        x = (2**i)
        parity = 0
        for j in range(1, n + 1):
            if j & x == x:
                parity ^= int(arr[j - 1])
        error_pos += x if parity != 0 else 0
    
    if error_pos != 0:
        arr = list(arr)
        arr[error_pos - 1] = '0' if arr[error_pos - 1] == '1' else '1'
        arr = ''.join(arr)
    
    return arr

def hamming_code(data):
    r = calculate_parity_bits(data)
    arr = position_parity_bits(data, r)
    arr = calculate_parity_values(arr, r)
    return arr

def main():
    data = input("Enter binary data: ")
    encoded_data = hamming_code(data)
    print(f"Encoded data with parity bits: {encoded_data}")
    
    introduce_error = input("Do you want to introduce an error? (yes/no): ").lower()
    if introduce_error == 'yes':
        error_bit = int(input("Enter the bit position to flip (1-indexed): ")) - 1
        encoded_data = list(encoded_data)
        encoded_data[error_bit] = '0' if encoded_data[error_bit] == '1' else '1'
        encoded_data = ''.join(encoded_data)
        print(f"Encoded data with an error introduced: {encoded_data}")
    
    corrected_data = detect_and_correct(encoded_data, calculate_parity_bits(data))
    print(f"Corrected data: {corrected_data}")

if __name__ == "__main__":
    main()

# KEY GENERATION PROCESS
# P10: 3 5 2 7 4 10 1 9 8 6
# P8: 6 3 7 4 8 5 10 9

# Key -> P10 -> LCS by 1 -> P8 -> Key 1
# Result of LCS by 1 -> LCS by 2 -> P8 -> Key 2


# ENCRYPTION & DECRYPTION
# PP: 2 6 3 1 4 8 5 7
# EP: 4 1 2 3 2 3 4 1
''' S0: [1 0 3 2
         3 2 1 0
         0 2 1 3
         3 1 3 2] '''
''' S1: [0 1 2 3
         2 0 1 3
         3 0 1 0        
         2 1 0 3] '''
# P4: 2 4 3 1
# IPP: 4 1 3 5 7 2 8 6

# ENCRYPTION
# PP -> Divide into L(4bits) & R(4bits)
# EP1 on R -> XOR with K1 -> Divide into L1(4bits) & R1(4bits) -> Use S-box to get 4 bit Result (center == col) -> P4 -> XOR with L -> Combine with R -> Swap bits
# Divide into L(4bits) & R(4bits) -> EP2 on R -> XOR with K2 -> Divide into L2(4bits) & R2(4bits) -> Use S-box to get 4 bit Result (center == col) -> P4 
# P4 XOR with L -> Combine with R -> IPP

# DECRYPTION
# PP -> Divide into L(4bits) & R(4bits)
# EP1 on R -> XOR with K2 -> Divide into L1(4bits) & R1(4bits) -> Use S-box to get 4 bit Result (center == col) -> P4 -> XOR with L -> Combine with R -> Swap bits
# Divide into L(4bits) & R(4bits) -> EP2 on R -> XOR with K1 -> Divide into L2(4bits) & R2(4bits) -> Use S-box to get 4 bit Result (center == col) -> P4 
# P4 XOR with L -> Combine with R -> IPP


# DATA VALIDATION
''' Input: 
8 bit PT/CT -> 8 bits, only 0s and 1s; 00 to FF
10 bit KEY -> 10 bits, only 0s and 1s; 000 to 3FF
'''

# For SDES
def s_des():
    print("Encrypt or Decrypt")
    print("1. Encrypt")
    print("2. Decrypt")
    ch = int(input("Enter your choice: ").strip())

    print("Enter the Key Value: ")
    key = input().strip()
    
    if key_checker(key) == True:
        if len(key) <= 3:
            key = hex_to_bin(key,10)
    else:
        print("Wrong Key Value!\n")
        return
    
    keys = key_generation(key)

    if ch == 1:
        print("Enter the PlainText: ")
        pt = input().strip()
        if checker(pt) == True:
            if len(pt) <= 2:
                pt = hex_to_bin(pt, 8)
        else:
            print("Wrong Value!\n")

        ct = enc_dec(pt,keys[0],keys[1])
        print("The Cipher Text is:",ct,"\n")
    else:
        print("Enter the CipherText: ")
        ct = input().strip()
        if checker(ct) == True:
            if len(ct) <= 2:
                ct = hex_to_bin(ct, 8)
        else:
            print("Wrong Value!\n")
        
        pt = enc_dec(ct,keys[1],keys[0])
        print("The Plain Text is:",pt,"\n")

def enc_dec(text, k1, k2):
    PP = [2, 6, 3, 1, 4, 8, 5, 7]
    IPP = [4, 1, 3, 5, 7, 2, 8, 6]

    pp_text = ''
    for i in PP:
        pp_text += text[i - 1]
    print("After PP:",pp_text,'\n')
    
    l = '' + pp_text[:4]
    r = '' + pp_text[4:]

    val1 = round(l,r,k1.strip())
    print("Before Swap:",val1,'\n')

    val1 = swap(val1)
    print("After Swap:",val1,'\n')

    l = '' + val1[:4]
    r = '' + val1[4:]
    
    val2 = round(l,r,k2.strip())
    print("Before IPP:",val2,'\n')

    final = ''
    for i in IPP:
        final += val2[i -1]
    
    return final
    

def swap(str):

    # Swap the first 4 bits with the last 4 bits
    swapped_str = str[4:] + str[:4]

    return swapped_str

def round(l, r, k):
    
    EP = [4, 1, 2, 3, 2, 3, 4, 1]
    P4 = [2, 4, 3, 1]

    ep_r = ''
    for i in EP:
        ep_r += r[i - 1]
    print("After EP:",ep_r,'\n')
    
    # Doing XOR
    res1 = xor(ep_r,k)
    print("After XOR:",res1,'\n')

    #S-BOX
    res2 = sbox(res1[:4],res1[4:])
    print("After S-box:",res2,'\n')

    after_p4 = ''
    for i in P4:
        after_p4 += res2[i - 1]
    print("After P4:",after_p4,'\n')
    
    res3 = xor(after_p4,l)
    print("After XOR:",res3,'\n')

    res = res3 + r

    return res
    

def sbox(l,r):
    S0 = [[1, 0, 3, 2],
         [3, 2, 1, 0],
         [0, 2, 1, 3],
         [3, 1, 3, 2]]
    S1 = [[0, 1, 2, 3],
         [2, 0, 1, 3],
         [3, 0, 1, 0],        
         [2, 1, 0, 3]]
    
    res = ''
    # For L
    col = bin_to_dec(l[1:3])
    row = bin_to_dec(l[0]+l[3])
    res += dec_to_bin(S0[row][col])
    # For R
    col = bin_to_dec(r[1:3])
    row = bin_to_dec(r[0]+r[3])
    res += dec_to_bin(S1[row][col])

    #print(res)
    return res
    
def xor(str1, str2):
    #print(str1,'\n',str2,'\n')
    ans = ''
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            ans += '0'
        else:
            ans += '1'
    return ans

#To Validate the Key
def key_checker(key):
    length = len(key)

    if length == 10 and is_correct(key, 2) == True:
            return True
    elif length <= 3 and is_correct(key, 16) == True:
            if int(key, 16) <= 0x3FF:
                return True
    else:
        print("Wrong Key Value!\n")
        return False

# KEY GENERATION PROCESS
def key_generation(key):
    P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    P8 = [6, 3, 7, 4, 8, 5, 10, 9]

    temp_key = ''
    for i in P10:
        temp_key += key[i - 1]
    print("Value After P10:",temp_key,'\n')
    
    temp_key = left_circular_shift(temp_key, 1)
    print("Value After LCS-1:",temp_key,'\n')
    
    key1 = ' '
    for i in P8:
        key1 += temp_key[i - 1]
    print("KEY 1:",key1,'\n')
    
    temp_key = left_circular_shift(temp_key, 2)
    print("Value After LCS - 2:",temp_key,'\n')
    
    key2 = ' '
    for i in P8:
        key2 += temp_key[i - 1]
    print("KEY 2:",key2,'\n')

    return ([key1,key2])


def left_circular_shift(binary_number, shift_amount):

    l = binary_number[:5]
    r = binary_number[5:]

    # Perform the left circular shift
    shifted_number = ''
    shifted_number += l[shift_amount:] + l[:shift_amount]
    shifted_number += r[shift_amount:] + r[:shift_amount]

    return shifted_number

# Validate PT or CT
def checker(str):
    length = len(str)
    if length == 8 and is_correct(str,2) == True:
            return True
    elif length <= 2 and is_correct(str,16) == True:
            return True
    else:
        print("Wrong Value!\n")
        return False

def is_correct(str, n):
    try:
        # Try to convert the input to an integer with base n
        int(str, n)
        return True
    except:
        return False  

def hex_to_bin(str, l):
    # Define a dictionary to map each hexadecimal digit to its 4-bit binary representation
    hex_to_bin_mapping = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
                          '4': '0100', '5': '0101', '6': '0110', '7': '0111',
                          '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
                          'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

    # Convert each hexadecimal digit to its binary representation
    binary_representation = ''.join(hex_to_bin_mapping[digit] for digit in str)

    # Calculate the number of leading zeros needed
    num_zeros = l - len(binary_representation)

    # Add leading zeros to the binary string
    binary_result = '0' * num_zeros + binary_representation

    return binary_result

def bin_to_dec(binary_str):

    decimal_number = 0
    power = len(binary_str) - 1

    for bit in binary_str:
        decimal_number += int(bit) * (2 ** power)
        power -= 1

    return decimal_number

def dec_to_bin(decimal_number):
    if decimal_number == 0:
        return "0"

    binary_string = ""
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_string = str(remainder) + binary_string
        decimal_number //= 2

    return binary_string

def aes():
    print()


while True:
    print("Choose a Block Cipher")
    print("1. S-DES")
    print("2. AES")
    print("3. Exit")
    print("\nEnter your choice: ")
    choice = int(input().strip())

    if choice == 1:
        s_des()
    elif choice == 2:
        aes() 
    else:
        break



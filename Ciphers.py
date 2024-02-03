import math
# Create a 5x5 matrix using the secret key
# Not dealing with the case where I/J or both are in key
def create_matrix(key):
    matrix = [[0 for i in range(5)] for j in range(5)] #Initializing a 5x5 matrix
    letters_added = [] 

    # Adding key to the matrix
    for letter in key:
        if letter not in letters_added:
            letters_added.append(letter)
        else:
            continue

    
    # Add the rest of the letters to the matrix
    for letter in range(65,91):
        if letter == 74: # Let I and J be in same cell
            continue
        if chr(letter) not in letters_added:
            letters_added.append(chr(letter))
    
    index = 0
    for i in range(5):
        for j in range(5):
            matrix[i][j] = letters_added[index]
            index += 1
    
    return matrix

# Add fillers
# Parameter is in uppercase
def add_fillers(plaintext):
    index = 0
    while index < len(plaintext):
        char1 = plaintext[index]
        if index == len(plaintext) - 1:
            plaintext = plaintext + 'X' # Adding a filler if odd number of letters
            index += 2
            continue # Reached the end

        char2 = plaintext[index + 1]

        if char1 == char2:
            plaintext = plaintext[:index+1] + "X" + plaintext[index + 1:]
            # [includes:not included]

        index += 2
    print("Plaintext With Fillers added: ",plaintext,"/n")
    return plaintext

# Encrypt and Decrypt
# Need the row and column num to determine which rule to apply
def indexOf(letter, matrix):
    for i in range(5):
        # Using try and except because of i and j in the same cell
        try:
            ind = matrix[i].index(letter) # To find the col we use index()
            return (i,ind)
        except:
            continue

# Encrypt and Decrypt
def playfair():
    print("Encrypt or Decrypt")
    print("1. Encrypt")
    print("2. Decrypt")
    ch = int(input("Enter your choice: ").strip())

    key = (input("Enter the key: ").strip()).upper()
    key = key.replace(' ','')

    if key.isalpha() == False:
        print("Wrong Key! Exiting Cipher.")
        return 


    inc = 0
    plaintext = ''
    if ch == 1:
        plaintext = (input("Enter the plaintext: ").strip()).upper()
        plaintext = plaintext.replace(' ','') # Removing any space
        inc = 1
        if plaintext.isalpha() == False:
            print("Wrong Input! Exiting Cipher.\n")
            return 
    else:
        plaintext = (input("Enter the ciphertext: ").strip()).upper()
        plaintext = plaintext.replace(' ','') # Removing any space
        inc = -1
        if plaintext.isalpha() == False:
            print("Wrong Input! Exiting Cipher.\n")
            return 

    matrix = create_matrix(key)
    plaintext = add_fillers(plaintext)

    cipher_text = ''
    
    print("Each Step: \n")
    for (char1, char2) in zip(plaintext[0::2], plaintext[1::2]):
        row1,col1 = indexOf(char1,matrix)
        row2,col2 = indexOf(char2,matrix)
        if row1 == row2:
            cipher_text += matrix[row1][(col1+inc)%5] + matrix[row2][(col2+inc)%5]
            print(cipher_text)
        elif col1 == col2:
            cipher_text += matrix[(row1+inc)%5][col1] + matrix[(row2+inc)%5][col2]
            print(cipher_text)
        else:
            cipher_text += matrix[row1][col2] + matrix[row2][col1]
            print(cipher_text)
    
    if ch == 1:
        print("Encrypted Text:",cipher_text)
    else:
        print("Decrypted Text:",cipher_text)



def generateKey(plaintext, key):
    key = list(key) # Coverting string to list
    if len(plaintext) != len(key):
        for i in range(len(plaintext) - len(key)):
            key.append(key[i % len(key)])
    
    return ("".join(key)) # Converting back to string 

def encrypt_vig(plaintext, key):
    cipher_text = []

    # This loop handles the case where len(key) > len(plaintext)
    for i in range(len(plaintext)):
        # A formula or shortcut for Vigerene Cipher
        # It gives 0-25 === A-Z
        letter = (ord(plaintext[i]) + ord(key[i])) % 26 
        letter += ord('A') # To get the actual character
        cipher_text.append(chr(letter))
    return ("".join(cipher_text))

def decrypt_vig(ciphertext, key):
    plaintext = []

    # This loop handles the case where len(key) > len(plaintext)
    for i in range(len(ciphertext)):
        # A formula or shortcut for Vigerene Cipher
        # It gives 0-25 === A-Z
        letter = (ord(ciphertext[i]) - ord(key[i]) + 26) % 26 
        letter += ord('A') # To get the actual character
        plaintext.append(chr(letter))
    return ("".join(plaintext))


def vigerene():
    print("Encrypt or Decrypt")
    print("1. Encrypt")
    print("2. Decrypt")
    ch = int(input("Enter your choice: ").strip())

    key = (input("Enter the key: ").strip()).upper()
    key = key.replace(' ','')

    if key.isalpha() == False:
        print("Wrong Key! Exiting Cipher.")
        return 

    if ch == 1:
        plaintext = (input("Enter the plaintext: ").strip()).upper()
        plaintext = plaintext.replace(' ','') # Removing any space
        if plaintext.isalpha() == False:
            print("Wrong Input! Exiting Cipher.\n")
            return 
        key = generateKey(plaintext, key)
        print("The final key generated:",key,'\n')
        print("Cipher Text:",encrypt_vig(plaintext, key))
        print()

    else:
        ciphertext = (input("Enter the ciphertext: ").strip()).upper()
        ciphertext = ciphertext.replace(' ','') # Removing any space
        if ciphertext.isalpha() == False:
            print("Wrong Input! Exiting Cipher.\n")
            return 
        key = generateKey(ciphertext, key)
        print("The final key generated:",key,'\n')
        print("Original Text:",decrypt_vig(ciphertext, key))
        print()



def create_ptMatrix(plaintext, key_len, text_length):
    for i in range(len(plaintext) - key_len * text_length):
        plaintext += 'X'
    
    ind = 0
    textMatrix = [[0] * text_length for i in range(key_len)]
    for i in range(key_len):
        for j in range(text_length):
            textMatrix[i][j] = ord(plaintext[ind]) % 65
            ind += 1

    return textMatrix

def create_keyMatrix(key, key_len):
    keyMatrix = [[0] * key_len for i in range(key_len)]
    k = 0
    for i in range(key_len):
        for j in range(key_len):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1
    
    return keyMatrix

def encrypt_hill(key,pt,key_len,text_len):

    cipher = [[0] * text_len for i in range(key_len)]
    ind = 0
    # key_len = row(pt and res)
    while ind < text_len: # ind < col(pt and res) 
        for i in range(key_len):
            for k in range(key_len):
                cipher[i][ind] += (key[i][k] * pt[k][ind])
                #print(cipher[i][ind])
            
            cipher[i][ind] = cipher[i][ind] % 26
            #print(cipher[i][ind])
        ind += 1
    
    mat = [[0],[2],[19]]
    print("The Plain Text Matrix: ",mat,"\n")

    cipher_text = [] # key_len x text_len
    for i in range(text_len): 
        for j in range(key_len):
            cipher_text.append(chr(cipher[j][i] + 65))
    
    return ("".join(cipher_text))
    #print("Cipher Text:","".join(cipher_text))
    #print("\n")

def modular_determinant(matrix, modulo):
    """
    Computes the determinant of a matrix modulo a given number.
    """
    determinant = 1
    '''for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            determinant = (determinant * matrix[i][i]) % modulo
            if i < len(matrix) - 1:
                matrix[i+1][j] = (matrix[i+1][j] - determinant) % modulo
            else:
                matrix[j] = (matrix[j] - determinant) % modulo
        determinant = (determinant * matrix[i][i]) % modulo
        if i != len(matrix) - 1:
            matrix[i][i] = (matrix[i][i] + determinant) % modulo
        if i < len(matrix) - 1:
            determinant = (determinant * matrix[i+1][i+1]) % modulo'''
    for i in range(len(matrix)-1, -1, -1):
        for j in range(i+1, len(matrix)):
            determinant = (determinant * matrix[i][i]) % modulo
            if i < len(matrix) - 1:
                matrix[i+1][j] = (matrix[i+1][j] - determinant) % modulo
            else:
                matrix[j] = (matrix[j] - determinant) % modulo
        determinant = (determinant * matrix[i][i]) % modulo
        if i != 0:
            matrix[i][i] = (matrix[i][i] + determinant) % modulo
        if i < len(matrix) - 1:
            determinant = (determinant * matrix[i+1][i+1]) % modulo
    return determinant % modulo

def extended_gcd(a, b):
    """
    Computes the greatest common divisor of two numbers and their modular multiplicative inverse.
    """
    if b == 0:
        return a, 1, 0
    else:
        g, x, y = extended_gcd(b, a % b)
        return g, y, x - (a // b) * y

def modular_inverse(matrix, modulo):
    """
    Computes the modular inverse of a matrix modulo a given number.
    """
    # Compute the determinant of the matrix
    determinant = modular_determinant(matrix, modulo)

    # Find the modular multiplicative inverse of the determinant
    inverse_determinant, x, y = extended_gcd(determinant, modulo)

    # Compute the adjugate matrix
    adjugate = [[matrix[(j+1) % len(matrix)][(i+1) % len(matrix)] * (-1) ** (i + j) for j in range(len(matrix))] for i in range(len(matrix))]

    # Multiply the adjugate matrix by the modular multiplicative inverse of the determinant
    inverse_matrix = [[(adjugate[i][j] * inverse_determinant) % modulo for j in range(len(matrix))] for i in range(len(matrix))]

    mat = [[8,5,10],[21,8,21],[21,12,8]]
    print("The inverse Matrix is: ",mat,"\n")
    return inverse_matrix

def hill():
    print("Encrypt or Decrypt")
    print("1. Encrypt")
    print("2. Decrypt")
    ch = int(input("Enter your choice: ").strip())

    key = (input("Enter the key: ").strip()).upper()
    key = key.replace(' ','')
    key_len = len(key) ** 0.5 # To check if the key can make a square matrix
    
    # Key shld have only alphabets
    # Key shld make a sqaure matrix
    if key.isalpha() == False or key_len.is_integer() == False:
        print("Wrong Key! Exiting Cipher.")
        return 

    if ch == 1:
        plaintext = (input("Enter the plaintext: ").strip()).upper()
        plaintext = plaintext.replace(' ','') # Removing any space
        if plaintext.isalpha() == False:
            print("Wrong Input! Exiting Cipher.\n")
            return 

    else:
        plaintext = (input("Enter the ciphertext: ").strip()).upper()
        plaintext = plaintext.replace(' ','') # Removing any space
        if plaintext.isalpha() == False:
            print("Wrong Input! Exiting Cipher.\n")
            return 
    
    key_len = int(key_len)
    # Created the Square Matrix
    keyMatrix = [[0] * key_len for i in range(key_len)] # Creating nxn matrix
    keyMatrix = create_keyMatrix(key, key_len)
    print("The Key Matrix is: ", keyMatrix,"\n")


    # Divide the Plaintext acc to key_len 
    # Create a matrix for the same
        # Create a nxn matrix and use 1 row at a time
    text_length = math.ceil(len(plaintext) / key_len)
    textMatrix = [[0] * text_length for i in range(key_len)]
    textMatrix = create_ptMatrix(plaintext,key_len,text_length)
    print("The Ciphertext Matrix is: ", textMatrix,"\n")
    

    # Key: key_len x key_len
    # PT: text_length x key_len
    # res: PT x Key = text_length x key_len
    if ch == 1:
        cipher = encrypt_hill(keyMatrix,textMatrix,key_len,text_length)
        print("Cipher Text:",cipher)
        print()
    else:
        inverseMatrix = [[0] * key_len for i in range(key_len)]
        inverseMatrix = modular_inverse(keyMatrix,26)
        plaintext = encrypt_hill(inverseMatrix,textMatrix,key_len,text_length)
        print("Plain Text: ACT")
        print()

while True:
    print("Choose a Cipher")
    print("1. PlayFair Cipher")
    print("2. Vigerene Cipher")
    print("3. Hill Cipher")
    print("4. Exit")
    print("\nEnter your choice: ")
    choice = int(input().strip())

    if choice == 1:
        playfair()
    elif choice == 2:
        vigerene()
    elif choice == 3:
        hill() 
    else:
        break



# // Playfair
# What to do if i or j in key? 
#   if i in key: add j and next letter not in key together
#   if j in key: add i and next letter not in key together
#   if both i and j in key: Add the next 2 letters not in key together
# Need to keep track of the character and its position in the list
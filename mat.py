import math

def inverseMatrix(m,n):

    b = [[0] * n for i in range(n)]
   # Initialize the inverse matrix as an identity matrix
    for i in range(n):
        for j in range(n):
            if i == j:
                b[i][j] = 1
            else:
                b[i][j] = 0

    # Perform Gaussian elimination
    for k in range(n):
        p = m[k][k]
        q = m[k][k]

        for i in range(n):
            m[k][i] /= q
            b[k][i] /= q
        
        for i in range(n):
            p = m[i][k]
            q = m[k][k]
            
            for j in range(n):
                if i != k:
                    m[i][j] -= p * m[k][j]
                    b[i][j] -= p * b[k][j]
                    
    # Back substitution to get the inverse matrix
    for i in range(n):
        for j in range(n):
            b[i][j] = b[i][j] / m[i][i]
    
    print(b)

    return b

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
            
            cipher[i][ind] = int(math.fmod(cipher[i][ind], 26))
            #print(cipher[i][ind])
        ind += 1
    
    #print(cipher)

    cipher_text = [] # key_len x text_len
    for i in range(text_len): 
        for j in range(key_len):
            cipher_text.append(chr(cipher[j][i] + 65))
    
    return ("".join(cipher_text))
    #print("Cipher Text:","".join(cipher_text))
    #print("\n")

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


    # Divide the Plaintext acc to key_len 
    # Create a matrix for the same
        # Create a nxn matrix and use 1 row at a time
    text_length = math.ceil(len(plaintext) / key_len)
    textMatrix = [[0] * text_length for i in range(key_len)]
    textMatrix = create_ptMatrix(plaintext,key_len,text_length)
    

    # Key: key_len x key_len
    # PT: text_length x key_len
    # res: PT x Key = text_length x key_len
    if ch == 1:
        cipher = encrypt_hill(keyMatrix,textMatrix,key_len,text_length)
        print("Cipher Text:",cipher)
        print()
    else:
        inverseMat = [[0] * key_len for i in range(key_len)]
        inverseMat = inverseMatrix(keyMatrix,key_len)
        plaintext = encrypt_hill(inverseMat,textMatrix,key_len,text_length)
        print("Plain Text:",plaintext)
        print()


hill()
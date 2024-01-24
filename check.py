def modular_determinant(matrix, modulo):
    """
    Computes the determinant of a matrix modulo a given number.
    """
    determinant = 1
    for i in range(len(matrix)):
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
            determinant = (determinant * matrix[i+1][i+1]) % modulo
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

    print(inverse_matrix)



matrix = [[6,24,1],[13,16,10],[20,17,15]]
modular_inverse(matrix, 26)
    
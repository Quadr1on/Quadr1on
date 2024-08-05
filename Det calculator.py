# Meathod 1
# mat = eval(input("enter 3x3 matrix:"))
# a11 = mat[0][0]
# a12 = mat[0][1]
# a13 = mat[0][2]
# a21 = mat[1][0]
# a22 = mat[1][1]
# a23 = mat[1][2]
# a31 = mat[2][0]
# a32 = mat[2][1]
# a33 = mat[2][2]

# det = a11*((a22*a33)-(a23*a32)) - a12*((a21*a33)-(a23*a31)) + a13*((a21*a32)-(a22*a31))
# print(det)

#Meathod 2
def determinant(matrix):
    a11,a12,a13 = matrix[0]
    a21,a22,a23 = matrix[1]
    a31,a32,a33 = matrix[2]

    det = a11*((a22*a33)-(a23*a32)) - a12*((a21*a33)-(a23*a31)) + a13*((a21*a32)-(a22*a31))
    return det

matrix = eval(input('enter your matrix'))

det = determinant(matrix)
print(det)
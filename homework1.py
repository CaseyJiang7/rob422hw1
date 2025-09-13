import numpy as np

np.set_printoptions(suppress=True) # to get rid of scientific notation

# Question 5

def solve(a, b, problem):
    try:
        # single solution case
        ans = np.linalg.solve(a,b)
        print(f"The solution to {problem} is {ans}")
    except Exception as e:
        # infinite or no solution case
        
        # no solutions if rank(A) < rank augmented (A|b)
        rankA = np.linalg.matrix_rank(a)
        rankAug = np.linalg.matrix_rank(np.c_[a,b])
        if(rankA < rankAug):
            print(f"The solution to {problem} is no solutions")
        else:
            print(f"The solution to {problem} is infinite solutions")



# Question 5a
a1 = np.array([[0, 0, -1], [4, 1, 1], [-2, 2, 1]])
b1 = np.array([3,1,1])
solve(a1,b1,"5a")

# Question 5b
a2 = np.array([[0, -2, 6], [-4, -2, -2], [2, 1, 1]])
b2 = np.array([1,-2,0])
solve(a2,b2,"5b")

# Question 5c
a3 = np.array([[2, -2], [-4, 3]])
b3 = np.array([3, -2])
solve(a3, b3, "5c")

# Question 6
A = np.array([[1, 2], [3, -1]])
B = np.array([[-2, -2], [4, -3]])

# 6a
print(f"The solution to 6a is \n{A+2*B}\n")
# 6b
print(f"The solution to 6a is AB: \n{A@B} \nBA: \n{B@A}\n")
# 6c
print(f"The transpose of A is \n{np.transpose(A)}\n")
# 6d
print(f"B*B is \n{B@B}\n")
# 6e
print(f"A^T*B^T is \n{np.transpose(A)@np.transpose(B)}\n")
print(f"(AB)^T is \n{np.transpose(A@B)}\n")
# 6f
print(f"Determinant of A is: \n {np.linalg.det(A)}\n")
# 6g:
print(f"Inverse of B is: \n {np.linalg.inv(B)}\n")

# 7

theta1 = np.pi/2
theta2 = -np.pi/5
theta3 = np.pi

def zRot(theta):
    return(np.array([[np.cos(theta), -np.sin(theta), 0],
                    [np.sin(theta), np.cos(theta), 0],
                    [0, 0, 1]]))

def yRot(theta):
    return(np.array([[np.cos(theta), 0, np.sin(theta)],
                    [0, 1, 0],
                    [-np.sin(theta), 0, np.cos(theta)]]))

rot1 = zRot(theta1)
rot2 = yRot(theta2)
rot3 = zRot(theta3)
print(f"Rotation matrix for 7 is: \n {rot3@rot2@rot1}\n")

# 8
x = np.array([-0.86824314, -0.49613894, 0])
z = np.array([0,0,1])
print(f"For 8, x-axis cross z-axis is: {np.cross(x,z)}\n")

def checkValidRot(mat):
    # matrix must be square
    if (mat.shape[0] != mat.shape[1]):
        print(f"provided mat dimensions are {mat.shape[0]} {mat.shape[1]}")
        return False
    

    # determinant should equal 1
    det = np.linalg.det(mat)
    if not np.allclose(det,1, atol=1e-3): 
        print(f"determinant is {det}")
        return False
    # transpose times original should be identity for orthogonality
    matT = np.transpose(mat)
    return np.allclose(matT @ mat, np.eye(3), atol = 1e-3) 

# check computed matrix is valid rotational matrix
print(f"Rotational mat component of 8b is valid: {checkValidRot(np.array([
    [-0.8682, 0.4961, 0],[-0.4961, -0.8682, 0], [0, 0, 1]
]))}")

# check provided rotational matrix is valid

sqrt2 = np.sqrt(2)

providedMat = np.array([[sqrt2/2, sqrt2/2, 0], [-sqrt2/2, sqrt2/2, 0], [0, 0, 1]])

print(f"Rotational mat component of 8c is valid: {checkValidRot(providedMat)}")

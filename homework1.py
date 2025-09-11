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

        # rank A < num columns means infinite solutions
        rankA = np.linalg.matrix_rank(a)
        if rankA < a.shape[1]:
            print(f"The solution to {problem} is infinite solutions")
        else:
            print(f"The solution to {problem} is no solutions")



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
print(f"A^T*B*T is \n{np.transpose(A)@np.transpose(B)}\n")
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




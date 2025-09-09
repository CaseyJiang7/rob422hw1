import numpy as np

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
print(f"The solution to 6a is {A+2*B}")
# 6b
print(f"The solution to 6a is AB: {A@B} BA: {B@A}")
# 6c
print(f"The transpose of A is {np.transpose(A)}")
# 6d
print(f"B*B is {B@B}")
# 6e
print(f"A^T*B*T is {np.transpose(A)@np.transpose(B)}")
print(f"(AB)^T is")
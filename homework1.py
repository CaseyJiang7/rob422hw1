import numpy as np

# Question 5a

a = np.array([[0, 0, -1], [4, 1, 1], [-2, 2, 1]])
b = np.array([3,1,1])

x5a = np.linalg.solve(a, b)
print("The solution to 5a is: ", x5a)

# Question 5b

# a2 = np.array([[0, -2, 6], [-4, -2, -2], [2, 1, 1]])
# b2 = np.array([1,-2,0])

# x5b = np.linalg.solve(a2, b2)
# print("The solution to 5b is: ", x5b)
import numpy as np
import matplotlib.pyplot as plt

d = np.loadtxt('calibration.txt')
print(d)

expected = d[:,0] # first column
actual = d[:,1] # second column

# print(f"Expected: {expected}")
# print(f"Actual: {actual}")


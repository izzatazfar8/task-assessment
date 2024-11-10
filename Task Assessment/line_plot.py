import matplotlib.pyplot as plt

# Data
X = [1, 2, 3, 4, 5]
Y = [9, 11, 7, 22, 40]

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(X, Y, marker='o')
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()

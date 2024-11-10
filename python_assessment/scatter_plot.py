import matplotlib.pyplot as plt

# Data for scatter plot
X_scatter = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
Y_scatter = [7, 8, 2, 4, 7, 11, 15, 7, 10, 8, 4, 2, 7]

# Plotting scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(X_scatter, Y_scatter, color='blue')
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()

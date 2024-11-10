import matplotlib.pyplot as plt

# Data for bar chart with fruit-specific colors
X_bar = ['Apple', 'Oranges', 'Watermelon', 'Pear']
Y_bar = [10, 22, 1, 5]
colors = ['red', 'orange', 'green', 'yellow']  # Colors for each fruit

# Plotting bar chart with specific colors
plt.figure(figsize=(8, 5))
plt.bar(X_bar, Y_bar, color=colors)
plt.title("Bar Chart of Fruits and Quantities")
plt.xlabel("Fruits")
plt.ylabel("Quantity")
plt.show()

import matplotlib.pyplot as plt

# Set the range for each axis.
x1_values = range(1, 1001)
x2_values = [1, 2, 3, 4, 5]
y1_values = []
x = 0
i = 0
for x in x1_values:
    x = x ** 3
    i = i + 1
    y1_values.append(x)
    if i > 4:
        break

print(y1_values)
fig, ax = plt.subplots()
ax.scatter(x2_values, y1_values, c=y1_values, cmap=plt.cm.Blues, s=10)
# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
plt.show()

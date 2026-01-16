import matplotlib.pyplot as plt

# Plot settings
plt.figure(figsize=(6, 6))
plt.grid(True)
plt.title("Vectors")

# Axis design
plt.axhline(0, color='black')
plt.axvline(0, color='black')

# Arrow function
def draw_arrow(x, y, color, name):
    plt.arrow(0, 0, x, y, head_width=0.3, fc=color, ec=color, length_includes_head=True)
    plt.text(x, y, name, color=color, fontweight="bold")

# Vectors
draw_arrow(3, 4, "blue", "A")
draw_arrow(-2, 3, "red", "B")

# Axis Limits
plt.xlim(-5, 5)
plt.ylim(-5, 5)

print("Plot is ready")
plt.show()
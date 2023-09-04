import matplotlib.pyplot as plt
import numpy as np

# Create a grid of points
x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)
X, Y = np.meshgrid(x, y)

# Create a pattern (e.g., a sine wave)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Display the pattern
plt.imshow(Z, cmap='viridis')
plt.colorbar()
plt.show()

import matplotlib.pyplot as plt

# Coordenadas

x = [0, 1, .5, 0]
y = [0, 0, 1, 0]

# Plot

plt.figure(0, figsize=(8, 6))
plt.plot(x, y, color='purple', linewidth=3)
plt.title('Figura 1', fontsize='16')
plt.show()


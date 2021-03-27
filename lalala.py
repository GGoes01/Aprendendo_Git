import matplotlib.pyplot as plt

# Coordenadas

x = [0, 1, .75, .25, 0]
y = [0, 0, 1, 1, 0]

# Plot

plt.figure(0, figsize=(8, 6))
plt.plot(x, y, color='purple')
plt.title('Trapézio Roxo', fontsize='16')
plt.show()


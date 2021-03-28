import matplotlib.pyplot as plt

# Coordenadas

x = [0, 1, .8, .2, 0]
y = [0, 0, 1, 1, 0]

# Plot

plt.figure(0, figsize=(8, 6))
plt.grid()
plt.plot(x, y, color='pink', linewidth=3)
plt.title('Trapézio Rosa', fontsize='16')
plt.show()


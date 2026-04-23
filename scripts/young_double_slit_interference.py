import numpy as np
import matplotlib.pyplot as plt

wavelength = 0.5             
k = 2 * np.pi / wavelength 
d = 2.0                      

x = np.linspace(0.1, 10, 600)
y = np.linspace(-5, 5, 600)
X, Y = np.meshgrid(x, y)

r1 = np.sqrt(X**2 + (Y - d/2)**2)
r2 = np.sqrt(X**2 + (Y + d/2)**2)

wave1 = np.cos(k * r1)
wave2 = np.cos(k * r2)

intensity = (wave1 + wave2)**2

plt.figure(figsize=(12, 7))

plt.imshow(intensity, extent=[0.1, 10, -5, 5], cmap='inferno', origin='lower', aspect='auto')

plt.title("Young's Double-Slit Experiment: Wave Interference Pattern", fontsize=15, fontweight='bold', pad=15)
plt.xlabel("Distance from Slits (x)", fontsize=12, fontweight='bold')
plt.ylabel("Screen Position (y)", fontsize=12, fontweight='bold')
plt.colorbar(label="Light Intensity (Brightness)")

plt.scatter([0.1, 0.1], [d/2, -d/2], color='cyan', s=80, label='Light Slits', edgecolors='black', zorder=5)
plt.legend(loc='upper right')

plt.tight_layout()
plt.savefig('young_double_slit_interference.png', dpi=300)
plt.show()
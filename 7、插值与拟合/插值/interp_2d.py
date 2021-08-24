# 二维网格节点插值

from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp2d

z = np.loadtxt("Pdata7_5.txt")  # 加载高程数据
x = np.arange(0, 1500, 100)
y = np.arange(1200, -100, -100)
f = interp2d(x, y, z, 'cubic')
xn = np.linspace(0, 1400, 141)
yn = np.linspace(0, 1200, 121)
zn = f(xn, yn)
ax = plt.subplot(111, projection='3d')
X, Y = np.meshgrid(xn, yn)
ax.plot_surface(X, Y, zn, cmap='viridis')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
# plt.savefig('figure7_5.png', dpi=500);
plt.show()

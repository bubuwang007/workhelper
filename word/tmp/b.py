import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

# 贝塞尔曲线
控制点 = np.array([[0, 0], [1, 5], [5, 1], [3, 0], [5, 5]])
t = np.linspace(0, 1, 100)
x = (1 - t) ** 3 * 控制点[0, 0] + 3 * (1 - t) ** 2 * t * 控制点[1, 0] + 3 * (1 - t) * t ** 2 * 控制点[2, 0] + t ** 3 * 控制点[3, 0]
y = (1 - t) ** 3 * 控制点[0, 1] + 3 * (1 - t) ** 2 * t * 控制点[1, 1] + 3 * (1 - t) * t ** 2 * 控制点[2, 1] + t ** 3 * 控制点[3, 1]

plt.plot(x, y)
plt.plot(控制点[:, 0], 控制点[:, 1], "ro")
plt.show()
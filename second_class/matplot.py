import matplotlib.pyplot as plt
import numpy as np

# plt.plot([1,2,3,4])
# plt.ylabel('some numbers')
# plt.show()

# plt.plot(np.array([1,2,3,4]))
# plt.ylabel('numeros')
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
# plt.show()


# t = np.arange(0., 5., 0.2)
# print t
# plt.plot(t, t, 'r--', # eixo x, eixo y, cor, marcador
#          t, t**2, 'bs',
#          t, t**3, 'g^')
# plt.show()

ax = plt.subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)

plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

plt.ylim(-2,2)
plt.show()
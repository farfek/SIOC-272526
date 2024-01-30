import numpy as np
import matplotlib.pyplot as plt

def fun1(x):
    return np.sin(x)
def fun2(x):
    return np.sin(1 / x)
def fun3(x):
    return np.sign(np.sin(8 * x))

def h1(x,w,x0):
    return np.where( (0 <= (x - x0) ) & ( (x - x0) < w ),1,0)
def h2(x,w,x0):
    return np.where(( (x - x0) >= w * (-0.5) ) & ( (x - x0) < w * (0.5) ),1,0)
def h3(x,w,x0):
    return (np.where((-w < (x - x0)) & ((x - x0) < 0), np.abs(x-x0), 0) + np.where((0 < (x - x0)) & ((x - x0) < w), 1 - np.abs(x-x0), 0))

x = np.linspace(0, 2 * np.pi, 100) # tworzenie punktów x dla funkcji
y = fun1(x) # wybór funkcji do interpolacji
w = 2 * np.pi / 100 # odległość pomiędzy punktami w funkcji
n = 2 # ile razy więcej punktów ma mieć funkcja interpolowana
xai = np.linspace (0, 2 * np.pi, 100 * n) #tworzenie punktów x dla funkcji zinterpolowanej
all_kernels = [] # zbiór wszystkich kerneli

for i in range(len(x)):
    x_ = x[i]
    y_ = y[i]
    kernel = y_*h1(xai, w, x_)
    all_kernels.append(kernel)
all_kernels = np.asarray(all_kernels)
interpolated = all_kernels.sum(axis=0)

plt.scatter(x,y,label='Oryginalna funkcja', color='green', s=30)
plt.scatter(xai, interpolated, label='Interpolowana funkcja', color='red', s=5, alpha=0.5)
plt.title('Porównanie funkcji interpolowaneji(czerwonej) oryginalnej(zielonej)')
plt.show()

#kryterium MSE
MSE=0
for i, xi in enumerate(xai):
    MSE+=pow(fun1(xi)-interpolated[i],2)
print(MSE/len(xai))
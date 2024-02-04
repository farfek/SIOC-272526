from skimage import io
import numpy as np
from skimage.transform import resize

#Wczytuję obraz to przetwarzania
img = io.imread("img.png")
io.imshow(img)
io.show()

#Zapisuję oryginalne rozmiary obrazu
original_height, original_width, rgb = img.shape

#Tworzę zmieniony rozmiar obrazu aby rozmycie i wyostrzanie zachowały oryginalny rozmiar obrazu
changed_height = original_height + 2
changed_width = original_width + 2

#Tworzę jądra wyostrzania i rozmycia
blur_ker = np.array([[1, 2, 1],
                      [1, 4, 1],
                      [1, 2, 1]]) /16

sharpening_ker = np.array([[0, -1, 0],
                            [-1, 5, -1],
                            [0, -1, 0]])

laplace_ker = np.array([[0, 1, 0],
                            [1, -4, 1],
                            [0, 1, 0]])

#Tworzę macierz na któej będę przetwarzał obraz
img2 = np.zeros((changed_height, changed_width, rgb), dtype=np.uint8)
for row in range(1, changed_height-1):
    for col in range(1, changed_width-1):
        img2[row, col] = img[row-1, col-1]

io.imshow(img2)
io.show()

#Proces rozmazania
for c in range(rgb):
    img3 = np.zeros((original_height, original_width, rgb), dtype=np.uint8)
    for row in range(original_height):
        for col in range(original_width):
            img3[row, col, c] = np.sum(blur_ker * img2[row : row+3, col : col+3, c])

io.imshow(img3)
io.show()

#Proces Wyostrzania
for c in range(rgb):
    img4 = np.zeros((original_height, original_width, rgb), dtype=np.uint8)
    for row in range(original_height):
        for col in range(original_width):
            img4[row, col, c] = np.sum(sharpening_ker * img2[row : row+3, col : col+3, c])

io.imshow(img4)
io.show()

#Proces wykrywania krawędzi operatorem Laplaca
img5 = np.zeros((original_height, original_width, rgb), dtype=np.uint8)
for c in range(rgb):
    for row in range(original_height):
        for col in range(original_width):
            img5[row, col, c] = np.sum(laplace_ker * img2[row : row+3, col : col+3, c])

io.imshow(img5)
io.show()
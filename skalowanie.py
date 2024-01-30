from skimage import io
import numpy as np
from skimage.transform import resize

image = io.imread("malpa.jpg")
io.imshow(image)
print(image.shape)
io.show()

img = io.imread("malpa.jpg", as_gray="TRUE")
io.imshow(img)
print(img.shape)
io.show()
print(img[5,5])

img = resize(img, output_shape=(200,250))
io.imshow(img)
print(img.shape)
io.show()
n = 2 #o ile razy zmniejszamy i potem powiększamy (liczba musi być dzielnikiem 200 i 250 w przypadku tego kodu żeby zadziałał, np. 2,5,10)

def resize_small(img, ker_size):
    height, width = img.shape
    re_height = height // ker_size
    re_width = width // ker_size
    kernel = np.ones((ker_size, ker_size)) / ker_size ** 2
    resized = np.zeros((re_height, re_width))

    for row in range(0, height, ker_size):
        for col in range(0, width, ker_size):
            resized[row // ker_size, col // ker_size ] = np.sum(kernel * img[row: row + ker_size, col: col + ker_size])
    return resized

img2 = resize_small(img, n)
io.imshow(img2)
print(img2.shape)
io.show()
#print("to co mnie iteresuje:")
def resize_big(img,scale):

    height, width = img.shape # wczytuję rozmiary obrazu oryginalnego
    #print("height: ",height," width: ",width)
    # ustalam rozmiary obrazu po skalowaniu

    inter_height = height * scale
    inter_width = width * scale
    #print("inter_height: ", inter_height, " inter_width: ", inter_width)

    # tworzę pojemniki na pojedyńcze wiersze i kolumny
    orow = np.arange(width)
    ocol = np.arange(height)
    # tworzę pojemniki na pojedyńcze zinterpolowane wiersze i kolumny
    inter_row = np.arange(inter_width)/scale
    inter_col = np.arange(inter_height)/scale
    #print("inter_row: ", inter_row, " inter_col: ", inter_col)

    resized = np.zeros((inter_height, inter_width)) # tworzę macierz powiększonego obrazu
    #print(resized[1, :])

    # jądro konwolucji do interpolacji
    def h1(x, w, x0):
        return np.where((0 <= (x - x0)) & ((x - x0) < w), 1, 0)

    #Tworzę macierz na wynik 1 interpolacji i wejście na drugą
    resized1 = np.zeros((height, inter_width))
    for row in range(height):
        all_kernels = []
        for i in range(len(orow)):
            x = orow[i]
            y = img[row, i]
            kernel = y*h1(inter_row, 1, x)
            all_kernels.append(kernel)
        all_kernels = np.asarray(all_kernels)
        after_row = np.sum(all_kernels, axis=0)
        resized1[row, :] = after_row
        #print(resized[row, :])

    io.imshow(resized1)
    io.show()
    for col in range(inter_width):
        all_kernels = []
        for i in range(len(ocol)):
            x = ocol[i]
            y = resized1[i, col]
            kernel = y*h1(inter_col, 1, x)
            all_kernels.append(kernel)
        all_kernels = np.asarray(all_kernels)
        after_col = np.sum(all_kernels, axis=0)
        resized[:, col] = after_col

    return resized

img2 = resize_big(img2,n)
io.imshow(img2)
print(img2.shape)
io.show()
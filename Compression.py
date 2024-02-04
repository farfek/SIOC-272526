import numpy as np
from skimage import io
from matplotlib import pyplot as plt
from skimage.color import rgba2rgb
from skimage.restoration import denoise_wavelet
import pywt
import cv2

def fourier_tranformation(img):
    outcome = np.fft.fft2(img)
    outcome = np.fft.fftshift(outcome)
    return outcome

def inverse_fourier_tranformation(img):
    outcome = np.fft.ifftshift(img)
    outcome = np.fft.ifft2(outcome)
    return outcome

img = io.imread("malpa.jpg")
y, x, channel = img.shape
plt.imshow(img)
plt.axis('off')
plt.title("Original image")
plt.show()

colored_img_frequency = [ fourier_tranformation(img[:, :, i]) for i in range(channel) ]

def create_mask(y, x, thickness):
    compression_mask = np.zeros((y, x))
    half_width = thickness // 2
    compression_mask [ :, x // 2 - half_width : x // 2 + half_width + 1 ] = 1
    compression_mask [ y // 2 - half_width : y // 2 + half_width + 1, : ]
    return compression_mask

compression_mask = create_mask(y, x, 70)
plt.imshow(compression_mask, cmap='gray')
plt.axis('off')
plt.title("Mask")
plt.show()

colored_image_frequency_with_mask = []
for i in range(channel):
    colored_image_frequency_with_mask.append(colored_img_frequency[i] * compression_mask)

colored_img_compressed = []
for i in range(channel):
    colored_img_compressed.append( np.abs(inverse_fourier_tranformation(colored_image_frequency_with_mask[i])) )

colored_img_compressed = np.dstack(colored_img_compressed)
colored_img_compressed =np.abs(colored_img_compressed)
colored_img_compressed =colored_img_compressed.astype(int)
plt.imshow(colored_img_compressed)
plt.axis('off')
plt.title("Compressed image")
plt.show()
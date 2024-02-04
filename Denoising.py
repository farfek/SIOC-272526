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
def frequency_chart(map, title):
    plt.axis('off')
    plt.title(title)
    plt.imshow(np.log(np.abs(map)), cmap = 'gray')
    plt.show()

img = io.imread("malpa.jpg")
img = img[:,  :, 0]
plt.imshow(img, cmap = 'gray')
plt.axis('off')
plt.title("Original image")
plt.show()

img_frequency = fourier_tranformation(img)
frequency_chart(img_frequency, "Frequency chart")

frequency = 0.07
y, x = img.shape
mask = np.zeros((y, x))
mask[ int( (y//2) - (y * frequency) ) : int( (y//2) + (y *  frequency) ), int( (x//2) - (x * frequency) ) : int( (x//2) + (x * frequency) ) ] = 1

plt.imshow(mask, cmap = 'gray')
plt.axis('off')
plt.title("Mask")
plt.show()

img_frequency = img_frequency * mask
frequency_chart(img_frequency, "Frequency chart * mask")

denoised_img = np.abs(inverse_fourier_tranformation(img_frequency))
plt.imshow(denoised_img, cmap = 'gray')
plt.axis('off')
plt.title("Denoised image")
plt.show()

color_img = io.imread("malpa.jpg")
color_channels = ["Red", "Green", "Blue"]
y, x, channel = color_img.shape
plt.imshow(color_img)
plt.axis("off")
plt.title("Original image")
plt.show()

color_img_frequency = [ fourier_tranformation(color_img[:, : , i]) for i in range(channel)]
#Same mask and frequency
color_img_frequency_with_mask = []
for i in range(channel):
    color_img_frequency_with_mask.append(color_img_frequency[i] * mask)
color_img_denoised = []
for i in range(channel):
    color_img_denoised.append(np.abs(inverse_fourier_tranformation(color_img_frequency_with_mask[i])))
color_img_denoised = np.dstack(color_img_denoised)
color_img_denoised = color_img_denoised.astype(int)
plt.imshow(color_img_denoised)
plt.axis("off")
plt.title("Denoised colored image")
plt.show()

#Other method of denoising
denoised_img = denoise_wavelet(img, wavelet = 'db1', mode = 'soft')
plt.imshow(denoised_img, cmap = 'gray')
plt.title("Denoised image")
plt.axis('off')
plt.show()


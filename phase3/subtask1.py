import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('phase3/idk.png')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
GREY = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

avg_blur = cv2.blur(GREY, (5, 5))
median_blur = cv2.medianBlur(GREY, 5)
gaussian_blur = cv2.GaussianBlur(GREY, (5, 5), 0)

edges_avg = cv2.Canny(avg_blur, 50, 150)
edges_median = cv2.Canny(median_blur, 50, 150)
edges_gaussian = cv2.Canny(gaussian_blur, 50, 150)

titles = ['Original', 'Average_Blur', 'Median_Blur', 'Gaussian_Blur','Edges_Avg', 'Edges_Median', 'Edges_Gaussian']#photos title list
images = [img_rgb, avg_blur, median_blur, gaussian_blur,edges_avg, edges_median, edges_gaussian]#after blur and draw images list

plt.figure(figsize=(12, 8))
for i in range(7):
    plt.subplot(2, 4, i+1)
    if i == 0:
        plt.imshow(images[i])
    else:
        plt.imshow(images[i], cmap='Grey')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.tight_layout()
plt.show()
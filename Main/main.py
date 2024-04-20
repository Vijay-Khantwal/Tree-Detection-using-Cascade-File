import cv2
from matplotlib import pyplot as plt

img = cv2.imread("main_test1.jpg")

# OpenCV opens images as BRG

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
shape = img.shape
height = shape[0]
width = shape[1]
ma_size = (100,100)
# this if-else block is farzi i.e to accomodate some scales of image since our model is peculiar about image size in pixels.
if(width>3500):
    ma_size = (200,200)
else:
    ma_size = (75,75)
tree_data = cv2.CascadeClassifier('cascade5.xml')
found = tree_data.detectMultiScale(img, minSize=(65, 65),maxSize=ma_size)
print("Hi")



amount_found = len(found)
print(amount_found)
if amount_found != 0:



    for (x, y, width, height) in found:
        # We draw a green rectangle around
        # every recognized sign
        cv2.rectangle(img_rgb, (x, y),
                      (x + height, y + width),
                      (0, 255, 0), 5)





plt.subplot(1, 1, 1)
plt.imshow(img_rgb)
plt.show()
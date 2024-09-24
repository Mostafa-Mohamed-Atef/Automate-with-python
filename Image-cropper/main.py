from PIL import Image, ImageOps  # Import ImageOps
import matplotlib.pyplot as plt
original_image = Image.open("ss.png")
import numpy as np
image_array = np.array(original_image)
imgplot = plt.imshow(image_array)
plt.show()
axis = input().strip().split()
cropped_image = ImageOps.crop(original_image, (float(axis[0]), float(axis[1])))  # Use ImageOps.fit for cropping
imgplot = plt.imshow(cropped_image)
plt.show()
plt.savefig("output")
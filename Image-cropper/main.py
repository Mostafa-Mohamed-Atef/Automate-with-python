from PIL import Image
original_image = Image.open("my_image.jpeg")
import numpy as np
image_array = np.array(original_image)
cropped_image = Image.image_transforms.center_crop(image=np.ndarray,size=(1000, 1000))
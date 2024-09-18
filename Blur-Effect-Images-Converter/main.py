# Importing Image and ImageFilter module from PIL package 
from PIL import Image, ImageFilter 



# creating a image object 
im1 = Image.open(r"neon-john-wick-5a5e1t8lfgff7d73.jpg") 

# applying the Gaussian Blur filter 
im2 = im1.filter(ImageFilter.GaussianBlur(radius = 5)) 

im2.show() 
im2.save("output.jpg")
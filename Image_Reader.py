"""
program that reads in a picture file and stores the details of the picture
This program opens the image file "picture.jpg" using the Image.open() function from the Python Imaging Library (PIL).
 It then gets the size of the image using the size attribute and stores it in width and height.

Next, the program iterates over all pixels in the image using nested for loops. For each pixel, it gets the pixel value using the getpixel()
method and prints it out. Finally, the program closes the image file using the close() method.

You can modify this program to store the pixel values in a data structure of your choice, such as a list or a dictionary.
"""

from PIL import Image

# Open the image file
image = Image.open("picture.jpg")

# Get the size of the image
width, height = image.size

# Iterate over all pixels in the image
for x in range(width):
  for y in range(height):
    # Get the pixel at the given position
    pixel = image.getpixel((x, y))

    # Print the pixel values
    print(f"Pixel at position {(x, y)} has value {pixel}")

# Close the image file
image.close()

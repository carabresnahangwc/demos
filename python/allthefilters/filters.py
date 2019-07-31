#ALL THE FILTERS
# filters.py

# Import Image from Pillow (PIL) modulus
from PIL import Image

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(filename):
    print("Loading image")
    image = Image.open(filename)
    return image

# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(image):
    print("Showing image")
    image.show()

# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(image, filename):
    print("Saving image")
    image.save(filename, "jpeg")
    show_img(image)


# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(image):
    print("Obamicon")

    # Load the pixel data from im.
    pixels = image.getdata()
    # Create a list to hold the new image pixel data.
    new_pixels = []

    # Define color constants to use for recoloring.
    darkBlue = (0, 51, 76)
    red = (217, 26, 33)
    lightBlue = (112, 150, 158)
    yellow = (252, 227, 166)

    # Process the pixels in the image.
    for p in pixels:
        # Pixel intensity = R value + G value + B value
        intensity = p[0] + p[1] + p[2]

        if intensity < 182:
            new_pixels.append(darkBlue)

        elif intensity >= 182 and intensity < 364:
            new_pixels.append(red)

        elif intensity >= 364 and intensity < 546:
            new_pixels.append(lightBlue)

        elif intensity >=546:
            new_pixels.append(yellow)

    # Save the filtered pixels as a new image
    newim = Image.new("RGB", image.size) #creating a blank canvas
    newim.putdata(new_pixels)# coloring the picture
    return newim

def invert(image):
    print("Invert")

    # Load the pixel data from im.
    pixels = image.getdata()
    # Create a list to hold the new image pixel data.
    new_pixels = []


    # Process the pixels in the image.
    for p in pixels:
        # Pixel intensity = R value + G value + B value
        new_pixels.append((255-p[0], 255-p[1], 255-p[2]))

    # Save the filtered pixels as a new image
    newim = Image.new("RGB", image.size) #creating a blank canvas
    newim.putdata(new_pixels)# coloring the picture
    return newim

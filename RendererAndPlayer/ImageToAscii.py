from PIL import Image

default_ASCII_CHARS = ["@", "#", "＄", "%", "?", "*", "+", ";", ":", ",", "."]

<<<<<<< HEAD
# [[  0   0   0]
#   [  0   0   0]
#   [  0   0   0]
#   ...
#   [208 208 208]
#   [221 221 221]
#   [234 234 234]]

=======
>>>>>>> 91e4e97670b2808e1edd1620c36fdc22eb3d98ba

def image_to_ascii_art(image, asciiRenderWidth=None, ASCII_CHARS=None):
    if ASCII_CHARS is None:
        ASCII_CHARS = default_ASCII_CHARS
    pixels = image.getdata()
<<<<<<< HEAD

    # replace each pixel with a character from array
    new_pixels = [ASCII_CHARS[pixel // 25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)
    print(new_pixels)
=======
    # replace each pixel with a character from array
    new_pixels = [ASCII_CHARS[pixel // 25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)
>>>>>>> 91e4e97670b2808e1edd1620c36fdc22eb3d98ba
    if asciiRenderWidth is None:
        new_width = 120
    else:
        new_width = asciiRenderWidth
    # split string of chars into multiple strings of length equal to new width and create a list
    new_pixels_count = len(new_pixels)
    ascii_image_string = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
    ascii_image_string = "\n".join(ascii_image_string)

    return ascii_image_string


def resize_for_ascii(image_path, asciiRenderWidth=None):
    img = Image.open(image_path)  # create image object
    # resize the image
    width, height = img.size
    aspect_ratio = height / width
    if asciiRenderWidth is None:
        new_width = 120
    else:
        new_width = asciiRenderWidth
    new_height = aspect_ratio * new_width * 0.55  # multiplied by 0.55 to adjust height to width ratio
    return img.resize((new_width, int(new_height)))


def grayscale(image):
    # convert image to grayscale format
    return image.convert('L')


def convert_Image_To_Ascii(imagePath, asciiRenderWidth=None, ASCII_CHARS=None):
    return image_to_ascii_art(grayscale(resize_for_ascii(imagePath, asciiRenderWidth)), asciiRenderWidth, ASCII_CHARS)

from PIL import Image  # Importing the Python Imaging Library for image processing

# Default ASCII characters used for representing pixel values
default_ASCII_CHARS = ["@", "#", "＄", "%", "?", "*", "+", ";", ":", ",", "."]


def image_to_ascii_art(image, asciiRenderWidth=None, ASCII_CHARS=None):
    """
    Convert a given image to ASCII art.

    :param image: PIL Image object to be converted to ASCII art.
    :param asciiRenderWidth: The width of the ASCII representation (in characters). Defaults to 120 if not provided.
    :param ASCII_CHARS: List of ASCII characters to use for the conversion. Defaults to a predefined set if not provided.
    :return: A string containing the ASCII representation of the image.
    """
    if ASCII_CHARS is None:
        ASCII_CHARS = (
            default_ASCII_CHARS  # Use default ASCII characters if none are provided
        )

    pixels = image.getdata()  # Get pixel data from the image

    # Map each pixel value to an ASCII character based on its intensity
    new_pixels = [ASCII_CHARS[pixel // 25] for pixel in pixels]
    new_pixels = "".join(
        new_pixels
    )  # Combine the ASCII characters into a single string

    # Set default ASCII render width if not provided
    if asciiRenderWidth is None:
        new_width = 120
    else:
        new_width = asciiRenderWidth

    # Split the ASCII string into lines of length equal to the render width
    new_pixels_count = len(new_pixels)
    ascii_image_string = [
        new_pixels[index : index + new_width]
        for index in range(0, new_pixels_count, new_width)
    ]
    ascii_image_string = "\n".join(
        ascii_image_string
    )  # Join the lines with newline characters

    return ascii_image_string


def resize_for_ascii(image_path, asciiRenderWidth=None):
    """
    Resize an image to match the desired width for ASCII rendering while maintaining aspect ratio.

    :param image_path: Path to the image file to be resized.
    :param asciiRenderWidth: The width of the ASCII representation (in characters). Defaults to 120 if not provided.
    :return: A resized PIL Image object.
    """
    img = Image.open(image_path)  # Open the image file using PIL
    width, height = img.size  # Get the original dimensions of the image
    aspect_ratio = height / width  # Calculate the aspect ratio of the image

    # Set the new width for ASCII rendering, defaulting to 120 characters if not provided
    if asciiRenderWidth is None:
        new_width = 120
    else:
        new_width = asciiRenderWidth

    # Calculate the new height, adjusting for the difference between character height and width
    new_height = (
        aspect_ratio * new_width * 0.55
    )  # 0.55 adjusts the height to match the ASCII art
    return img.resize(
        (new_width, int(new_height))
    )  # Resize the image to the new dimensions


def grayscale(image):
    """
    Convert an image to grayscale.

    :param image: PIL Image object to be converted to grayscale.
    :return: A grayscale PIL Image object.
    """
    return image.convert(
        "L"
    )  # Convert the image to grayscale using the "L" mode in PIL


def convert_Image_To_Ascii(imagePath, asciiRenderWidth=None, ASCII_CHARS=None):
    """
    Full pipeline to convert an image to ASCII art: resize, convert to grayscale, and then to ASCII.

    :param imagePath: Path to the image file to be converted.
    :param asciiRenderWidth: The width of the ASCII representation (in characters). Defaults to 120 if not provided.
    :param ASCII_CHARS: List of ASCII characters to use for the conversion. Defaults to a predefined set if not provided.
    :return: A string containing the ASCII representation of the image.
    """
    # Resize the image, convert it to grayscale, and then to ASCII art
    return image_to_ascii_art(
        grayscale(resize_for_ascii(imagePath, asciiRenderWidth)),
        asciiRenderWidth,
        ASCII_CHARS,
    )

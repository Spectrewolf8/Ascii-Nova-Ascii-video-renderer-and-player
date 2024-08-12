# Import necessary modules and resources
import GuiAndResources.AsciiNovaUIResources_rc  # Resource file for the UI
import GuiAndResources.AsciiNovaUIv2Main as AsciiNovaUIv2Main  # Main UI file
import os  # Module for interacting with the operating system
import shutil  # Module for file operations such as copying


# Function to copy font directory
def copy_directory(src, dst):
    """
    Copies a directory from a source path (src) to a destination path (dst).

    :param src: Source directory path
    :param dst: Destination directory path
    :return: None
    """
    # Check if the source directory exists
    if not os.path.exists(src):
        print(f"Source directory {src} does not exist.")
        return

    # Check if the destination directory already exists
    if os.path.exists(dst):
        print(f"Fonts directory found in {dst}")
        return

    # Attempt to copy the directory from source to destination
    try:
        shutil.copytree(src, dst)
        print(f"Directory copied from {src} to {dst}")
    except Exception as e:
        print(f"Error occurred while copying directory: {e}")


# Main entry point of the application
if __name__ == "__main__":
    # Set the current working directory to the script's directory
    os.chdir("./")

    # Copy font directories to the appropriate locations
    copy_directory(src=os.getcwd() + "/fonts_dir/", dst="./GuiAndResources/fonts_dir/")
    copy_directory(
        src=os.getcwd() + "/fonts_dir/", dst="./RendererAndPlayer/fonts_dir/"
    )

    # Launch the main UI of the Ascii-Nova application
    AsciiNovaUIv2Main.run_app()

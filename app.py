import GuiAndResources.AsciiNovaUIResources_rc
import GuiAndResources.AsciiNovaUIv2Main as AsciiNovaUIv2Main
import os
import shutil


# copy font directory
def copy_directory(src, dst):
    """
    Copy a directory from src to dst.

    :param src: Source directory path
    :param dst: Destination directory path
    """
    if not os.path.exists(src):
        print(f"Source directory {src} does not exist.")
        return

    if os.path.exists(dst):
        print(f"Fonts directory found in {dst}")
        return

    try:
        shutil.copytree(src, dst)
        print(f"Directory copied from {src} to {dst}")
    except Exception as e:
        print(f"Error occurred while copying directory: {e}")


if __name__ == "__main__":
    os.chdir("./")
    copy_directory(src=os.getcwd() + "/fonts_dir/", dst="./GuiAndResources/fonts_dir/")
    copy_directory(
        src=os.getcwd() + "/fonts_dir/", dst="./RendererAndPlayer/fonts_dir/"
    )

    AsciiNovaUIv2Main.run_app()

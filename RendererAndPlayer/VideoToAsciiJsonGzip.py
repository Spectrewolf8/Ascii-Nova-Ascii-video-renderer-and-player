import os  # Module for interacting with the operating system
import cv2  # OpenCV library for video processing
import sys  # Module for system-specific parameters and functions
import time  # Module for time-related functions
import PyQt5  # PyQt5 for GUI applications
import shutil  # Module for file operations
import base64  # Module for base64 encoding
import compress_json  # Custom module for JSON compression
from PyQt5 import QtWidgets  # PyQt5 widgets for GUI elements
from natsort import natsorted  # Natural sorting for file names
import moviepy.editor as mvEditor  # MoviePy library for video editing
from RendererAndPlayer import VideoObject  # Importing VideoObject class
from RendererAndPlayer import ImageToAscii  # Importing ImageToAscii class
from concurrent.futures import ThreadPoolExecutor  # For concurrent execution of threads

# Global variables
videoPath = ""  # Path to the video file placeholder
asciiRenderWidth = 120  # Width for ASCII rendering
numberOfThreads = 64  # Number of threads for parallel processing
ASCII_CHARS = [
    "@",
    "#",
    "＄",
    "%",
    "?",
    "*",
    "+",
    ";",
    ":",
    ",",
    ".",
]  # Characters used for ASCII rendering


def renderVideoToAsciiJsonGzip(status_bar, progress_bar):
    """
    Convert a video to ASCII art, render audio to base64, and compress results to a JSON GZIP file.

    :param status_bar: Status bar widget to update the status message.
    :param progress_bar: Progress bar widget to update the progress percentage.
    """
    renderedFrames = []  # List to store rendered ASCII frames
    submittedThreads = []  # List to keep track of submitted threads for rendering
    videoObject = VideoObject.VideoObject(videoPath)  # Create a VideoObject instance

    status_bar.setText("Splitting Frames")  # Update status bar
    splitVideoIntoFrames(videoObject)  # Split video into individual frames
    status_bar.setText("Rendering Frames")  # Update status bar
    progress_bar.setProperty("value", 10)  # Update progress bar

    # Set up thread pool for parallel processing
    threadPool = ThreadPoolExecutor(numberOfThreads)
    tempFrames = os.listdir("../temp")  # List all temporary frame files
    tempFrames = natsorted(tempFrames, reverse=False)  # Sort frame files naturally

    # Split frame files list into chunks for parallel processing
    frameChunks = splitFramesList(tempFrames, numberOfThreads)

    # Submit rendering tasks to the thread pool
    x = 0
    while x < len(frameChunks):
        submittedThreads.append(
            threadPool.submit(
                renderFramesToAscii, frameChunks[x], asciiRenderWidth, ASCII_CHARS
            )
        )
        x += 1

    print(submittedThreads)

    # Collect results from threads and update progress
    i = 0
    for x in submittedThreads:
        renderedFrames.extend(x.result())
        i += 1
        value = round((i / len(submittedThreads)) * 80)
        if value > progress_bar.value():
            progress_bar.setProperty("value", round(value))
            print("progress:", round(value))

    threadPool.shutdown()  # Shut down the thread pool
    print(len(renderedFrames))
    videoObject.frames = renderedFrames  # Store rendered frames in video object
    status_bar.setText("Rendering Audio")  # Update status bar
    videoObject.base64Audio = renderBase64Audio(videoObject).decode(
        "utf-8"
    )  # Render audio to base64
    status_bar.setText("Compressing to Json Gzip")  # Update status bar
    progress_bar.setProperty("value", 90)  # Update progress bar
    makeJsonGzip(videoObject)  # Compress data to JSON GZIP
    progress_bar.setProperty("value", 100)  # Set progress to 100%


def renderFramesToAscii(submittedFrames, asciiRenderWidth, ASCII_CHARS=None):
    """
    Convert a list of frames to ASCII art.

    :param submittedFrames: List of frame filenames.
    :param asciiRenderWidth: Width of ASCII rendered output.
    :param ASCII_CHARS: List of ASCII characters used for rendering.
    :return: List of ASCII art strings for each frame.
    """
    print(submittedFrames)
    asciiFramesBuffer = []  # List to store ASCII art frames
    for frame in submittedFrames:
        print("current frame", frame)
        # Convert each frame to ASCII art
        asciiFramesBuffer.append(
            ImageToAscii.convert_Image_To_Ascii(
                f"../temp/" + frame, asciiRenderWidth, ASCII_CHARS=ASCII_CHARS
            )
        )
        os.remove(f"../temp/" + frame)  # Remove temporary frame file
    return asciiFramesBuffer


def splitVideoIntoFrames(videoObject):
    """
    Split a video into individual frames and save them as images.

    :param videoObject: VideoObject instance containing video path.
    """
    print("Splitting Frames")
    # Recreate temp directory to clear previous session files
    if os.path.exists("../temp"):
        shutil.rmtree("../temp")
    os.mkdir("../temp")
    capture = cv2.VideoCapture(videoObject.path)  # Open video file
    frameNr = 0
    while True:
        success, frame = capture.read()
        if success:
            cv2.imwrite(f"../temp/{frameNr}.jpg", frame)  # Save frame as image file
        else:
            break
        frameNr += 1
    capture.release()  # Release video capture object
    print("frames split")


def splitFramesList(framesList, number_of_parts_to_split_in=1):
    """
    Split a list of frames into specified number of parts.

    :param framesList: List of frame filenames.
    :param number_of_parts_to_split_in: Number of parts to split the list into.
    :return: List of lists, each containing a chunk of the original frame list.
    """
    length = len(framesList)
    return [
        framesList[
            i
            * length
            // number_of_parts_to_split_in : (i + 1)
            * length
            // number_of_parts_to_split_in
        ]
        for i in range(number_of_parts_to_split_in)
    ]


def renderBase64Audio(videoObject):
    """
    Extract audio from a video file, encode it in base64 format, and return it.

    :param videoObject: VideoObject instance containing video path.
    :return: Base64 encoded audio string.
    """
    print(videoObject.path)
    video = mvEditor.VideoFileClip(videoObject.path)  # Load video file
    video.audio.write_audiofile(
        "../temp/" + videoObject.filename + "_audio.mp3"
    )  # Extract audio and save as MP3

    # Encode audio file in base64
    with open(("../temp/" + videoObject.filename + "_audio.mp3"), "rb") as f:
        base64AudioString = base64.b64encode(f.read())
    print(sys.getsizeof(base64AudioString))
    print(len(base64AudioString))
    f.close()
    os.remove(
        "../temp/" + videoObject.filename + "_audio.mp3"
    )  # Remove temporary audio file

    return base64AudioString


def makeJsonGzip(videoObjectToWrite):
    """
    Compress video data into a JSON GZIP file.

    :param videoObjectToWrite: VideoObject instance with data to be written.
    """
    vidJsonObject = {
        "path": videoObjectToWrite.path,
        "filename": videoObjectToWrite.filename,
        "AsciiFrames": videoObjectToWrite.frames,
        "fps": videoObjectToWrite.fps,
        "renderChars": videoObjectToWrite.renderChars,
        "base64Audio": videoObjectToWrite.base64Audio,
    }

    # Create a JSON GZIP file with the same base name as the video file
    videoFilePath = videoObjectToWrite.path
    base = os.path.splitext(videoFilePath)[0]
    compress_json.dump(vidJsonObject, base + ".json.gz")

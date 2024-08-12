import os  # Module for interacting with the operating system
import cv2  # OpenCV library for video processing


class VideoObject:
    def __init__(self, path):
        """
        Initialize a VideoObject instance with video file properties.

        :param path: Path to the video file.
        """
        self.path = path  # Path to the video file
        self.filename = os.path.basename(path)  # Extract the filename from the path
        cap = cv2.VideoCapture(path)  # Open the video file using OpenCV
        self.numberOfFrames = int(
            cap.get(cv2.CAP_PROP_FRAME_COUNT)
        )  # Get the total number of frames in the video
        self.fps = float(
            cap.get(cv2.CAP_PROP_FPS)
        )  # Get the frames per second (FPS) of the video
        self.frames = []  # List to store frames if needed
        self.renderChars = ""  # Placeholder for rendering characters
        self.base64Audio = ""  # Placeholder for base64 encoded audio

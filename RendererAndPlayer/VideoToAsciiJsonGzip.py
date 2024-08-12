import os
import cv2
import sys
import time
import PyQt5
import shutil
import base64
import compress_json
from PyQt5 import QtWidgets
from natsort import natsort
import moviepy.editor as mvEditor
from RendererAndPlayer import VideoObject
from RendererAndPlayer import ImageToAscii
from concurrent.futures import ThreadPoolExecutor


videoPath = ""
asciiRenderWidth = 120
numberOfThreads = 64
ASCII_CHARS = ["@", "#", "＄", "%", "?", "*", "+", ";", ":", ",", "."]


def renderVideoToAsciiJsonGzip(status_bar, progress_bar):
    renderedFrames = []
    submittedThreads = []
    videoObject = VideoObject.VideoObject(videoPath)

    status_bar.setText("Splitting Frames")
    splitVideoIntoFrames(videoObject)
    status_bar.setText("Rendering Frames")
    progress_bar.setProperty("value", 10)

    threadPool = ThreadPoolExecutor(numberOfThreads)
    tempFrames = os.listdir("../temp")
    tempFrames = natsort.natsorted(tempFrames, reverse=False)

    frameChunks = splitFramesList(tempFrames, numberOfThreads)

    x = 0
    while x < len(frameChunks):
        submittedThreads.append(
            threadPool.submit(
                renderFramesToAscii, frameChunks[x], asciiRenderWidth, ASCII_CHARS
            )
        )
        x += 1

    print(submittedThreads)

    i = 0
    for x in submittedThreads:
        renderedFrames.extend(x.result())
        i += 1
        value = round((i / len(submittedThreads)) * 80)
        if value > progress_bar.value():
            progress_bar.setProperty("value", round(value))
            print("progress:", round(value))

    threadPool.shutdown()
    print(len(renderedFrames))
    videoObject.frames = renderedFrames
    status_bar.setText("Rendering Audio")
    videoObject.base64Audio = renderBase64Audio(videoObject).decode("utf-8")
    status_bar.setText("Compressing to Json Gzip")
    progress_bar.setProperty("value", 90)
    makeJsonGzip(videoObject)
    progress_bar.setProperty("value", 100)


def renderFramesToAscii(submittedFrames, asciiRenderWidth, ASCII_CHARS=None):
    print(submittedFrames)
    asciiFramesBuffer = []
    for frame in submittedFrames:
        print("current frame", frame)
        asciiFramesBuffer.append(
            ImageToAscii.convert_Image_To_Ascii(
                f"../temp/" + frame, asciiRenderWidth, ASCII_CHARS=ASCII_CHARS
            )
        )
        os.remove(f"../temp/" + frame)
    return asciiFramesBuffer


def splitVideoIntoFrames(videoObject):
    print("Splitting Frames")
    # recreating temp directory to clear everything from last session
    if os.path.exists("../temp"):
        shutil.rmtree("../temp")
    os.mkdir("../temp")
    capture = cv2.VideoCapture(videoObject.path)
    frameNr = 0
    while True:
        success, frame = capture.read()
        if success:
            cv2.imwrite(f"../temp/{frameNr}.jpg", frame)

        else:
            break
        frameNr = frameNr + 1
    capture.release()
    print("frames split")


def splitFramesList(framesList, number_of_parts_to_split_in=1):
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
    print(videoObject.path)
    video = mvEditor.VideoFileClip(videoObject.path)
    video.audio.write_audiofile("../temp/" + videoObject.filename + "_audio.mp3")

    with open(("../temp/" + videoObject.filename + "_audio.mp3"), "rb") as f:
        base64AudioString = base64.b64encode(f.read())
    print(sys.getsizeof(base64AudioString))
    print(len(base64AudioString))
    f.close()
    os.remove("../temp/" + videoObject.filename + "_audio.mp3")

    return base64AudioString


def makeJsonGzip(videoObjectToWrite):
    vidJsonObject = {
        "path": videoObjectToWrite.path,
        "filename": videoObjectToWrite.filename,
        "AsciiFrames": videoObjectToWrite.frames,
        "fps": videoObjectToWrite.fps,
        "renderChars": videoObjectToWrite.renderChars,
        "base64Audio": videoObjectToWrite.base64Audio,
    }

    # creating a file at same destination and same with a different extension
    videoFilePath = videoObjectToWrite.path
    base = os.path.splitext(videoFilePath)[0]
    compress_json.dump(vidJsonObject, base + ".json.gz")

import shutil  # Module for high-level file operations, like removing directories
import cv2  # OpenCV library for video processing
import sys  # Module for system-specific parameters and functions
import pygame  # Library for creating video games and multimedia applications
from pygame import (
    DOUBLEBUF,
    RESIZABLE,
    HWSURFACE,
    QUIT,
    display,
    K_ESCAPE,
)  # Import specific Pygame constants and functions

from RendererAndPlayer import ptext  # Import custom module for text rendering
from RendererAndPlayer import (
    ImageToAscii,
)  # Import custom module for image-to-ASCII conversion
from RendererAndPlayer.VideoObject import VideoObject  # Import custom VideoObject class
import os  # Module for interacting with the operating system


class RealTimeAsciiVideoPlayer:
    def __init__(self):
        """
        Initialize the real-time ASCII video player.
        Sets up Pygame, screen properties, fonts, and other configurations.
        """
        pygame.init()  # Initialize Pygame
        pygame.font.init()  # Initialize Pygame fonts
        self.background_colour = (30, 30, 30)  # Background color of the display
        self.SCREEN_WIDTH = 1280  # Width of the display screen
        self.SCREEN_HEIGHT = 720  # Height of the display screen
        self.screen = pygame.display.set_mode(
            (self.SCREEN_WIDTH, self.SCREEN_HEIGHT),
            pygame.RESIZABLE,  # Allow window resizing
            HWSURFACE | DOUBLEBUF | RESIZABLE,  # Set display flags
            vsync=1,  # Enable vertical sync to prevent screen tearing
        )

        self.screen.fill(
            self.background_colour
        )  # Fill the screen with the background color
        pygame.display.set_caption("ASCII Nova")  # Set the window title
        pygame.display.flip()  # Update the display
        self.fps_count_render_font = pygame.font.Font(
            "./fonts_dir/courier.ttf", 16
        )  # Font for displaying FPS
        self.media_controls_render_font = pygame.font.Font(
            "./fonts_dir/courier.ttf", 12
        )  # Font for media controls
        self.clock = pygame.time.Clock()  # Create a clock object to manage frame rate
        self.playback_paused = False  # Flag to indicate whether playback is paused

        self.fps_lock = 30  # Target frames per second

        ######################
        # Configuration parameters for rendering
        self.fontColorHex = "#FFFFFF"  # Font color for ASCII characters
        self.fontSize = 14  # Font size for ASCII characters
        self.lineHeight = 1  # Line height for ASCII characters
        self.showFpsSwitch = True  # Toggle for displaying FPS
        self.ascii_render_font_name = (
            "./fonts_dir/courier.ttf'"  # Font name for rendering ASCII
        )
        self.ascii_Chars = [
            "@",
            "#",
            "S",
            "%",
            "?",
            "*",
            "+",
            ";",
            ":",
            ",",
            ".",
        ]  # ASCII characters used for rendering
        self.renderTextWidth = 120  # Width of the ASCII text
        self.videoPath = ""  # Path to the video file

        self.fullScreen = (
            False  # Flag to indicate whether the display is in full screen mode
        )

    ######################
    def RTplayVideoAscii(self):
        """
        Start playing the video in ASCII art format.
        """
        videoToRenderInAscii = VideoObject(
            self.videoPath
        )  # Create a VideoObject instance
        print(videoToRenderInAscii.path)  # Print the video path for debugging
        pygame.init()  # Initialize Pygame again
        print("Init")
        self.renderFrames(videoToRenderInAscii)  # Start rendering video frames

    def renderFrames(self, videoObject):
        """
        Process and render each frame of the video as ASCII art.

        :param videoObject: VideoObject instance containing video path and properties.
        """
        print("Splitting Frames")
        # Recreate temp directory to clear any previous files
        if os.path.exists("../temp"):
            shutil.rmtree("../temp")
        os.mkdir("../temp")  # Create a new temporary directory for frame images
        capture = cv2.VideoCapture(videoObject.path)  # Open the video file using OpenCV
        frameNr = 0  # Frame number counter

        # Track double-click event for fullscreen toggle
        last_click_time = 0
        double_click_interval = (
            400  # Time interval for detecting double-click (in milliseconds)
        )

        try:
            while True:
                if not self.playback_paused:
                    success, frame = capture.read()  # Read a frame from the video
                    if success:
                        cv2.imwrite(
                            f"../temp/{frameNr}.jpg", frame
                        )  # Save the frame as an image file
                        frame = ImageToAscii.convert_Image_To_Ascii(
                            f"../temp/{frameNr}.jpg",
                            self.renderTextWidth,
                            ASCII_CHARS=self.ascii_Chars,
                        )  # Convert the image to ASCII art
                        self.renderFrameOnScreen(
                            frame,
                            videoObject.fps,
                            self.fontColorHex,
                            self.fontSize,
                            self.lineHeight,
                            self.showFpsSwitch,
                            self.ascii_render_font_name,
                        )  # Render the ASCII frame on screen
                        os.remove(
                            f"../temp/{frameNr}.jpg"
                        )  # Remove the temporary image file
                    else:
                        break  # Exit loop if no more frames

                    frameNr += 1  # Increment the frame number

                for event in pygame.event.get():
                    # Handle media control events
                    pygame.event.pump()  # Process event queue
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_k:  # Toggle pause/unpause
                            if not self.playback_paused:
                                self.playback_paused = True
                                pygame.mixer.music.pause()  # Pause music playback if any
                                print("Paused")
                            else:
                                self.playback_paused = False
                                pygame.mixer.music.unpause()  # Resume music playback if any
                                print("UnPaused")
                        if event.key == K_ESCAPE and self.fullScreen:
                            # Exit fullscreen mode
                            pygame.display.quit()
                            pygame.init()
                            self.screen = pygame.display.set_mode(
                                (self.SCREEN_WIDTH, self.SCREEN_HEIGHT),
                                pygame.RESIZABLE,
                                HWSURFACE | DOUBLEBUF | RESIZABLE,
                                vsync=1,
                            )
                            self.fullScreen = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # Handle mouse click events
                        if event.button == 1:
                            print("click registered")
                            if (
                                pygame.time.get_ticks() - last_click_time
                                < double_click_interval
                            ):
                                if not self.fullScreen:
                                    # Toggle fullscreen mode on double-click
                                    self.screen = pygame.display.set_mode(
                                        (0, 0),
                                        pygame.FULLSCREEN,
                                        HWSURFACE | DOUBLEBUF,
                                        vsync=1,
                                    )
                                    self.fullScreen = True
                            last_click_time = pygame.time.get_ticks()

                    if event.type == QUIT:
                        # Handle quit event
                        pygame.display.quit()
                        return
        except pygame.error as e:
            # Handle Pygame errors
            if e.args[0] == "video system not initialized":
                print("Error: Video system not initialized")
                sys.exit(0)
            elif e.args[0] == "display Surface quit":
                print("Error: Display windows was quit")
                sys.exit(0)
        finally:
            # Clean up resources
            pygame.display.quit()
            capture.release()
            return

    def render_overlay(self, show_fps_switch=True):
        """
        Render an overlay for media controls and FPS.

        :param show_fps_switch: Boolean to determine whether to display FPS.
        """
        if show_fps_switch:
            overlay_surface = pygame.Surface(
                (140, 40)
            )  # Create an overlay surface with dimensions
        else:
            overlay_surface = pygame.Surface((140, 20))

        if not self.fullScreen:
            if show_fps_switch:
                overlay_surface = pygame.Surface((140, 40))
            else:
                overlay_surface = pygame.Surface((140, 20))
        else:
            if show_fps_switch:
                overlay_surface = pygame.Surface((300, 40))
            else:
                overlay_surface = pygame.Surface((300, 20))

        overlay_surface.set_colorkey((0, 0, 0))  # Set the color key for transparency
        pygame.draw.rect(
            overlay_surface, (30, 30, 20), overlay_surface.get_rect(), border_radius=6
        )  # Draw a rectangle with rounded corners

        # Render media controls text
        if not self.fullScreen:
            media_controls_text = "K - Pause/Unpause"
        else:
            media_controls_text = "K - Pause/Unpause    Esc - Exit Full screen"
        media_controls_surface = self.media_controls_render_font.render(
            media_controls_text, True, (255, 255, 255)
        )
        overlay_surface.blit(
            media_controls_surface, (5, 5)
        )  # Draw the media controls text onto the overlay

        # Render FPS text if enabled
        if show_fps_switch:
            fps_text = str(int(self.clock.get_fps()))
            fps_surface = self.fps_count_render_font.render(
                "fps: " + fps_text, True, (255, 255, 255)
            )
            overlay_surface.blit(
                fps_surface, (5, 20)
            )  # Draw the FPS text onto the overlay

        self.screen.blit(
            overlay_surface, (self.screen.get_rect().left + 10, 10)
        )  # Draw the overlay on the screen

    def renderFrameOnScreen(
        self,
        asciiFrameString,
        fpsLockValue=30,
        fontColorHex="#FFFFFF",
        fontSize=14,
        lineheight=1,
        showFpsSwitch=True,
        ascii_render_font_name="./fonts_dir/courier.ttf'",
    ):
        """
        Render an ASCII frame string onto the screen.

        :param asciiFrameString: String containing ASCII art to be rendered.
        :param fpsLockValue: Target frames per second for synchronization.
        :param fontColorHex: Hex color code for ASCII font color.
        :param fontSize: Size of the ASCII font.
        :param lineheight: Line height for ASCII text.
        :param showFpsSwitch: Boolean to determine whether to display FPS.
        :param ascii_render_font_name: Path to the font file for rendering ASCII.
        """
        try:
            # Render the ASCII frame string
            if not self.playback_paused:
                self.screen.fill(
                    self.background_colour
                )  # Fill the screen with the background color
                ptext.draw_in_exact_center(
                    asciiFrameString,
                    self.screen,
                    0,
                    10,
                    (500, 100),
                    fontname=ascii_render_font_name,
                    fontsize=fontSize,
                    lineheight=lineheight,
                    width=10,
                    color=fontColorHex,
                )  # Draw the ASCII text centered on the screen

                self.clock.tick(
                    fpsLockValue
                )  # Control the frame rate to match the target FPS

                self.render_overlay(
                    showFpsSwitch
                )  # Render the overlay (media controls and FPS)

                display.flip()  # Update the display
        except pygame.error as e:
            # Handle Pygame errors
            if e.args[0] == "display Surface quit":
                print("Error: Display windows was quit")
                sys.exit(0)

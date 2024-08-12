import compress_json  # For handling compressed JSON files
import base64  # For encoding and decoding binary data
import os  # For interacting with the operating system
import sys  # For system-specific parameters and functions
from math import floor  # For mathematical operations

import pygame  # For creating video games and multimedia applications
from pygame import (
    DOUBLEBUF,
    RESIZABLE,
    HWSURFACE,
    QUIT,
    display,
    K_ESCAPE,
    K_F11,
)  # Pygame constants and functions

from RendererAndPlayer import (
    ptext,
)  # Custom module for text rendering | modified originally from https://github.com/cosmologicon/pygame-text


class AsciiVideoPlayer:
    def __init__(self):
        """
        Initialize the ASCII video player with Pygame settings and fonts.
        """
        pygame.init()
        pygame.font.init()

        # Set background color and screen dimensions
        self.background_colour = (30, 30, 30)
        self.SCREEN_WIDTH = 1280
        self.SCREEN_HEIGHT = 720

        # Initialize the display window with specific settings
        self.screen = pygame.display.set_mode(
            (self.SCREEN_WIDTH, self.SCREEN_HEIGHT),
            pygame.RESIZABLE,
            HWSURFACE | DOUBLEBUF | RESIZABLE,
            vsync=1,
        )
        self.screen.fill(self.background_colour)

        # Set window title and refresh display
        pygame.display.set_caption("ASCII Nova")
        pygame.display.flip()

        # Load fonts for rendering text on screen
        self.fps_count_render_font = pygame.font.Font("./fonts_dir/courier.ttf", 16)
        self.media_controls_render_font = pygame.font.Font(
            "./fonts_dir/courier.ttf", 12
        )

        self.clock = pygame.time.Clock()

        # Default settings for rendering ASCII video
        self.fontColorHex = "#FFFFFF"
        self.fontSize = 8
        self.lineHeight = 1.0
        self.showFpsSwitch = True
        self.ascii_render_fontName = "./fonts_dir/courier.ttf"

        self.fullScreen = False

    def renderAudio(self, asciiVideoDict):
        """
        Decode and save the audio from the ASCII video dictionary.

        :param asciiVideoDict: Dictionary containing base64 encoded audio data
        """
        b = base64.b64decode(asciiVideoDict["base64Audio"])

        try:
            # Save the decoded audio as an MP3 file
            file = open(
                "../temp/" + asciiVideoDict["filename"] + "_audio_decoded.mp3", "wb"
            )
            file.write(b)
            file.close()
        except Exception as e:
            print(e)
            sys.exit(0)

    def playAsciiVideo(self, gzippedJsonfile_path):
        """
        Load the compressed JSON file and play the ASCII video.

        :param gzippedJsonfile_path: Path to the gzipped JSON file containing ASCII video data
        """
        # Load the compressed JSON file as a dictionary
        asciiVideoDict = compress_json.load(gzippedJsonfile_path)

        # Render the audio and frames on the screen
        self.renderAudio(asciiVideoDict)
        self.renderFramesOnScreen(
            asciiVideoDict,
            fontColorHex=self.fontColorHex,
            fontSize=self.fontSize,
            lineheight=self.lineHeight,
            showFpsSwitch=self.showFpsSwitch,
            ascii_render_font_name=self.ascii_render_fontName,
        )

    def initializeMediaControls(self, asciiVideoDict):
        """
        Initialize media controls and play the audio for the ASCII video.

        :param asciiVideoDict: Dictionary containing ASCII video data and audio
        """
        try:
            # Decode and save the audio
            file = open(
                "../temp/" + asciiVideoDict["filename"] + "_audio_decoded.mp3", "wb"
            )
            file.write(base64.b64decode(asciiVideoDict["base64Audio"]))
            file.close()
        except Exception as e:
            print(e)
            sys.exit(0)

        # Load and play the audio with Pygame's mixer
        pygame.mixer.music.load(
            "../temp/" + asciiVideoDict["filename"] + "_audio_decoded.mp3"
        )
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(1.0)

    def render_overlay(self, show_fps_switch=True):
        """
        Render an overlay on the screen, including media controls and FPS.

        :param show_fps_switch: Boolean to show or hide FPS on the overlay
        """
        # Adjust overlay surface size based on screen mode (fullscreen or windowed)
        if not self.fullScreen:
            overlay_surface = (
                pygame.Surface((700, 40))
                if show_fps_switch
                else pygame.Surface((700, 20))
            )
        else:
            overlay_surface = (
                pygame.Surface((870, 40))
                if show_fps_switch
                else pygame.Surface((870, 20))
            )

        overlay_surface.set_alpha(200)
        overlay_surface.set_colorkey(
            (0, 0, 0)
        )  # Set transparent background for the overlay
        pygame.draw.rect(
            overlay_surface, (30, 30, 20), overlay_surface.get_rect(), border_radius=8
        )  # Set the color and border radius for the overlay

        # Media controls text
        media_controls_text = "J - FastBackward(10s)     L - FastForward(10s)   K - Pause/Unpause   M - Mute/Unmute   R - Replay"
        if self.fullScreen:
            media_controls_text += "    Esc - Exit Full screen"
        media_controls_surface = self.media_controls_render_font.render(
            media_controls_text, True, (255, 255, 255)
        )
        overlay_surface.blit(
            media_controls_surface, (5, 5)
        )  # Position the media controls text on the overlay

        # FPS text
        if show_fps_switch:
            fps_text = str(int(self.clock.get_fps()))
            fps_surface = self.fps_count_render_font.render(
                "fps: " + fps_text, True, (255, 255, 255)
            )
            overlay_surface.blit(fps_surface, (5, 20))

        # Display the overlay on the screen
        self.screen.blit(overlay_surface, (self.screen.get_rect().left + 10, 10))

    def renderFramesOnScreen(
        self,
        asciiVideoDict,
        fontColorHex="#FFFFFF",
        fontSize=14,
        lineheight=1.0,
        showFpsSwitch=True,
        ascii_render_font_name="./fonts_dir/courier.ttf",
    ):
        """
        Render ASCII frames on the screen and synchronize with the audio.

        :param asciiVideoDict: Dictionary containing ASCII video data
        :param fontColorHex: Font color in hexadecimal
        :param fontSize: Font size for rendering ASCII characters
        :param lineheight: Line height for rendering text
        :param showFpsSwitch: Boolean to show or hide FPS on the screen
        :param ascii_render_font_name: Font name for rendering ASCII characters
        """
        # Get the length of the audio in seconds
        music_length = pygame.mixer.Sound(
            "../temp/" + asciiVideoDict["filename"] + "_audio_decoded.mp3"
        ).get_length()
        print(music_length)

        FPS_LOCK_VALUE = asciiVideoDict["fps"]  # Lock the FPS to the video's FPS
        frameIndex = 0
        pygame.init()
        self.initializeMediaControls(asciiVideoDict)

        # Track double-click events for toggling fullscreen mode
        last_click_time = 0
        double_click_interval = 400  # milliseconds

        running = True
        playback_paused = False
        print("Running")

        try:
            # Game loop for rendering frames
            while running:
                if not playback_paused:
                    self.screen.fill(
                        self.background_colour
                    )  # Fill background on resize/refresh
                    if frameIndex < len(asciiVideoDict["AsciiFrames"]):
                        frameIndex += 1

                self.screen.fill(self.background_colour)

                # Draw ASCII frames on the screen
                if frameIndex < len(asciiVideoDict["AsciiFrames"]):
                    ptext.draw_in_exact_center(
                        asciiVideoDict["AsciiFrames"][frameIndex],
                        self.screen,
                        0,
                        10,
                        (500, 100),
                        fontname=ascii_render_font_name,
                        fontsize=fontSize,
                        lineheight=lineheight,
                        width=10,
                        color=fontColorHex,
                    )

                self.clock.tick(FPS_LOCK_VALUE)  # Maintain constant FPS
                self.render_overlay(showFpsSwitch)  # Render the overlay

                display.flip()  # Update the display

                # Handle user input events
                for event in pygame.event.get():
                    pygame.event.pump()  # Update internal event queue
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_m:  # Mute/Unmute audio
                            if pygame.mixer.music.get_volume() == 0.0:
                                pygame.mixer.music.set_volume(1.0)
                            elif pygame.mixer.music.get_volume() == 1.0:
                                pygame.mixer.music.set_volume(0.0)
                        if event.key == pygame.K_j:  # Fast-backward 10 seconds
                            frameIndex = frameIndex - int(FPS_LOCK_VALUE) * 10
                            newPos = floor(frameIndex / FPS_LOCK_VALUE) - 10
                            if frameIndex < 0:
                                newPos = 0
                                frameIndex = 0
                            pygame.mixer.music.set_pos(newPos)
                        if event.key == pygame.K_k:  # Pause/Unpause playback
                            playback_paused = not playback_paused
                            if playback_paused:
                                pygame.mixer.music.pause()
                            else:
                                pygame.mixer.music.unpause()
                        if event.key == pygame.K_l:  # Fast-forward 10 seconds
                            frameIndex = frameIndex + int(FPS_LOCK_VALUE) * 10
                            newPos = floor(frameIndex / FPS_LOCK_VALUE) + 10
                            if frameIndex >= len(asciiVideoDict["AsciiFrames"]):
                                newPos = music_length
                                frameIndex = len(asciiVideoDict["AsciiFrames"]) - 1
                            pygame.mixer.music.set_pos(newPos)
                        if event.key == pygame.K_r:  # Restart playback
                            frameIndex = 0
                            pygame.mixer.music.rewind()
                        if event.key == pygame.K_ESCAPE:  # Exit fullscreen mode
                            if self.fullScreen:
                                pygame.display.set_mode(
                                    (self.SCREEN_WIDTH, self.SCREEN_HEIGHT),
                                    RESIZABLE,
                                    HWSURFACE | DOUBLEBUF | RESIZABLE,
                                    vsync=1,
                                )
                                self.fullScreen = False
                        if event.key == pygame.K_f:  # Toggle fullscreen mode
                            self.fullScreen = not self.fullScreen
                            if self.fullScreen:
                                pygame.display.set_mode(
                                    (self.SCREEN_WIDTH, self.SCREEN_HEIGHT),
                                    pygame.FULLSCREEN | DOUBLEBUF | RESIZABLE,
                                    vsync=1,
                                )
                            else:
                                pygame.display.set_mode(
                                    (self.SCREEN_WIDTH, self.SCREEN_HEIGHT),
                                    pygame.RESIZABLE,
                                    HWSURFACE | DOUBLEBUF | RESIZABLE,
                                    vsync=1,
                                )

                    if event.type == pygame.QUIT:  # Exit the player
                        pygame.quit()
                        sys.exit(0)

                    if (
                        event.type == pygame.MOUSEBUTTONDOWN
                    ):  # Handle mouse double-click
                        current_time = pygame.time.get_ticks()
                        if current_time - last_click_time < double_click_interval:
                            if not self.fullScreen:
                                pygame.display.set_mode(
                                    (self.SCREEN_WIDTH, self.SCREEN_HEIGHT),
                                    pygame.FULLSCREEN | DOUBLEBUF | RESIZABLE,
                                    vsync=1,
                                )
                                self.fullScreen = True
                            else:
                                pygame.display.set_mode(
                                    (self.SCREEN_WIDTH, self.SCREEN_HEIGHT),
                                    RESIZABLE,
                                    HWSURFACE | DOUBLEBUF | RESIZABLE,
                                    vsync=1,
                                )
                                self.fullScreen = False
                        last_click_time = current_time

                if frameIndex >= len(asciiVideoDict["AsciiFrames"]):
                    running = False  # Stop the loop if the frame index exceeds the number of frames
        except pygame.error as e:
            if e.args[0] == "video system not initialized":
                print("Error: Video system not initialized")
                sys.exit(0)  # Exit the program if the video system is not initialized
            elif e.args[0] == "display Surface quit":
                print("Error: Display window was quit")
                sys.exit(0)  # Exit the program if the display window was quit
        finally:
            pygame.display.quit()  # Quit the pygame display
            if pygame.mixer.get_init():  # Check if the mixer is initialized
                pygame.mixer.music.unload()  # Unload the music if the mixer is initialized
            os.remove(
                "../temp/" + asciiVideoDict["filename"] + "_audio_decoded.mp3"
            )  # Remove the temporary audio file
            return  # Return from the function

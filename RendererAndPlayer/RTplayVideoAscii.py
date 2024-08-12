import shutil
import cv2
import sys
import pygame
from pygame import DOUBLEBUF, RESIZABLE, HWSURFACE, QUIT, display, K_ESCAPE

from RendererAndPlayer import ptext
from RendererAndPlayer import ImageToAscii
from RendererAndPlayer.VideoObject import VideoObject
import os


class RealTimeAsciiVideoPlayer():
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.background_colour = (30, 30, 30)
        self.SCREEN_WIDTH = 1280
        self.SCREEN_HEIGHT = 720
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), pygame.RESIZABLE,
                                              HWSURFACE | DOUBLEBUF | RESIZABLE, vsync=1)

        self.screen.fill(self.background_colour)
        pygame.display.set_caption('ASCII Nova')
        pygame.display.flip()
        self.fps_count_render_font = pygame.font.Font('../fonts[place fonts to use here]/courier.ttf', 16)
        self.media_controls_render_font = pygame.font.Font('../fonts[place fonts to use here]/courier.ttf', 12)
        self.clock = pygame.time.Clock()
        self.playback_paused = False

        self.fps_lock = 30

        ######################
        self.fontColorHex = "#FFFFFF"
        self.fontSize = 14
        self.lineHeight = 1
        self.showFpsSwitch = True
        self.ascii_render_font_name = "../fonts[place fonts to use here]/courier.ttf"
        self.ascii_Chars = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']
        self.renderTextWidth = 120
        self.videoPath = ""

        self.fullScreen = False

    ######################
    def RTplayVideoAscii(self):
        videoToRenderInAscii = VideoObject(self.videoPath)
        print(videoToRenderInAscii.path)
        pygame.init()
        print("Init")
        self.renderFrames(videoToRenderInAscii)

    def renderFrames(self, videoObject):
        print("Splitting Frames")
        # recreating temp directory to clear everything from last session
        if os.path.exists('../temp'):
            shutil.rmtree('../temp')
        os.mkdir('../temp')
        capture = cv2.VideoCapture(videoObject.path)
        frameNr = 0

        # Track double-click event
        last_click_time = 0
        double_click_interval = 400  # milliseconds

        try:
            while True:

                if self.playback_paused is False:
                    success, frame = capture.read()
                    if success:
                        cv2.imwrite(f'../temp/{frameNr}.jpg', frame)
                        frame = ImageToAscii.convert_Image_To_Ascii(f'../temp/{frameNr}.jpg', self.renderTextWidth,
                                                                    ASCII_CHARS=self.ascii_Chars)
                        self.renderFrameOnScreen(frame, videoObject.fps, self.fontColorHex, self.fontSize,
                                                 self.lineHeight,
                                                 self.showFpsSwitch, self.ascii_render_font_name)
                        os.remove(f'../temp/{frameNr}.jpg')
                    else:
                        break

                    frameNr = frameNr + 1

                for event in pygame.event.get():
                    # Check for media control key events
                    pygame.event.pump()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_k:  # pause/upause
                            if self.playback_paused is False:
                                self.playback_paused = True
                                pygame.mixer.music.pause()
                                print("Paused")
                            elif self.playback_paused is True:
                                self.playback_paused = False
                                pygame.mixer.music.unpause()
                                print("UnPaused")
                            print('K')
                            # resize screen on key events
                        if event.key == K_ESCAPE and self.fullScreen:
                            pygame.display.quit()
                            pygame.init()
                            self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT),
                                                                  pygame.RESIZABLE,
                                                                  HWSURFACE | DOUBLEBUF | RESIZABLE, vsync=1)
                            self.fullScreen = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # resize screen on key events
                        if event.button == 1:
                            print("click registered")
                            if pygame.time.get_ticks() - last_click_time < double_click_interval:
                                if not self.fullScreen:
                                    self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN,
                                                                          HWSURFACE | DOUBLEBUF, vsync=1)
                                    self.fullScreen = True
                            last_click_time = pygame.time.get_ticks()

                            # Check for QUIT event

                    # Check for QUIT event
                    if event.type == QUIT:
                        pygame.display.quit()
                        return
        except pygame.error as e:
            if e.args[0] == 'video system not initialized':
                print("Error: Video system not initialized")
                sys.exit(0)
            elif e.args[0] == 'display Surface quit':
                print("Error: Display windows was quit")
                sys.exit(0)
        finally:
            pygame.display.quit()
            capture.release()
            return

    def render_overlay(self, show_fps_switch=True):
        if show_fps_switch:
            overlay_surface = pygame.Surface((140, 40))
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

        overlay_surface.set_colorkey((0, 0, 0))  # Set the background color of the overlay as transparent
        pygame.draw.rect(overlay_surface, (30, 30, 20), overlay_surface.get_rect(),
                         border_radius=6)  # Set the color and border radius

        if not self.fullScreen:
            media_controls_text = 'K - Pause/Unpause'
        else:
            media_controls_text = 'K - Pause/Unpause    Esc - Exit Full screen'
        media_controls_surface = self.media_controls_render_font.render(media_controls_text, True, (255, 255, 255))
        overlay_surface.blit(media_controls_surface, (5, 5))  # Customize the position of the media controls text

        if show_fps_switch:
            fps_text = str(int(self.clock.get_fps()))
            fps_surface = self.fps_count_render_font.render('fps: ' + fps_text, True, (255, 255, 255))
            overlay_surface.blit(fps_surface, (5, 20))  # Customize the position of the FPS text

        self.screen.blit(overlay_surface, (self.screen.get_rect().left + 10, 10))

    def renderFrameOnScreen(self, asciiFrameString, fpsLockValue=30, fontColorHex="#FFFFFF", fontSize=14, lineheight=1,
                            showFpsSwitch=True,
                            ascii_render_font_name="fonts[place fonts to use here]/courier.ttf"):
        try:
            # game loop

            if self.playback_paused is True:
                pass
            elif self.playback_paused is False:
                self.screen.fill(self.background_colour)  # filling background on resize/refresh
                ptext.draw_in_exact_center(asciiFrameString, self.screen, 0, 10, (500, 100),
                                           fontname=ascii_render_font_name,
                                           fontsize=fontSize,
                                           lineheight=lineheight, width=10, color=fontColorHex)

                self.clock.tick(fpsLockValue)  # making fps constant(synced to original video's fps)

                self.render_overlay(showFpsSwitch)

                display.flip()  # to update display
        except pygame.error as e:
            if e.args[0] == 'display Surface quit':
                print("Error: Display windows was quit")
                sys.exit(0)

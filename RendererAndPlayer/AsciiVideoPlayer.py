import compress_json
import base64
import os
import sys
from math import floor

import pygame
from pygame import DOUBLEBUF, RESIZABLE, HWSURFACE, QUIT, display, K_ESCAPE, K_F11

from RendererAndPlayer import ptext


class AsciiVideoPlayer():
    def __init__(self):

        pygame.init()
        pygame.font.init()

        self.background_colour = (30, 30, 30)

        # screen = pygame.display.set_mode((1024, 768), pygame.RESIZABLE, vsync=1)
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

        self.fontColorHex = "#FFFFFF"
        self.fontSize = 8
        self.lineHeight = 1.0
        self.showFpsSwitch = True
        self.ascii_render_fontName = "../fonts[place fonts to use here]/courier.ttf"

        self.fullScreen = False

    def renderAudio(self, asciiVideoDict):
        # f = open("temp/" + "BadAppleForPython2.mp4_audio_encoded" + '.txt', 'rb')
        b = base64.b64decode(asciiVideoDict['base64Audio'])
        # f.close()

        try:
            file = open("../temp/" + asciiVideoDict['filename'] + '_audio_decoded.mp3', 'wb')
            file.write(b)
            file.close()
        except Exception as e:
            print(e)
            sys.exit(0)

    def playAsciiVideo(self, gzippedJsonfile_path):
        asciiVideoDict = compress_json.load(gzippedJsonfile_path)  # loads json as a dictionary

        self.renderAudio(asciiVideoDict)
        self.renderFramesOnScreen(asciiVideoDict, fontColorHex=self.fontColorHex, fontSize=self.fontSize,
                                  lineheight=self.lineHeight,
                                  showFpsSwitch=self.showFpsSwitch,
                                  ascii_render_font_name=self.ascii_render_fontName)

    def initializeMediaControls(self, asciiVideoDict):
        try:
            file = open("../temp/" + asciiVideoDict['filename'] + '_audio_decoded.mp3', 'wb')
            file.write(base64.b64decode(asciiVideoDict['base64Audio']))
            file.close()
        except Exception as e:
            print(e)
            sys.exit(0)

        pygame.mixer.music.load("../temp/" + asciiVideoDict['filename'] + '_audio_decoded.mp3')
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(1.0)



    def render_overlay(self, show_fps_switch=True):
        if not self.fullScreen:
            if show_fps_switch:
                overlay_surface = pygame.Surface((700, 40))
            else:
                overlay_surface = pygame.Surface((700, 20))
        else:
            if show_fps_switch:
                overlay_surface = pygame.Surface((870, 40))
            else:
                overlay_surface = pygame.Surface((870, 20))

        overlay_surface.set_alpha(200)
        overlay_surface.set_colorkey((0, 0, 0))  # Set the background color of the overlay as transparent
        pygame.draw.rect(overlay_surface, (30, 30, 20), overlay_surface.get_rect(),
                         border_radius=8)  # Set the color and border radius

        if not self.fullScreen:
            media_controls_text = 'J - FastBackward(10s)     L - FastForward(10s)   K - Pause/Unpause   M - Mute/Unmute   R - Replay'
        else:
            media_controls_text = 'J - FastBackward(10s)     L - FastForward(10s)   K - Pause/Unpause   M - Mute/Unmute   R - Replay    Esc - Exit Full screen'
        media_controls_surface = self.media_controls_render_font.render(media_controls_text, True, (255, 255, 255))
        overlay_surface.blit(media_controls_surface, (5, 5))  # Customize the position of the media controls text

        if show_fps_switch:
            fps_text = str(int(self.clock.get_fps()))
            fps_surface = self.fps_count_render_font.render('fps: ' + fps_text, True, (255, 255, 255))
            overlay_surface.blit(fps_surface, (5, 20))  # Customize the position of the FPS text

        self.screen.blit(overlay_surface,
                         (self.screen.get_rect().left + 10,
                          10))  # Customize the position of the overlay surface on the screen

    #
    # pygame.mixer.music.unload()

    def renderFramesOnScreen(self, asciiVideoDict, fontColorHex="#FFFFFF", fontSize=14, lineheight=1.0,
                             showFpsSwitch=True,
                             ascii_render_font_name="../fonts[place fonts to use here]/courier.ttf"):
        music_length = pygame.mixer.Sound("../temp/" + asciiVideoDict['filename'] + '_audio_decoded.mp3').get_length()
        print(music_length)
        FPS_LOCK_VALUE = asciiVideoDict['fps']
        frameIndex = 0
        pygame.init()
        self.initializeMediaControls(asciiVideoDict)

        # Track double-click event
        last_click_time = 0
        double_click_interval = 400  # milliseconds

        running = True
        playback_paused = False
        print("Running")
        try:
            # game loop
            while running:
                if playback_paused is True:
                    pass
                elif playback_paused is False:
                    self.screen.fill(self.background_colour)  # filling background on resize/refresh
                    if frameIndex < len(asciiVideoDict['AsciiFrames']):
                        frameIndex += 1

                self.screen.fill(self.background_colour)  # filling background on resize/refresh

                if frameIndex < len(asciiVideoDict['AsciiFrames']):
                    ptext.draw_in_exact_center(asciiVideoDict['AsciiFrames'][frameIndex], self.screen, 0, 10, (500, 100),
                                               fontname=ascii_render_font_name,
                                               fontsize=fontSize,
                                               lineheight=lineheight, width=10, color=fontColorHex)

                self.clock.tick(FPS_LOCK_VALUE)  # making fps constant(synced to original video's fps)
                self.render_overlay(showFpsSwitch)

                display.flip()  # to update display

                # keys = pygame.key.get_pressed()
                for event in pygame.event.get():
                    # Check for media control key events
                    pygame.event.pump()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_m:  # mute/unmute
                            print("M pressed")
                            print(pygame.mixer.music.get_volume())
                            if pygame.mixer.music.get_volume() == 0.0:
                                pygame.mixer.music.set_volume(1.0)
                                print('Unmuted')
                            elif pygame.mixer.music.get_volume() == 1.0:
                                pygame.mixer.music.set_volume(0.0)
                                print('Muted')
                        if event.key == pygame.K_j:  # fast-backward
                            frameIndex = frameIndex - int(FPS_LOCK_VALUE) * 10
                            newPos = floor(frameIndex / FPS_LOCK_VALUE) - 10
                            print("back by: ", newPos)
                            if frameIndex < 0:
                                newPos = 0
                                pygame.mixer.music.set_pos(newPos)
                                frameIndex = 0
                            else:
                                pygame.mixer.music.set_pos(newPos)
                            print("Fast Backwarded 10s")
                            print('J')
                        if event.key == pygame.K_k:  # pause/upause
                            if playback_paused is False:
                                playback_paused = True
                                pygame.mixer.music.pause()
                                print("Paused")
                            elif playback_paused is True:
                                playback_paused = False
                                pygame.mixer.music.unpause()
                                print("UnPaused")
                            print('K')
                        if event.key == pygame.K_l:  # fast-forward
                            frameIndex = frameIndex + int(FPS_LOCK_VALUE) * 10
                            newPos = floor(frameIndex / FPS_LOCK_VALUE) + 10
                            print("forward by: ", newPos)
                            if frameIndex > len(asciiVideoDict['AsciiFrames']):
                                pygame.mixer.music.unload()
                                frameIndex = len(asciiVideoDict['AsciiFrames'])
                            else:
                                pygame.mixer.music.set_pos(newPos)

                            print("Fast Forwarded 10s")
                            print('L')
                        if event.key == pygame.K_r:  # replay
                            frameIndex = 0
                            pygame.mixer.music.set_pos(0)
                            print('Replayed')

                        # resize screen on key events
                        if event.key == K_ESCAPE and self.fullScreen:
                            pygame.display.quit()
                            pygame.init()
                            self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), pygame.RESIZABLE,
                                                             HWSURFACE | DOUBLEBUF | RESIZABLE, vsync=1)

                            self.fullScreen = False
                    if event.type == pygame.MOUSEBUTTONDOWN:

                        # resize screen on key events
                        if event.button == 1:
                            print("click registered")
                            if pygame.time.get_ticks() - last_click_time < double_click_interval:
                                if not self.fullScreen:
                                    self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN,
                                                                     HWSURFACE | DOUBLEBUF | RESIZABLE, vsync=1)
                                    self.fullScreen = True
                            last_click_time = pygame.time.get_ticks()
                    # Check for QUIT event
                    if event.type == QUIT:
                        pygame.display.quit()
                        return
                if frameIndex >= len(asciiVideoDict['AsciiFrames']):
                    break
        except pygame.error as e:
            if e.args[0] == 'video system not initialized':
                print("Error: Video system not initialized")
                sys.exit(0)
            elif e.args[0] == 'display Surface quit':
                print("Error: Display windows was quit")
                sys.exit(0)
        finally:
            pygame.display.quit()
            pygame.mixer.music.unload()
            os.remove("../temp/" + asciiVideoDict['filename'] + '_audio_decoded.mp3')
            return

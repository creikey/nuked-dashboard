#!/usr/bin/env python

"""
Shows networktable data
"""

import pygame
import pynk
import pynk.nkpygame
from networktables import NetworkTables
import copy

WIDTH = 1024
HEIGHT = 768
FONT_NAME = "Arial"
FONT_SIZE = 36
WIN_CAPTION = "Doomsdash"
SERVER_URL = "10.29.84.2"

conn_status = "CONNECTED"
tb = NetworkTables.initialize(server=SERVER_URL)
d_width = WIDTH
d_height = HEIGHT


def make_screen():
    return pygame.display.set_mode((d_width, d_height), pygame.RESIZABLE)


if __name__ == '__main__':

    # Initialise pygame.
    pygame.init()
    screen = make_screen()
    pygame.display.set_caption(WIN_CAPTION)

    running = True
    # Initialise nuklear
    font = pynk.nkpygame.NkPygameFont(
        pygame.font.SysFont(FONT_NAME, FONT_SIZE))
    with pynk.nkpygame.NkPygame(font) as nkpy:
        text_color = pynk.lib.nk_rgb(nkpy.ctx.style.text.color.r, nkpy.ctx.style.text.color.g, nkpy.ctx.style.text.color.b)
        while running:
            # Handle input.
            events = []
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    running = False
                elif e.type == pygame.VIDEORESIZE:
                    d_width = e.w
                    d_height = e.h
                    screen = make_screen()
                else:
                    events.append(e)
            nkpy.handle_events(events)

            # Show the demo GUI.
            if pynk.lib.nk_begin(nkpy.ctx, WIN_CAPTION.encode('utf-8'), pynk.lib.nk_rect(0, 0, d_width, d_height), 0):
                pynk.lib.nk_layout_row_dynamic(nkpy.ctx, 0, 2)
                pynk.lib.nk_label(nkpy.ctx, "Connection Status:".encode('utf-8'), pynk.lib.NK_TEXT_LEFT)
                nkpy.ctx.style.text.color = pynk.lib.nk_rgb(0, 255, 0)
                pynk.lib.nk_label(nkpy.ctx, conn_status.encode('utf-8'), pynk.lib.NK_TEXT_RIGHT)
                nkpy.ctx.style.text.color = text_color
            pynk.lib.nk_end(nkpy.ctx)

            # Draw
            screen.fill((0, 0, 0))
            nkpy.render_to_surface(screen)
            pygame.display.update()

            # Clear the context for the next pass.
            pynk.lib.nk_clear(nkpy.ctx)

    # Shutdown.
    pygame.quit()

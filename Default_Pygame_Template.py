import pygame
import pygame.freetype
import csv
import sys

# --- Constants ---
SURFACE_COLOR_BLACK = BLACK = (0,0,0)

# --- Main Function --- Runs Once
def main(): 
    
    # --Initiatilize The Pygame --
    pygame.init()
    clock = pygame.time.Clock()

    # - Create The Screen & Local Variables -
    screenflags = pygame.FULLSCREEN
    screen = pygame.display.set_mode((0,0))#,screenflags) # Add screenflags back in to go fullscreen.
    
    pygame.display.set_caption("Start in Pygame")
    screenH = screen.get_height() # Grab whatever screen size resulted from (0,0) above.
    screenW = screen.get_width() # Grab whatever screen size resulted from (0,0) above.

    # -- Main Loop --
    running = True
    while running:
        
        # - Events -
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # - Draws (without updates) -
        screen.fill(SURFACE_COLOR_BLACK)
        pygame.display.flip() # Updates the contents of the entire display.
        
        # - Tick the Clock -
        clock.tick(60) # Prevents program from running faster than 60 frames per second. Uses SDL_Delay function which is not that accurate but saves CPU.
        
    # - End while loop when running=False -
    pygame.quit()

# ---- Call The Function ----
main()



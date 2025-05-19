import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot



def main():

    # Initialize PyGame
    pygame.init()

    # Initialize the display. Feed it our SCREEN_WIDTH/HEIGHT
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Setup our game clock and our variable to track delta time "dt"
    clock = pygame.time.Clock()
    dt = 0

    # Initialize Groups
    updatable   = pygame.sprite.Group()     # all objects that can be updated
    drawable    = pygame.sprite.Group()     # all objects that can be drawn
    asteroids   = pygame.sprite.Group()     # all asteroid objects
    shots       = pygame.sprite.Group()     # all shot objects

    # Assign all Objects to Groups
    Player.containers           = (updatable, drawable)
    Asteroid.containers         = (updatable, drawable, asteroids)
    AsteroidField.containers    = updatable
    Shot.containers             = (updatable, drawable, shots)

    # Intialize our Asteroid Field object
    asteroid_field = AsteroidField()

    # Intialize our Player object
    player = Player(PLAYER_START_X, PLAYER_START_Y)



    # Lets start things up.  This is the main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Lets update the player at the start
        # KEEP THIS AS THE FIRST THING
        #player.update(dt)  < ---  This is now inside of the Group: updatable
        # Update all objects
        updatable.update(dt)

        # Check asteroids, for collision with objects
        for i in asteroids:
            # First with the Player.  If impacted, player loses, exit program
            if i.collision(player):
                sys.exit()

            # Then with Player Shots.  If impacted, destroy both asteroid and shot
            for s in shots:
                if i.collision(s):
                    s.kill()
                    i.split()

        # Fill out the screen with a black background
        screen.fill("black")

        # Add anything you want to draw here (after the background, so it's "on top of")
            # ...but anything before Player, so Player will be drawn "on top of"

        # Lets draw the player to the screen
        #player.draw(screen)    < -- This is now inside of the Group: drawable
        for i in drawable:
            i.draw(screen)

        # Add UI draw here, so it's above everything else

        # This will refresh the screen
        pygame.display.flip()

        # This will limit the framerate to 60 FPS, and feed to "dt" how much time passed between frame draws
        # THIS NEEDS TO BE LAST
        dt = clock.tick(MAX_FPS) / 1000


if __name__ == "__main__":
    main()

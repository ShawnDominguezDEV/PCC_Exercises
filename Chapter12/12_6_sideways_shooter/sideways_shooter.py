# Exercsie 12-6; Sideways Shooter

# Main file for Sideways Shooter game

# Items Left: Allow bullet shooting. Align jet to center of screen upon game start, currently starts at top left.

import sys

import pygame
from ss_settings import Settings
from jet import Jet
from missile import Missile

class SidewaysShooter:
    """Main class for the Sideways Shooter game"""

    def __init__(self):
        """Initialze the game."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Sideways Shooter")

        self.jet = Jet(self)
        self.missiles = pygame.sprite.Group()

    def run_game(self):
        """Main Loop to Run the Game."""
        while True:
            self._check_events()
            self.jet.update()
            self._update_missiles()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to key presses."""
        if event.key == pygame.K_UP:
            self.jet.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.jet.moving_down = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_missile()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.jet.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.jet.moving_down = False

    def _fire_missile(self):
        """Create a new missile and add it to the missiles group."""
        if len(self.missiles) < self.settings.missiles_allowed:
            new_missile = Missile(self)
            self.missiles.add(new_missile)

    def _update_missiles(self):
        """Update position of missiles and get rid of old missiles."""
        # Update missile positions.
        self.missiles.update()

        # Get rid of missiles that have disappeared.
        for missile in self.missiles.copy():
            if missile.rect.left >= self.screen.get_rect().right:
                self.missiles.remove(missile)

    def _update_screen(self):
        """"Update the images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.jet.blitme()
        for missile in self.missiles.sprites():
            missile.draw_missile()

        # Make the most recently drawn screen visible
        pygame.display.flip()
            


if __name__ == '__main__':
    # Make a new game instance, and run the game.
    ss = SidewaysShooter()
    ss.run_game()
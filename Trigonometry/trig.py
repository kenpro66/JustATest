import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
PLAYER_SIZE = 30
OBSTACLE_WIDTH = 50
OBSTACLE_GAP = 50
OBSTACLE_SPEED = 3
PLAYER_SPEED = 2
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Triangle Escape")

# Player triangle class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)
        self.speed = PLAYER_SPEED

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Keep player within screen bounds
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

# Obstacle class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, y):
        super().__init__()
        self.shape = random.choice(['rectangle', 'circle', 'triangle'])
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if self.shape == 'rectangle':
            self.width = random.randint(20, 100)
            self.height = random.randint(20, 100)
            self.image = pygame.Surface((self.width, self.height))
            self.image.fill(self.color)
            self.rect = self.image.get_rect()
            self.rect.x = SCREEN_WIDTH
            self.rect.y = y
        elif self.shape == 'circle':
            self.radius = random.randint(10, 50)
            self.image = pygame.Surface((self.radius * 2, self.radius * 2))
            self.image.fill((0, 0, 0, 0))  # Make transparent
            self.rect = self.image.get_rect()
            pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
            self.rect.x = SCREEN_WIDTH
            self.rect.y = y
        elif self.shape == 'triangle':
            self.size = random.randint(20, 80)
            self.image = pygame.Surface((self.size, self.size))
            self.image.fill((0, 0, 0, 0))  # Make transparent
            self.rect = self.image.get_rect()
            pygame.draw.polygon(self.image, self.color, [(self.size // 2, 0), (0, self.size), (self.size, self.size)])
            self.rect.x = SCREEN_WIDTH
            self.rect.y = y

    def update(self):
        self.rect.x -= OBSTACLE_SPEED  # Move obstacles from right to left
        # If obstacle is completely off the screen, remove it
        if self.rect.right < 0:
            self.kill()

# Function to generate obstacles
def create_obstacle():
    top_height = random.randint(50, SCREEN_HEIGHT - OBSTACLE_GAP - 50)
    bottom_height = SCREEN_HEIGHT - top_height - OBSTACLE_GAP
    top_obstacle = Obstacle(0)
    bottom_obstacle = Obstacle(top_height + OBSTACLE_GAP)
    return top_obstacle, bottom_obstacle

# Function to draw text on the screen
def draw_text(surface, text, size, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

# Main game function
def main():
    # Initialize game variables
    player = Player()
    obstacles = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    lives = 3
    score = 0
    obstacle_frequency = 150
    game_over = False

    # Game loop
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r and game_over:
                    main()  # Restart game

        # Add obstacles
        if not game_over and score % obstacle_frequency == 0:
            top_obstacle, bottom_obstacle = create_obstacle()
            obstacles.add(top_obstacle, bottom_obstacle)
            all_sprites.add(top_obstacle, bottom_obstacle)

        # Update sprites
        all_sprites.update()

        # Check for collisions
        if pygame.sprite.spritecollide(player, obstacles, False):
            lives -= 1
            if lives == 0:
                game_over = True
            else:
                for obstacle in obstacles:
                    obstacle.kill()

        # Clear screen
        screen.fill(BLACK)

        # Draw sprites
        all_sprites.draw(screen)

        # Draw score and lives
        draw_text(screen, f"Score: {score}", 30, SCREEN_WIDTH // 2, 10)
        draw_text(screen, f"Lives: {lives}", 30, SCREEN_WIDTH // 2, 40)

        # Update display
        pygame.display.flip()

        # Increment score
        if not game_over:
            score += 1

        # Game over condition
        if game_over:
            draw_text(screen, "Game Over", 50, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            draw_text(screen, "Press R to Restart", 30, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            pygame.display.flip()

# Run the game
if __name__ == "__main__":
    main()

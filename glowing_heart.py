import pygame
import math
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Glowing Animated Heart')

# Heart parameters
def draw_heart(surface, x, y, size, color, glow=0):
    points = []
    for t in range(0, 360, 2):
        rad = math.radians(t)
        xh = 16 * math.sin(rad) ** 3
        yh = 13 * math.cos(rad) - 5 * math.cos(2 * rad) - 2 * math.cos(3 * rad) - math.cos(4 * rad)
        points.append((x + size * xh, y - size * yh))
    if glow > 0:
        for g in range(glow, 0, -2):
            alpha = max(10, int(255 * (g / glow) * 0.2))
            glow_surf = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            pygame.draw.polygon(glow_surf, (*color, alpha), points)
            surface.blit(glow_surf, (0, 0))
    pygame.draw.polygon(surface, color, points)

# Heart movement
x, y = WIDTH // 2, HEIGHT // 2
size = 15
color = (255, 0, 100)
glow = 40
speed = 3
angle = random.uniform(0, 2 * math.pi)
dx = speed * math.cos(angle)
dy = speed * math.sin(angle)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move heart
    x += dx
    y += dy
    if x < 80 or x > WIDTH - 80:
        dx = -dx + random.uniform(-0.5, 0.5)
    if y < 80 or y > HEIGHT - 80:
        dy = -dy + random.uniform(-0.5, 0.5)

    # Draw
    screen.fill((10, 10, 30))
    draw_heart(screen, int(x), int(y), size, color, glow=glow)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
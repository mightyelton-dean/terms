import pygame
import random

# Initialize pygame
pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Lightbulb with Pull Rope')

# Colors
color_list = [
    (255, 255, 120), # yellow
    (255, 120, 120), # red
    (120, 255, 120), # green
    (120, 200, 255), # blue
    (255, 120, 255), # magenta
    (255, 200, 120), # orange
    (200, 120, 255), # purple
    (255, 255, 255), # white
]
color_index = 0
bulb_color = color_list[color_index]
gray = (180, 180, 180)
dark = (40, 40, 40)
white = (255, 255, 255)

# Bulb state
bulb_on = False
rope_dragging = False
rope_top = (WIDTH // 2, 120)
rope_bottom = [WIDTH // 2, 300]
rope_rest = 300
rope_pulled = 400

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if abs(mx - rope_bottom[0]) < 30 and abs(my - rope_bottom[1]) < 30:
                rope_dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if rope_dragging:
                if rope_bottom[1] > (rope_rest + rope_pulled) // 2:
                    bulb_on = not bulb_on
                    if bulb_on:
                        color_index = (color_index + 1) % len(color_list)
                        bulb_color = color_list[color_index]
                rope_bottom[1] = rope_rest
                rope_dragging = False
        elif event.type == pygame.MOUSEMOTION and rope_dragging:
            mx, my = pygame.mouse.get_pos()
            rope_bottom[1] = min(max(my, rope_rest), rope_pulled)

    # Draw background
    screen.fill(dark)

    # Draw rope
    pygame.draw.line(screen, gray, rope_top, rope_bottom, 6)
    pygame.draw.circle(screen, gray, rope_bottom, 18)

    # Draw bulb
    bulb_center = (WIDTH // 2, 180)
    bulb_radius = 60
    if bulb_on:
        pygame.draw.circle(screen, bulb_color, bulb_center, bulb_radius)
        for i in range(8):
            angle = i * 3.14159 / 4
            x1 = bulb_center[0] + int(bulb_radius * 0.8 * pygame.math.Vector2(1, 0).rotate_rad(angle).x)
            y1 = bulb_center[1] + int(bulb_radius * 0.8 * pygame.math.Vector2(1, 0).rotate_rad(angle).y)
            x2 = bulb_center[0] + int(bulb_radius * 1.5 * pygame.math.Vector2(1, 0).rotate_rad(angle).x)
            y2 = bulb_center[1] + int(bulb_radius * 1.5 * pygame.math.Vector2(1, 0).rotate_rad(angle).y)
            pygame.draw.line(screen, bulb_color, (x1, y1), (x2, y2), 8)
    else:
        pygame.draw.circle(screen, gray, bulb_center, bulb_radius)
    pygame.draw.ellipse(screen, white, (bulb_center[0] - 30, bulb_center[1] - 60, 60, 40))
    pygame.draw.rect(screen, gray, (bulb_center[0] - 20, bulb_center[1] + 40, 40, 30))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

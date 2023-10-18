import pygame
import math
import time

# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Screen settings
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Analog Clock")

# Clock settings
clock_radius = 250
center_x = screen_width // 2
center_y = screen_height // 2

# Fonts
font = pygame.font.Font(None, 36)

# Function to draw numerical markers for hours
def draw_numerical_markers():
    for i in range(1, 13):
        angle = math.radians(90 - i * 30)
        marker_x = center_x + (clock_radius - 40) * math.cos(angle) - 10
        marker_y = center_y - (clock_radius - 40) * math.sin(angle) - 10
        text = font.render(str(i), True, WHITE)
        screen.blit(text, (marker_x, marker_y))

# Function to update the clock
def update_clock():
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min
    hours = current_time.tm_hour % 12

    # Clear the screen
    screen.fill(BLACK)

    # Draw clock face
    pygame.draw.circle(screen, WHITE, (center_x, center_y), clock_radius, 5)

    # Draw numerical markers for hours
    draw_numerical_markers()

    # Draw hour hand
    hour_angle = math.radians(90 - (hours * 30 + minutes / 2))
    hour_x = center_x + (clock_radius - 70) * math.cos(hour_angle)
    hour_y = center_y - (clock_radius - 70) * math.sin(hour_angle)
    pygame.draw.line(screen, styles[current_style]["hour_color"], (center_x, center_y), (hour_x, hour_y), 12)

    # Draw minute hand
    minute_angle = math.radians(90 - (minutes * 6 + seconds / 10))
    minute_x = center_x + (clock_radius - 30) * math.cos(minute_angle)
    minute_y = center_y - (clock_radius - 30) * math.sin(minute_angle)
    pygame.draw.line(screen, styles[current_style]["minute_color"], (center_x, center_y), (minute_x, minute_y), 8)

    # Draw second hand
    second_angle = math.radians(90 - seconds * 6)
    second_x = center_x + (clock_radius - 10) * math.cos(second_angle)
    second_y = center_y - (clock_radius - 10) * math.sin(second_angle)
    pygame.draw.line(screen, styles[current_style]["second_color"], (center_x, center_y), (second_x, second_y), 2)

    # Draw clock center point
    pygame.draw.circle(screen, WHITE, (center_x, center_y), 5)

    # Update the clock
    pygame.display.flip()

# Create a Pygame clock object to control the frame rate
clock = pygame.time.Clock()

# Clock styles
styles = [
    {"hour_color": BLUE, "minute_color": GREEN, "second_color": RED},
    {"hour_color": RED, "minute_color": GREEN, "second_color": BLUE},
    {"hour_color": WHITE, "minute_color": WHITE, "second_color": WHITE}
]
current_style = 0

# Main game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Cycle through clock styles when the spacebar is pressed
                current_style = (current_style + 1) % len(styles)

    update_clock()
    clock.tick(30)  # Update the clock at 30 frames per second

# Quit Pygame
pygame.quit()

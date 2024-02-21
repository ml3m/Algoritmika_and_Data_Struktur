import pygame
import random

# Initializing PyGame
pygame.init()

# Set up the window
win_width = 1280
win_height = 720
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Selection Sort Visualizer GeekforGeeks")
win.fill((0, 0, 0))

# Generating random array
arr_len = 50
arr = [random.randint(1, win_height) for i in range(arr_len)]

# Initializing sorted and unsorted parts of array
sorted_idx = -1
unsorted_idx = 0

# Selection sort loop
while sorted_idx < arr_len - 1:
	min_idx = unsorted_idx
	for i in range(unsorted_idx, arr_len):
		if arr[i] < arr[min_idx]:
			min_idx = i
	arr[unsorted_idx], arr[min_idx] = arr[min_idx], arr[unsorted_idx]
	sorted_idx = unsorted_idx
	unsorted_idx += 1

	# Drawing bars
	delay = 100 # Change the value to adjust the delay in milliseconds
	win.fill((0, 0, 0))
	for i in range(arr_len):
		color = (255, 255, 255) if i <= sorted_idx else (0, 255, 0)
		pygame.draw.rect(win, color, (i * (win_width / arr_len),
						win_height - arr[i], win_width / arr_len, arr[i]))
	pygame.display.update()
	pygame.time.wait(delay)

# Event handling loop
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

# Quit PyGame
pygame.quit()


import os
import time
import random

# T-Rex
t_rex = ["  /\_/\  ",
         " ( o.o ) ",
         " > ^ < "]

# Cactus
cactus = ["   /\_/\  ",
          "  / o o \ ",
          " (   \"   )",
          "  \~(*)~/ "]

# Bird
bird = ["  /\_/\  ",
        " ( o.o ) ",
        "  > ^ < "]

# Cloud
cloud = [" _ _ _ ",
         "   ~ ~  ",
         "  _ _ _ "]

# Game variables
game_over = False
t_rex_x = 0
cactus_x = random.randint(30, 50)
bird_x = random.randint(30, 50)
cloud_x = random.randint(30, 50)
score = 0

# Clear the terminal
os.system("clear")

while not game_over:
    # Print the T-Rex and obstacles
    for i in range(3):
        print(" " * t_rex_x + t_rex[i])
    for i in range(4):
        print(" " * cactus_x + cactus[i])
    for i in range(3):
        print(" " * bird_x + bird[i])
    for i in range(3):
        print(" " * cloud_x + cloud[i])
    print("Score:", score)

    # Get user input
    action = input("Jump or Quit (j/q): ")
    if action.lower() == "q":
        game_over = True
    elif action.lower() == "j":
        t_rex_x = max(t_rex_x - 3, 0)

    # Update the obstacles position
    cactus_x -= 1
    bird_x -= 2
    cloud_x -= 1
    if cactus_x < 0:
        cactus_x = random.randint(30, 50)
    if bird_x < 0:
        bird_x = random.randint(30, 50)
    if cloud_x < 0:
        cloud_x = random.randint(30, 50)

    # Check for collision
    if t_rex_x == cactus_x or t_rex_x == bird_x or t_rex_x == cloud_x:
        game_over = True
    else:
        score += 1

    # Clear the terminal
    os.system("clear")
    time.sleep(0.1)

print("Game Over")

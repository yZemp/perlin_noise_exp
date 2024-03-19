import tkinter
import perlin_noise
import time
import random

#####################################################################################################
# CONSTANTS

WIDTH = 800
HEIGHT = 800
RADIUS = 2
MOV_SCALE = 3

#####################################################################################################
# FUNCTIONS

noise = perlin_noise.PerlinNoise(octaves = 10, seed = int(random.random() * 100))


#####################################################################################################
# ROOT

root = tkinter.Tk()
root.geometry(f"{WIDTH}x{HEIGHT}+500+100")
root.grid_columnconfigure(0, weight = 1)
root.grid_rowconfigure(0, weight = 1)


#####################################################################################################
# CANVAS

canvas = tkinter.Canvas(root, bg = "#c0c0c0")
canvas.grid(row = 0, sticky = "news")


#####################################################################################################
# ANIMATION

def animation():
    root.update()
    x = 0
    y = canvas.winfo_height() / 2
    xoff = 0
    
    running = True
    
    while running:

        canvas.create_oval(x - RADIUS, y - RADIUS, x + RADIUS, y + RADIUS, fill = "#060606")
        
        x += .1
        y += noise(xoff + 10_000) * MOV_SCALE

        root.update()
        time.sleep(1 / 10_000)
        xoff += .001


#####################################################################################################
# RUNTIME

animation()
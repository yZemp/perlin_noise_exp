import tkinter
import perlin_noise
import time

#####################################################################################################
# FUNCTIONS

noise = perlin_noise.PerlinNoise(octaves = 4, seed = 1)


#####################################################################################################
# ROOT

root = tkinter.Tk()
root.geometry("800x800+500+100")
root.grid_columnconfigure(0, weight = 1)
root.grid_rowconfigure(0, weight = 3)
root.grid_rowconfigure(1, weight = 1)

#####################################################################################################
# CANVAS

canvas = tkinter.Canvas(root, bg = "#f0f0f0")
canvas.grid(row = 0, sticky = "news")

wrapper = tkinter.Frame(root)
wrapper.grid(row = 1, column = 0, sticky = "news")
wrapper.grid_columnconfigure(0, weight = 1)
wrapper.grid_columnconfigure(1, weight = 1)
wrapper.grid_columnconfigure(2, weight = 1)
wrapper.grid_rowconfigure(0, weight = 1)

red = tkinter.Canvas(wrapper, bg = "red")
red.grid(row = 0, column = 0, sticky = "nsew")
green = tkinter.Canvas(wrapper, bg = "green")
green.grid(row = 0, column = 1, sticky = "nsew")
blue = tkinter.Canvas(wrapper, bg = "blue")
blue.grid(row = 0, column = 2, sticky = "nsew")



#####################################################################################################
# ANIMATION

def animation():
    running = True
    x = 0
    while running:
        canvas.delete("all")

        r = hex(int(noise(x + 00_000) * 255) + 128)[2:].ljust(2, '0')
        g = hex(int(noise(x + 10_000) * 255) + 128)[2:].ljust(2, '0')
        b = hex(int(noise(x + 20_000) * 255) + 128)[2:].ljust(2, '0')

        print(f"{r}\t{g}\t{b}")
        

        red.configure(bg = f"#{r}0000")
        green.configure(bg = f"#00{g}00")
        blue.configure(bg = f"#0000{b}")

        canvas.configure(bg = f"#{r}{g}{b}")

        root.update()
        time.sleep(1 / 200)
        x += .001

#####################################################################################################
# RUNTIME

animation()
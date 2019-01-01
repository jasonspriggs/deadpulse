import time
import machine
import neopixel

num_pixels = 16
bits_per_pixel = 4 # this is usually 3 and needs to be explicitly set

pixels = neopixel.NeoPixel(machine.Pin(12), num_pixels, bits_per_pixel)

print("main.py is running")

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3, 0)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3, 0)

def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.write()
    time.sleep(0.5)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = (255, int((rc_index & 255) / 4), 0, 0)
        pixels.write()
        time.sleep(wait)

# pause is converted to milliseconds
def breathe(pause, steps, R, G, B): 
    for s in range(10, steps + 1):
        tmpR = int((R * s) / steps)
        tmpG = int((G * s) / steps)
        tmpB = int((B * s) / steps)

        #print('R: ', {tmpR}, ', G: ', {tmpG}, ', B: ', {tmpB})
    
        for i in range(0, num_pixels):
            pixels[i] = (tmpR, tmpG, tmpB, 0)
        
        pixels.write()
        time.sleep(pause / 1000)

    s = steps
    while (s > 10):
        s -= 1
        tmpR = int((R * s) / steps)
        tmpG = int((G * s) / steps)
        tmpB = int((B * s) / steps)

        #print('R: ', {tmpR}, ', G: ', {tmpG}, ', B: ', {tmpB})
    
        for i in range(0, num_pixels):
            pixels[i] = (tmpR, tmpG, tmpB, 0)
        
        pixels.write()
        time.sleep(pause / 1000)

def breathe_cycle(pause, steps):
    j = 0
    for s in range(10, steps + 1):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            tmpR = 255
            tmpG = int((rc_index & 255) / 4)
            pixels[i] = (int((tmpR * s) / steps), int((tmpG * s) / steps), 0, 0)
        j += 2
        pixels.write()
        time.sleep(pause / 1000)

    s = steps
    while (s > 10):
        s -= 1
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            tmpR = 255
            tmpG = int((rc_index & 255) / 4)
            pixels[i] = (int((tmpR * s) / steps), int((tmpG * s) / steps), 0, 0)
        j += 2
        pixels.write()
        time.sleep(pause / 1000)
        

        # for s in range(10, steps + 1):
        #     tmpR = int((R * s) / steps)
        #     tmpG = int((G * s) / steps)
        #     tmpB = int((B * s) / steps)

        #     #print('R: ', {tmpR}, ', G: ', {tmpG}, ', B: ', {tmpB})
        
        #     for i in range(0, num_pixels):
        #         pixels[i] = (tmpR, tmpG, tmpB, 0)
            
        #     pixels.write()
        #     time.sleep(pause / 1000)

        # s = steps
        # while (s > 10):
        #     s -= 1
        #     tmpR = int((R * s) / steps)
        #     tmpG = int((G * s) / steps)
        #     tmpB = int((B * s) / steps)

        #     #print('R: ', {tmpR}, ', G: ', {tmpG}, ', B: ', {tmpB})
        
        #     for i in range(0, num_pixels):
        #         pixels[i] = (tmpR, tmpG, tmpB, 0)
            
        #     pixels.write()
        #     time.sleep(pause / 1000)


RED = (255, 0, 0, 0)
YELLOW = (255, 150, 0, 0)
GREEN = (0, 255, 0, 0)
CYAN = (0, 255, 255, 0)
BLUE = (0, 0, 255, 0)
PURPLE = (180, 0, 255, 0)

while True:
    # pixels.fill(RED)
    # pixels.write()
    # # Increase or decrease to change the speed of the solid color change.
    # time.sleep(1)
    # pixels.fill(GREEN)
    # pixels.write()
    # time.sleep(1)
    # pixels.fill(BLUE)
    # pixels.write()
    # time.sleep(1)

    # color_chase(RED, 0.1)  # Increase the number to slow down the color chase
    # color_chase(YELLOW, 0.1)
    # color_chase(GREEN, 0.1)
    # color_chase(CYAN, 0.1)
    # color_chase(BLUE, 0.1)
    # color_chase(PURPLE, 0.1)

    # rainbow_cycle(0)  # Increase the number to slow down the rainbow
    # breathe(10, 100, 255, 0, 0)
    breathe(10, 100, 255, 0, 0)


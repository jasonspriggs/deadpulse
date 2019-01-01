import time
import machine
import neopixel

num_pixels = 16
bits_per_pixel = 4 # this is usually 3 and needs to be explicitly set

pixels = neopixel.NeoPixel(machine.Pin(12), num_pixels, bits_per_pixel)

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

def main():
    while True:
        breathe_cycle(10, 100)

if __name__ == '__main__':
    print("main entered")
    main()


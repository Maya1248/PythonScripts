from PIL import Image
import numpy as np

def help():
    print("Time for the program to finish depends on the image size.")
    print("")
    print("pixify(image.[jpg, png...], color, mode)")
    print("")
    print("Available colors: white, black, red, green, blue")
    print("")
    print("Available modes: general, nature, portrait")
    print("")
    print("Mode description:")
    print("general - general purpose mode")
    print("nature - decreased number of colored pixels")
    print("portrait - increased number of colored pixels")

def toColor(color):
    d = {
        "white": (255,255,255),
        "black": (0,0,0),
        "red": (255,0,0),
        "green": (0,255,0),
        "blue": (0,0,255),
        "purple": (128,0,128)
        }

    return d.get(color)

def pixify(image, color, mode, whiteback=True):
    try:
        im = Image.open(image)
    except FileNotFoundError:
        print("File not found! Check if the file is in the same directory. Check if you mispelled the file name.")
    
    if mode == "general":
        m = 15
    elif mode == "nature":
        m = 50
    elif mode == "portrait":
        m = 5
    else:
        print("Invalid mode!")
        exit()

    im = im.convert('RGB')
    pixels = im.load()

    for x in range(0, im.size[0]):
        yside = False
        for y in range(0, im.size[1]):
            if y == 0:
                pass
            else:
                prevpix = pixels[x, y-1]
                curpix = pixels[x, y]

                if prevpix > curpix:
                    big = prevpix
                    small = curpix
                else:
                    big = curpix
                    small = prevpix
                
                if tuple(np.subtract(big, small)) >= (m,m,m):
                    if yside == False:
                        pixels[x, y-1] = color
                        yside = True
                    else:
                        pixels[x, y] = color
                        yside = False

    for y in range(0, im.size[1]):
        xside = False
        for x in range(0, im.size[0]):
            if x == 0:
                pass
            else:
                prevpix = pixels[x-1, y]
                curpix = pixels[x, y]

                if prevpix > curpix:
                    big = prevpix
                    small = curpix
                else:
                    big = curpix
                    small = prevpix

                if tuple(np.subtract(big, small)) >= (m,m,m):
                    if xside == False:
                        pixels[x-1, y] = color
                        xside = True
                    else:
                        pixels[x, y] = color
                        xside = False

    if whiteback:
        white = toColor("white")
        for x in range(0, im.size[0]):
            for y in range(0, im.size[1]):
                if pixels[x, y] != color:
                    pixels[x, y] = white
    
    print("Finishing...")
    im.save("pix_" + mode + str(color) + "_" + image)

def main():
    help()

    name = str(input("Name of the image (with extension): "))
    color = str(input("Color: "))
    mode = str(input("Mode: "))
    
    pixify(name,toColor(color),mode)

if __name__ == "__main__":
    main()

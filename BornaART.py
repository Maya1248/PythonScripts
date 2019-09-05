from PIL import Image
import numpy as np

print("help()")

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
acolors = [white, black, red, green, blue]

def help():
    print("Time for the program to finish depends on the image size, example: HD(1920x1080 pixels) image takes about 30 seconds, 4K(3840x2160) image takes about 2 minutes.")
    print("")
    print("art(image.[jpg, png...], color, mode, whiteback) - main command (image name must be fully correct, so must be the extension (example: .jpg)")
    print("")
    print("Avaiable colors: white, black, red, green, blue")
    print("")
    print("Avaiable modes: general, nature")
    print("")
    print("whiteback - must be True or False (Shall the program paint background in white ?)")
    print("")
    print("Mode description")
    print("")
    print("general - general mode")
    print("nature - numbers are optimized specifically for surfaces with similar colors")
    
# DO NOT DELETE, source code also known as the representation of how this program started out.
def dlbc(image, color):
    im = Image.open(image)

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
                
                if tuple(np.subtract(big, small)) >= (15,15,15):
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

                if tuple(np.subtract(big, small)) >= (15,15,15):
                    if xside == False:
                        pixels[x-1, y] = color
                        xside = True
                    else:
                        pixels[x, y] = color
                        xside = False

    im.save("C:/Users/Marzic/Desktop/Python/Projects/DLBC_Images/DLBC_" + image)

def art(image, color, mode, whiteback):
    if color not in acolors:
        print("Invalid color!")
        exit()
    
    if mode == "general":
        m = 15
    elif mode == "nature":
        m = 50
    else:
        print("Invalid mode!")
        exit()

    im = Image.open(image)

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

    if whiteback == True:
        for x in range(0, im.size[0]):
            for y in range(0, im.size[1]):
                if pixels[x, y] != color:
                    pixels[x, y] = white
    elif whiteback == False:
        print("Finishing...")
    else:
        whiteback = False
        print("Invalid argument. Finishing...")

    im.save("C:/Users/Marzic/Desktop/Python/Projects/DLBC_Images/Bart_" + mode + "_" + str(whiteback) + "_" + image)

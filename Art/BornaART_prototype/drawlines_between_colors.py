from PIL import Image

im = Image.open("test.png")

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
            
            if curpix != prevpix:
                if yside == False:
                    pixels[x, y-1] = (255,0,0)
                    yside = True
                else:
                    pixels[x, y] = (255,0,0)
                    yside = False

for y in range(0, im.size[1]):
    xside = False
    for x in range(0, im.size[0]):
        if x == 0:
            pass
        else:
            prevpix = pixels[x-1, y]
            curpix = pixels[x, y]

            if curpix != prevpix:
                if xside == False:
                    pixels[x-1, y] = (255,0,0)
                    xside = True
                else:
                    pixels[x, y] = (255,0,0)
                    xside = False


im.save("C:/Users/Marzic/Desktop/Python/Projects/drawlines_between_colors/test2.png")

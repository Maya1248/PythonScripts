from PIL import Image

im = Image.open("test.png")
im = im.convert('RGB')

image = im.load()

br = 0

for i in range(0, im.size[0]):
    for j in range(0, im.size[1]):        
        if image[i, j] < (50, 50, 50):
            br += 1
            if br == 1:
                x1 = i
                y1 = j

            x2 = i
            y2 = j

for i in range(x1, x2+1):
    image[i, y1-1] = (0, 255, 0)
    image[i, y2+1] = (0, 255, 0)
for i in range(y1, y2+1):
    image[x1-1, i] = (0, 255, 0)

im.save("C:/Users/Marzic/Desktop/Python/Projects/recognise_colors/test2.png")

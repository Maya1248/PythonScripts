from PIL import Image
from AesEverywhere import aes256

def getImageData(image):
    im = Image.open(image)
    im = im.convert("RGB")
    pixels = im.load()
    width = im.size[0]
    height = im.size[1]

    return (pixels, width, height)
    
def encryptImage(image, password):
    image = getImageData(image)
    pixels = image[0]
    newData = []
    width = image[1]
    height = image[2]
    
    for x in range(width):
        newData.append([])
        for y in range(height):
            newData[x].append(aes256.encrypt(str(pixels[x,y]), password))
        
    return (newData, width, height)

def decryptImage(image, password):
    data = image[0]
    newData = []
    width = image[1]
    height = image[2]

    for x in range(width):
        newData.append([])
        for y in range(height):
            newData[x].append(aes256.decrypt(data[x][y], password))

    return (newData, width, height)

def conjureImageFromData(image, name):
    data = image[0]
    width = image[1]
    height = image[2]

    im = Image.new("RGB",(width,height))
    pixels = im.load()

    for x in range(width):
        for y in range(height):
            pixels[x,y] = eval(data[x][y])

    im.save(name + ".jpg")


def main():
    ch = 0

    while True:
        ch = str(input("1 - Encrypt image \n2 - Decrypt image \n3 - Exit \n>"))
        
        if ch == "1":
            name = str(input("Name (e.g. image.jpg, image2.png): "))
            pwd = str(input("Password (remember this!): "))
            
            e = encryptImage(name, pwd)
            
            with open(name[0:name.find(".")] + ".image", "w") as f:
                f.write(str(e))

            print("[+] " + name + " encrypted\n")
        elif ch == "2":
            name = str(input("Name (e.g. image.image, image2.image): "))
            pwd = str(input("Password: "))

            with open(name, "r") as f:
                e = eval(f.read())
            
            d = decryptImage(e, pwd)
            conjureImageFromData(d, name[0:name.find(".")])
        elif ch == "3":
            break
        else:
            print("[-] Uknown command\n")

if __name__ == "__main__":
    main()

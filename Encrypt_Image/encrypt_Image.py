from PIL import Image
from AesEverywhere import aes256
import os

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

def saveToFile(name, pwd):
    e = encryptImage(name, pwd)
            
    with open(name[0:name.find(".")] + ".image", "w") as f:
        f.write(str(e))
    
def getFromFile(name, pwd):
    with open(name, "r") as f:
        e = eval(f.read())
            
    d = decryptImage(e, pwd)
    conjureImageFromData(d, name[0:name.find(".")])
    
def fetchFiles(folder):
    os.chdir(folder)
    images = [im for im in os.listdir()]
    os.chdir("..")
    
    return images

def read():
    print("1 - Encrypt an image")
    print("2 - Decrypt an image")
    print("3 - Encrypt all images in a folder")
    print("4 - Decrypt all images in a folder")
    print("5 - Exit")

def main():
    ch = 0

    while True:
        ch = str(input(">"))
        
        if ch == "1":
            name = str(input("Name (e.g. image.jpg, image2.png): "))
            pwd = str(input("Password (remember this!): "))

            saveToFile(name, pwd)

            print("[+] " + name + " encrypted\n")
            
        elif ch == "2":
            name = str(input("Name (e.g. image.image, image2.image): "))
            pwd = str(input("Password: "))

            getFromFile(name, pwd)

            print("[+] " + name + " decrypted\n")
            
        elif ch == "3":
            name = str(input("Name of folder to encrypt: "))
            pwd = str(input("Password: "))

            all_images = fetchFiles(name)

            os.mkdir("encrypted_files")
            os.chdir(name)

            for image in all_images:
                os.chdir("../encrypted_files")
                saveToFile("../" + name + "/" + image, pwd)

                print("[+] " + image + " encrypted\n")
            

        elif ch == "4":
            name = str(input("Name of folder to decrypt: "))
            pwd = str(input("Passowrd: "))

            all_files = fetchFiles(name)

            os.mkdir("decrypted_files")
            os.chdir(name)

            for file in all_files:
                os.chdir("../decrypted_files")
                getFromFile("../" + name + "/" + file, pwd)
                
                print("[+] " + file + " decrypted\n")
                
            
        elif ch == "5":
            break
        
        else:
            print("[-] Uknown command\n")


if __name__ == "__main__":
    read()
    main()

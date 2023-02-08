import pywhatkit
pywhatkit.image_to_ascii_art('IMG_3160.JPG','MyArt')
read_file = open("MyArt.txt","r")
print(read_file.read())
import pywhatkit
pywhatkit.image_to_ascii_art('PROFILE.png','MyArt2')
read_file = open("MyArt2.txt","r")
print(read_file.read())
import eyed3
from PIL import Image
import os
os.chdir("output")
for file in os.listdir():
    if file.endswith(".mp3"):
        audio_file = eyed3.load(file)
        album_name = audio_file.tag.album
        artist_name = audio_file.tag.artist
        for image in audio_file.tag.images:
            image_file = open("image.jpg", "wb")
            filename = "image.jpg"
            print("Writing image file: image.jpg")
            image_file.write(image.image_data)
            image_file.close()
            print("resizing image")
            img = Image.open(filename)
            img = img.resize((600, 600), Image.ANTIALIAS)
            img.save(filename)
            print("adding image to mp3")
            audio_file.tag.images.set(image.picture_type, open(filename, "rb").read(), "image/jpeg")
            audio_file.tag.save()
            print("done")
            os.remove(filename)
    else:
        continue
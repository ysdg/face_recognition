#!/usr/bin/env python
#-*- coding:utf8 -*-
import face_recognition
from PIL import Image, ImageDraw

imagePath = "../face_recognition/examples/"
obama_image = face_recognition.load_image_file(imagePath+"obama.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

biden_image = face_recognition.load_image_file(imagePath+"biden.jpg")
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

known_face_encodings = [obama_face_encoding, biden_face_encoding]
known_face_names = ["Barack Obama", "Joe Biden"]

unknown_image = face_recognition.load_image_file(imagePath+"two_people.jpg")

face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

pil_image = Image.fromarray(unknown_image)
draw = ImageDraw.Draw(pil_image)

for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    name = "Unknown"
    if True in matches:
        name = known_face_names[matches.index(True)]
    draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom-text_height-10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
    draw.text((left+6, bottom-text_height-5), name, fill=(255, 255, 255, 255))

del draw
pil_image.show()
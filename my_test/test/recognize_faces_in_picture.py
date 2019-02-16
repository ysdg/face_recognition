#!/usr/bin/env python
#-*- coding:utf8 -*-
import face_recognition

imagePath = "../../examples/"

biden_image = face_recognition.load_image_file(imagePath+"biden.jpg")
obama_image = face_recognition.load_image_file(imagePath+"obama.jpg")
unknow_image = face_recognition.load_image_file(imagePath+"obama2.jpg")

try:
    biden_face_encoding = face_recognition.face_encodings(biden_image)[0]
    obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
    unknow_face_encoding = face_recognition.face_encodings(unknow_image)[0]
except IndexError:
    print("Image must have face to recognize, please check the image files")
    quit()

known_face = [biden_face_encoding, obama_face_encoding]
print(biden_face_encoding)
results = face_recognition.compare_faces(known_face, unknow_face_encoding)

print("Is the unknown face a picture of biden?{}".format(results[0]))
print("Is the unknown face a picture of obama?{}".format(results[1]))
print("Is the unknown face a new person never seen before?{}".format(not True in results))

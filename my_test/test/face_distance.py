#!/usr/bin/env python
#-*- coding:utf8 -*-
import face_recognition
from PIL import Image, ImageDraw

imagePath = "../../examples/"

obama_image = face_recognition.load_image_file(imagePath+"obama.jpg")
biden_image = face_recognition.load_image_file(imagePath+"biden.jpg")

obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]
known_encodings = [obama_face_encoding, biden_face_encoding]

image_to_test = face_recognition.load_image_file(imagePath+"obama2.jpg")
image_to_test_encoding = face_recognition.face_encodings(image_to_test)[0]

face_distances = face_recognition.face_distance(known_encodings, image_to_test_encoding)
print(face_distances)
for i, face_distance in enumerate(face_distances):
    print("The test image has a distance of {:.2} from known image #{}".format(face_distance, i))
    print("- With a normal curoff of 0.6, would the test image match the known_image?{}".format(face_distance<0.6))
    print("- With a normal curoff of o.5, would the test image match the known_image?{}".format(face_distance<0.5))
    print()
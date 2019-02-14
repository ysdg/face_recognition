#!/usr/bin/env python
#-*- coding:utf8 -*-
import face_recognition
from PIL import Image, ImageDraw

imagePath = "../face_recognition/examples/"
image = face_recognition.load_image_file(imagePath+"two_people.jpg")
face_landmarks_list = face_recognition.face_landmarks(image)

for face_landmark in face_landmarks_list:
    pil_image = Image.fromarray(image)
    d = ImageDraw.Draw(pil_image, 'RGBA')
    
    d.polygon(face_landmark['left_eyebrow'], fill=(68, 54, 39, 128))
    d.polygon(face_landmark['right_eyebrow'], fill=(68, 54, 39, 128))
    d.line(face_landmark['left_eyebrow'], fill=(68, 54, 39, 150), width=5)
    d.line(face_landmark['right_eyebrow'], fill=(68, 54, 39, 150), width=5)

    d.polygon(face_landmark['top_lip'], fill=(150, 0, 0, 128))
    d.polygon(face_landmark['bottom_lip'], fill=(150, 0, 0, 128))
    d.line(face_landmark['top_lip'], fill=(150, 0, 0, 64), width=8)
    d.line(face_landmark['bottom_lip'], fill=(150, 0, 0, 64), width=8)

    d.polygon(face_landmark['left_eye'], fill=(255, 255, 255, 30))
    d.polygon(face_landmark['right_eye'], fill=(255, 255, 255, 30))
    d.line(face_landmark['left_eye']+[face_landmark['left_eye'][0]], fill=(0, 0, 0, 110), width=6)
    d.line(face_landmark['right_eye']+[face_landmark['right_eye'][0]], fill=(0, 0, 0, 110), width=6)
    pil_image.show()
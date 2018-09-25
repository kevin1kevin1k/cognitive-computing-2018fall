from PIL import Image, ImageDraw, ImageFont
import cv2

# This photo is taken by myself
image = cv2.imread('./input.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('image', image)

sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
sobel = Image.fromarray((sobelx + sobely)/2).convert('L')

draw = ImageDraw.Draw(sobel)
# https://github.com/todylu/monaco.ttf
font = ImageFont.truetype('./monaco.ttf', size=12)
draw.text((20, sobel.size[1]-20), 'r07922087', font=font)

sobel.save('output.png')

from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage

# This photo is taken by myself
image = Image.open('./input.png').convert('L')
image.show()

sobel = Image.fromarray(ndimage.sobel(image))

draw = ImageDraw.Draw(sobel)
# https://github.com/todylu/monaco.ttf
font = ImageFont.truetype('./monaco.ttf', size=12)
draw.text((20, sobel.size[1]-20), 'r07922087', font=font)

sobel.save('output.png')

from PIL import ImageFilter , Image
image = Image.open('screen.png')
blurred_jelly = image.filter(ImageFilter.BLUR)
blurred_jelly.save('test1.png')

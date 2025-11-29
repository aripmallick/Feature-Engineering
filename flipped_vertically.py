from PIL import Image

image=Image.open("D:/Feature Engineering/bird.jpg")
flipped_vertically=image.transpose(Image.FLIP_TOP_BOTTOM)
flipped_vertically.save("flipped_vertically_output.png")
image.show()
flipped_vertically.show()
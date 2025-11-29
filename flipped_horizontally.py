from PIL import Image

image=Image.open("D:/Feature Engineering/bird.jpg")
flipped_horizontally=image.transpose(Image.FLIP_LEFT_RIGHT)
flipped_horizontally.save("flipped_horizontally_output.png")
image.show()
flipped_horizontally.show()
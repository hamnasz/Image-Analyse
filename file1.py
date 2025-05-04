from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt

# Load the images
subject_path = "/mnt/data/524816d4-d5fc-42cd-af08-96a07ff93468.png"
background_path = "/mnt/data/e601a905-2a99-4948-836d-c5753f60fb76.png"

subject_img = Image.open(subject_path).convert("RGBA")
background_img = Image.open(background_path).convert("RGBA")

# Rotate the background image to portrait orientation (90 degrees)
rotated_background = background_img.rotate(90, expand=True)

# Show the rotated background for verification before proceeding with cutout and composite
rotated_background.show()

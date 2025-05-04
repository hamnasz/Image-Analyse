from PIL import ImageFilter

# Correct vignette creation using GaussianBlur for a soft, cinematic effect
vignette = Image.new("L", subject_img.size, 0)
center_x, center_y = subject_img.size[0] / 2, subject_img.size[1] / 2
max_dist = (center_x**2 + center_y**2) ** 0.5

for x in range(subject_img.size[0]):
    for y in range(subject_img.size[1]):
        dx = x - center_x
        dy = y - center_y
        dist = (dx**2 + dy**2) ** 0.5
        intensity = 255 - int(255 * (dist / max_dist))
        vignette.putpixel((x, y), max(0, min(255, intensity)))

# Blur the vignette to soften the gradient
vignette = vignette.filter(ImageFilter.GaussianBlur(100))

# Apply the vignette as a shadow overlay
cinematic_final = Image.composite(composited_dim, Image.new("RGBA", subject_img.size, "black"), vignette)

# Crop to 1:1 square ratio, centered
width, height = cinematic_final.size
side = min(width, height)
left = (width - side) // 2
top = (height - side) // 2
square_crop = cinematic_final.crop((left, top, left + side, top + side))

# Show final image
square_crop.show()

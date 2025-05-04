from PIL import ImageOps

# Resize background to match subject size for better compositing
resized_background = rotated_background.resize(subject_img.size)

# Extract the subject using alpha mask (assuming transparent background in subject image)
subject_mask = subject_img.getchannel("A")

# Composite subject onto background
composited_image = Image.composite(subject_img, resized_background, subject_mask)

# Dim the background slightly for cinematic effect
enhancer = ImageEnhance.Brightness(resized_background)
dimmed_background = enhancer.enhance(0.7)  # Reduce brightness to 70%
composited_dim = Image.composite(subject_img, dimmed_background, subject_mask)

# Apply soft shadow effect by adding subtle vignette (simulate cinematic lighting)
vignette = Image.new("L", subject_img.size, 0)
for x in range(subject_img.size[0]):
    for y in range(subject_img.size[1]):
        # Create radial vignette mask
        dx = x - subject_img.size[0] / 2
        dy = y - subject_img.size[1] / 2
        dist = (dx**2 + dy**2) ** 0.5
        vignette.putpixel((x, y), int(min(255, dist)))

vignette = ImageOps.invert(vignette)
vignette = vignette.filter(ImageEnhance.Sharpness(vignette).enhance(0.5))

# Apply the vignette as a shadow overlay
vignette_mask = vignette.convert("L")
cinematic_final = Image.composite(composited_dim, Image.new("RGBA", subject_img.size, "black"), vignette_mask)

# Crop to 1:1 square ratio, centered
width, height = cinematic_final.size
side = min(width, height)
left = (width - side) // 2
top = (height - side) // 2
square_crop = cinematic_final.crop((left, top, left + side, top + side))

# Show final result
square_crop.show()

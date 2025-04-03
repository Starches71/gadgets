
import requests
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

# Image URL
image_url = "https://image-us.samsung.com/us/smartphones/galaxy-s25/Gallery/PA1/PA1-01-Navy-1600x1200.jpg"

# Download image
response = requests.get(image_url)
image = Image.open(BytesIO(response.content)).convert("RGB")

# Image size
width, height = image.size

# Create gradient overlay (black fading to transparent)
gradient = Image.new("L", (width, 200), color=0)
for y in range(200):
    gradient.putpixel((0, y), int((y / 200) * 255))

# Expand gradient across the image width
gradient = gradient.resize((width, 200))

# Convert to RGBA and paste on image
gradient_layer = Image.new("RGBA", (width, height))
gradient_layer.paste((0, 0, 0, 200), (0, height - 200))  # Dark bottom

# Merge gradient with image
image = image.convert("RGBA")
image = Image.alpha_composite(image, gradient_layer)

# Load font
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Adjust if needed
font = ImageFont.truetype(font_path, 50)

# Draw text
draw = ImageDraw.Draw(image)
text = "Samsung Galaxy S25"
text_w, text_h = draw.textbbox((0, 0), text, font=font)[2:]

# Position text at the bottom center
x = (width - text_w) // 2
y = height - 150

# Add text with white color
draw.text((x, y), text, font=font, fill="white")

# Convert RGBA to RGB (JPEG doesn't support RGBA)
image = image.convert("RGB")

# Save final image
image.save("processed.jpg")

print("Image processing completed: saved as 'processed.jpg'")

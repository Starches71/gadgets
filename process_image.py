from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

# Load image from URL
url = "https://image-us.samsung.com/us/smartphones/galaxy-s25/Gallery/PA1/PA1-01-Navy-1600x1200.jpg"
response = requests.get(url)
image = Image.open(BytesIO(response.content))

# Convert to RGBA to handle transparency
image = image.convert("RGBA")

# Create gradient overlay
width, height = image.size
gradient_height = int(height * 0.4)
overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
gradient = Image.new("RGBA", (width, gradient_height), (0, 0, 0, 200))

# Apply gradient at the bottom
overlay.paste(gradient, (0, height - gradient_height, width, height))
image = Image.alpha_composite(image, overlay)

# Load font
font = ImageFont.truetype("DejaVuSans-Bold.ttf", 40)

# Add text
draw = ImageDraw.Draw(image)
text = "Samsung Galaxy S25 - Stunning Navy Blue!"
bbox = draw.textbbox((0, 0), text, font=font)
text_w, text_h = bbox[2] - bbox[0], bbox[3] - bbox[1]
text_x = (width - text_w) // 2
text_y = height - text_h - 20

draw.text((text_x, text_y), text, font=font, fill="white")

# Save result
image.save("processed.jpg")

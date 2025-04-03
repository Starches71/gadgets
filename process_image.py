
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Load the image
image = cv2.imread("original.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB

# Get image dimensions
h, w, _ = image.shape

# Create gradient overlay (Black to Transparent)
gradient = np.zeros((h, w, 3), dtype=np.uint8)
for i in range(int(h * 0.4), h):  # Apply gradient to the bottom 40%
    alpha = (i - h * 0.4) / (h * 0.6)
    gradient[i, :, :] = (0, 0, 0)  # Black
    gradient[i, :, :] = gradient[i, :, :] * alpha

# Blend gradient with image
overlayed = cv2.addWeighted(image, 1, gradient, 0.6, 0)

# Convert to PIL for text rendering
image_pil = Image.fromarray(overlayed)
draw = ImageDraw.Draw(image_pil)

# Load a bold font
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Adjust as needed
font = ImageFont.truetype(font_path, 60)  # Adjust font size

# Define text
text = "Samsung Galaxy S25 Ultra\nAI-Powered Performance"

# Get text size and position
text_w, text_h = draw.textsize(text, font=font)
text_x = (w - text_w) // 2
text_y = h - int(h * 0.3)  # Position text on gradient

# Add text
draw.text((text_x, text_y), text, font=font, fill="white")

# Save processed image
image_pil.save("processed.jpg")

# scripts/prep_photo.py
import cv2
import numpy as np
from PIL import Image
from rembg import remove

def prep(input_path="profile.jpg", output_path="source-prepped.png"):
    print("Processing source photo...")
    inp = Image.open(input_path)
    
    # 1. Remove background
    no_bg = remove(inp)
    
    # 2. Composite onto pure white background
    bg = Image.new("RGBA", no_bg.size, (255, 255, 255, 255))
    bg.paste(no_bg, (0, 0), no_bg)
    gray = cv2.cvtColor(np.array(bg.convert("RGB")), cv2.COLOR_RGB2GRAY)
    
    # 3. CLAHE contrast enhancement
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(gray)
    
    cv2.imwrite(output_path, enhanced)
    print(f"Prepped photo saved to {output_path}")

if __name__ == "__main__":
    prep()
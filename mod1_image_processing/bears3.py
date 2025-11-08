from PIL import Image

filename = 'bears_copy.jpg'
filepath = f"mod1_image_processing/{filename}"

file_out = 'bears3.jpg'
file_out_path = f"mod1_image_processing/{file_out}"

balloon_filename = 'balloon.jpg'
balloon_filepath = f"mod1_image_processing/{balloon_filename}"
balloon_image = Image.open(balloon_filepath)

# Load the original image, and get its size and color mode.
orig_image = Image.open(filepath)
balloon_image = Image.open(balloon_filepath)
width, height = orig_image.size
mode = orig_image.mode

balloon_width, balloon_height = balloon_image.size
new_width = width // 3
new_height = height // 2
balloon_image = balloon_image.resize((new_width, new_height), Image.LANCZOS)
balloon_height, balloon_width = balloon_image.size
balloon_image = balloon_image.convert("RGBA")

# Show information about the original image.
print(f"Original image: {filename}")
print(f"Size: {width} x {height} pixels")
print(f"Mode: {mode}")

print(f"Original image: {balloon_filename}")
print(f"Size: {balloon_height} x {balloon_width} pixels")

#get rid of baloon white background
datas = balloon_image.getdata()
newData = []
for item in datas:
    # Detect white (or near-white) pixels
    if item[0] > 240 and item[1] > 240 and item[2] > 240:
        # Set alpha to 0 (transparent)
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

balloon_image.putdata(newData)

# Load all pixels from the image.
orig_pixel_map = orig_image.load()


# Examine all pixels in the image.
"""print("\nPixel data:")
for x in range(10):
    for y in range(10):
        pixel = orig_pixel_map[x, y]
        print(pixel)
"""
# Create a new image matching the original image's color mode, and size.
new_image = Image.new("RGBA", (width, height))
new_pixel_map = new_image.load()


# Modify each pixel in the new image.
for x in range(width):
    for y in range(height):
        # Copy the original pixel to the new pixel map.
        new_pixel_map[x, y] = orig_pixel_map[x, y]

new_image.paste(balloon_image, (20, 350), balloon_image)
new_image = new_image.convert("RGB")
new_image.save(file_out_path)
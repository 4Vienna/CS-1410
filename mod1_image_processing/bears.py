from PIL import Image

filename = 'starr_bears.jpg'
filepath = f"./{filename}"

file_out = 'bears_copy.jpg'
file_out_path = f"./{file_out}"

# Load the original image, and get its size and color mode.
orig_image = Image.open(filepath)
width, height = orig_image.size
mode = orig_image.mode

# Show information about the original image.
print(f"Original image: {filename}")
print(f"Size: {width} x {height} pixels")
print(f"Mode: {mode}")

# Load all pixels from the image.
orig_pixel_map = orig_image.load()


# Examine all pixels in the image.
print("\nPixel data:")
for x in range(10):
    for y in range(10):
        pixel = orig_pixel_map[x, y]
        print(pixel)

# Create a new image matching the original image's color mode, and size.
#   Load all the pixels from this new image as well.
new_image = Image.new(mode, (width, height))
new_pixel_map = new_image.load()

# Modify each pixel in the new image.
for x in range(width):
    for y in range(height):
        # Copy the original pixel to the new pixel map.
        new_pixel_map[x, y] = orig_pixel_map[x, y]

new_image.save(file_out_path)
import os
from PIL import Image

def get_image_resolution(image_path, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    # Open image and get size
    img = Image.open(image_path)
    width, height = img.size
    
    # Create output filename
    image_name = os.path.basename(image_path)
    output_file = os.path.join(output_folder, f"{image_name}_resolution.txt")
    
    # Write resolution to file
    with open(output_file, 'w') as f:
        f.write(f"Image: {image_name}\n")
        f.write(f"Resolution: {width}x{height}")
        
    return width, height

# Example usage
input_image = "computer_vision/resources/001e163a-249c-4c5b-afa1-4b7a39434872_original_image_IMG-20231226-WA0088.jpg"  # Replace with your image path
output_folder = "resolutions"  # Output folder name
resolution = get_image_resolution(input_image, output_folder)
print(f"Resolution extracted: {resolution[0]}x{resolution[1]}")

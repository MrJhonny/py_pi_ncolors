from PIL import Image
from mpmath import mp

# Function to get colors (grayscale or color)
def get_color_for_number(number, grayscale=False):
    if grayscale:
        colors = {
            0: (76, 76, 76),      # Gray for Red
            1: (150, 150, 150),   # Gray for Green
            2: (29, 29, 29),      # Gray for Blue
            3: (225, 225, 225),   # Gray for Yellow
            4: (105, 105, 105),   # Gray for Magenta
            5: (178, 178, 178),   # Gray for Cyan
            6: (38, 38, 38),      # Gray for Dark Brown
            7: (38, 38, 38),      # Gray for Dark Green
            8: (15, 15, 15),      # Gray for Dark Blue
            9: (128, 128, 128)    # Gray
        }
    else:
        colors = {
            0: (255, 0, 0),       # Red
            1: (0, 255, 0),       # Green
            2: (0, 0, 255),       # Blue
            3: (255, 255, 0),     # Yellow
            4: (255, 0, 255),     # Magenta
            5: (0, 255, 255),     # Cyan
            6: (128, 0, 0),       # Dark Brown
            7: (0, 128, 0),       # Dark Green
            8: (0, 0, 128),       # Dark Blue
            9: (128, 128, 128)    # Gray
        }
    return colors.get(number, (0, 0, 0))  

# Get the first digits of pi
def get_pi_digits(count):
    pi_str = str(mp.pi).replace('.', '')  
    return [int(digit) for digit in pi_str[:count]]

# Create the image
def generate_image(width, height, grayscale):
    total_pixels = width * height
    digits = get_pi_digits(total_pixels)

    image = Image.new("RGB", (width, height))
    pixels = image.load()

    for y in range(height):
        for x in range(width):
            index = y * width + x
            if index < len(digits):
                color = get_color_for_number(digits[index], grayscale)
                pixels[x, y] = color

    return image

# Main script
if __name__ == "__main__":
    # Ask user for width and height
    try:
        width = int(input("Enter the width of the image (in pixels): "))
        height = int(input("Enter the height of the image (in pixels): "))
    except ValueError:
        print("Please enter valid numbers for width and height.")
        exit(1)

    # Ask if the user wants colors (default is colors)
    grayscale_input = input("Do you want the image in colors? (yes/no): ").strip().lower()
    grayscale = not (grayscale_input in ["yes", "y", "true"])

    # Configure precision to calculate enough digits of pi
    mp.dps = width * height + 1  # Precision in decimal places

    # Generate the image
    image = generate_image(width, height, grayscale)
    mode = "gray" if grayscale else "colors"
    file_name = f'pi_{width}x{height}_{mode}.png'
    image.save(file_name)

    print(f"Image generated and saved as '{file_name}'.")
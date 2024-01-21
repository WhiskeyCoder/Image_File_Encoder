from PIL import Image

binary_to_color = {
    '0000': (255, 0, 0),
    '0001': (0, 128, 255),
    '0010': (50, 205, 50),
    '0011': (255, 255, 0),
    '0100': (128, 0, 128),
    '0101': (0, 255, 128),
    '0110': (255, 128, 0),
    '0111': (0, 0, 255),
    '1000': (255, 192, 203),
    '1001': (0, 139, 139),
    '1010': (70, 130, 180),
    '1011': (107, 142, 35),
    '1100': (139, 0, 0),
    '1101': (30, 144, 255),
    '1110': (255, 69, 0),
    '1111': (169, 169, 169),
}


def read_binary_file(filename):
    with open(filename, 'rb') as file:
        binary_data = file.read()
    return ''.join(format(byte, '08b') for byte in binary_data)


def create_image_from_binary(binary_data):
    width = 4  # Each pixel represents 4 bits
    height = len(binary_data) // width  # Calculate height based on binary length
    image = Image.new('RGB', (width, height))
    pixels = []
    for i in range(0, len(binary_data), width):
        binary_chunk = binary_data[i:i + width]
        color = binary_to_color.get(binary_chunk, (255, 255, 255))
        pixels.append(color)

    image.putdata(pixels)
    return image


if __name__ == "__main__":
    input_file = "Your_Input_File"  # Replace with your input file
    output_image_file = "output_image.png"
    binary_data = read_binary_file(input_file)
    image = create_image_from_binary(binary_data)
    image.save(output_image_file)
    print(f"Image '{output_image_file}' created.")

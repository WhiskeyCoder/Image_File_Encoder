from PIL import Image

color_to_binary = {
    (255, 0, 0): '0000',
    (0, 128, 255): '0001',
    (50, 205, 50): '0010',
    (255, 255, 0): '0011',
    (128, 0, 128): '0100',
    (0, 255, 128): '0101',
    (255, 128, 0): '0110',
    (0, 0, 255): '0111',
    (255, 192, 203): '1000',
    (0, 139, 139): '1001',
    (70, 130, 180): '1010',
    (107, 142, 35): '1011',
    (139, 0, 0): '1100',
    (30, 144, 255): '1101',
    (255, 69, 0): '1110',
    (169, 169, 169): '1111',
}


def extract_binary_from_image(image):
    pixels = list(image.getdata())
    binary_data = ''
    for pixel in pixels:
        binary_chunk = color_to_binary.get(pixel, '0000')  # Default to '0000' if not found
        binary_data += binary_chunk
      
    binary_data = binary_data.rstrip('0')
    return binary_data


def write_binary_to_file(binary_data, output_filename):
    padding_length = 8 - (len(binary_data) % 8)
    binary_data += '0' * padding_length
    bytes_data = bytes(int(binary_data[i:i + 8], 2) for i in range(0, len(binary_data), 8))
    with open(output_filename, 'wb') as file:
        file.write(bytes_data)


if __name__ == "__main__":
    input_image_file = "output_image.png"  # Replace with the image file created earlier
    output_file = "decrypted_output"
    image = Image.open(input_image_file)
    binary_data = extract_binary_from_image(image)
    write_binary_to_file(binary_data, output_file)
    print(f"Decrypted file '{output_file}' created.")

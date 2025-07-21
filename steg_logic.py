from PIL import Image
import numpy as np

def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(char, 2)) for char in chars if int(char, 2) != 0)

def hide_text(image_path, text, output_path):
    img = Image.open(image_path).convert("RGB")
    pixels = np.array(img)
    binary_text = text_to_binary(text) + '1111111111111110'  
    idx = 0

    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            for k in range(3):
                if idx < len(binary_text):
                    pixels[i, j, k] = (pixels[i, j, k] & 0xFE) | int(binary_text[idx])
                    idx += 1
                else:
                    break

    new_img = Image.fromarray(pixels)
    new_img.save(output_path)

def extract_text(image_path):
    img = Image.open(image_path).convert("RGB")
    pixels = np.array(img)

    binary_text = ""
    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            for k in range(3):
                binary_text += str(pixels[i, j, k] & 1)

    end_marker = "1111111111111110"
    binary_text = binary_text[:binary_text.find(end_marker)]
    return binary_to_text(binary_text)

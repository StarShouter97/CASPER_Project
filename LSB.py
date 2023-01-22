import numpy as np
import Obfuscation_Layer
from PIL import Image


def lsb_encode(src, message, destination):

    img = Image.open(src, 'r')
    width, height = img.size
    array = np.array(list(img.getdata()))
    n = 0

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4

    total_pixels = array.size//n

    message += "$t3g0"
    b_message = ''.join([format(ord(i), "08b") for i in message])
    req_pixels = len(b_message)

    if req_pixels > total_pixels:
        print("\n ERROR: Need larger file size\n")
    else:
        index = 0
        for p in range(total_pixels):
            for q in range(0, 3):
                if index < req_pixels:
                    array[p][q] = int(bin(array[p][q])[2:9] + b_message[index], 2)
                    index += 1
                else:
                    break

        array = array.reshape(height, width, n)
        encoded_image = Image.fromarray(array.astype('uint8'), img.mode)
        encoded_image.save(destination)
        print("\n Image encoded successfully\n")


def lsb_decode(src, decrypted_key):

    img = Image.open(src, 'r')
    array = np.array(list(img.getdata()))
    n = 0

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4

    total_pixels = array.size//n

    hidden_bits = ""
    for p in range(total_pixels):
        for q in range(0, 3):
            hidden_bits += (bin(array[p][q])[2:][-1])

    hidden_bits = [hidden_bits[i:i+8] for i in range(0, len(hidden_bits), 8)]

    message = ""
    flag = False
    for i in range(len(hidden_bits)):
        if message[-5:] == "$t3g0":
            flag = True
            break
        else:
            message += chr(int(hidden_bits[i], 2))

    if flag:
        message = message.replace("$t3g0", "")
        Obfuscation_Layer.reverse_obfuscate(message, decrypted_key)
    else:
        print("\n No message in the image\n")

import cv2
import numpy as np


# Convert different types to binary
def msg_to_bin(msg):
    if isinstance(msg, str):
        return ''.join(format(ord(i), "08b") for i in msg)
    elif isinstance(msg, (bytes, np.ndarray)):
        return [format(i, "08b") for i in msg]
    elif isinstance(msg, (int, np.uint8)):
        return format(msg, "08b")
    else:
        raise TypeError("Unsupported input type")


# Hide the secret message into the image
def hide_data(img, secret_msg):
    # Calculate the maximum bytes for encoding
    max_bytes = img.shape[0] * img.shape[1] * 3 // 8
    print("Maximum Bytes for encoding:", max_bytes)

    # Check if data fits within the image
    if len(secret_msg) > max_bytes:
        raise ValueError("Insufficient bytes, need bigger image or less data!")

    secret_msg += '#####'  # Delimiter to identify end of hidden message
    bin_secret_msg = msg_to_bin(secret_msg)
    data_len = len(bin_secret_msg)
    data_index = 0

    # Encode data into the image
    for row in img:
        for pixel in row:
            r, g, b = msg_to_bin(pixel)

            if data_index < data_len:
                pixel[0] = int(r[:-1] + bin_secret_msg[data_index], 2)  # Modify LSB of Red
                data_index += 1
            if data_index < data_len:
                pixel[1] = int(g[:-1] + bin_secret_msg[data_index], 2)  # Modify LSB of Green
                data_index += 1
            if data_index < data_len:
                pixel[2] = int(b[:-1] + bin_secret_msg[data_index], 2)  # Modify LSB of Blue
                data_index += 1

            if data_index >= data_len:
                break
    return img


# Extract the hidden message from the image
def show_data(img):
    bin_data = ""

    for row in img:
        for pixel in row:
            r, g, b = msg_to_bin(pixel)
            bin_data += r[-1]  # Extract LSB of Red
            bin_data += g[-1]  # Extract LSB of Green
            bin_data += b[-1]  # Extract LSB of Blue

    # Split into bytes and convert to characters
    all_bytes = [bin_data[i: i + 8] for i in range(0, len(bin_data), 8)]
    decoded_data = ""

    for byte in all_bytes:
        decoded_data += chr(int(byte, 2))
        if decoded_data[-5:] == "#####":  # Stop at the delimiter
            break

    return decoded_data[:-5]  # Remove delimiter


# Function to encode data into an image
def encode_text():
    img_name = input("Enter image name (with extension): ")
    img = cv2.imread(img_name)

    if img is None:
        print("Error: Unable to read image. Please check the file name and path.")
        return

    print(f"Image Shape: {img.shape}")
    print("Displaying Image...")

    resized_img = cv2.resize(img, (500, 500))  # Resize for better visualization
    cv2.imshow("Original Image", resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    data = input("Enter the message to hide: ")
    if len(data) == 0:
        raise ValueError("Message is empty. Please enter some text.")

    output_img_name = input("Enter output image name (with extension): ")
    encoded_img = hide_data(img, data)
    cv2.imwrite(output_img_name, encoded_img)
    print(f"Data successfully encoded into {output_img_name}")


# Function to decode the hidden data from the image
def decode_text():
    img_name = input("Enter the name of the encoded image (with extension): ")
    img = cv2.imread(img_name)

    if img is None:
        print("Error: Unable to read image. Please check the file name and path.")
        return

    print("Displaying Encoded Image...")
    resized_img = cv2.resize(img, (500, 500))
    cv2.imshow("Encoded Image", resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    hidden_text = show_data(img)
    print("\nDecoded Message:", hidden_text)


# Main function for steganography
def steganography():
    while True:
        try:
            choice = int(input("\nImage Steganography\n1. Encode Data\n2. Decode Data\n3. Exit\nChoose an option: "))
            if choice == 1:
                encode_text()
            elif choice == 2:
                decode_text()
            elif choice == 3:
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Error: Please enter a valid number.")


# Run the program
steganography()

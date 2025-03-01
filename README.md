Image Steganography using Python

📌 Overview

This project demonstrates Image Steganography, a technique to hide secret messages within an image using Least Significant Bit (LSB) encoding. The encoded message remains invisible to the human eye while being securely embedded in the image.

🚀 Features

Hide Secret Messages within an image

Retrieve Hidden Messages from a steganographic image

Supports PNG, JPG, and BMP image formats

Uses Least Significant Bit (LSB) Encoding

Simple command-line interface for encoding and decoding

🔧 Technologies Used

Python

OpenCV (cv2) for image processing

NumPy for pixel manipulation

📥 Installation

Clone the repository:

git clone https://github.com/your-username/image-steganography.git
cd image-steganography

Install required dependencies:

pip install opencv-python numpy

🛠️ Usage

1️⃣ Encoding a Message into an Image

Run the script and follow the prompts:

python steganography.py

Enter 1 to encode a message

Provide the image name (e.g., image.png)

Enter the secret message to hide

Save the new encoded image (e.g., encoded_image.png)

2️⃣ Decoding a Message from an Image

Run the script and follow the prompts:

python steganography.py

Enter 2 to decode a message

Provide the steganographic image name (e.g., encoded_image.png)

The hidden message will be displayed

import sys
import re
import requests
import base64
import binascii
from stegano import lsb

# Function to extract hidden data using steganography
def extract_steganography(image_path):
    try:
        return lsb.reveal(image_path)
    except Exception as e:
        print(f"Error extracting from {image_path}: {str(e)}")
        return None

# Function to check if a given string is a valid OpenAI API key
def is_openai_key(key_fragment):
    return bool(re.match(r'^sk-[A-Za-z0-9]{48}$', key_fragment))

# Function to attempt decoding (base64, hex) to find a valid key
def attempt_decoding(possible_key):
    try:
        decoded_base64 = base64.b64decode(possible_key).decode('utf-8')
        if is_openai_key(decoded_base64):
            return decoded_base64
    except Exception:
        pass
    
    try:
        decoded_hex = binascii.unhexlify(possible_key).decode('utf-8')
        if is_openai_key(decoded_hex):
            return decoded_hex
    except Exception:
        pass
    
    return None

# Function to assemble fragments from multiple images
def assemble_key(fragments):
    return ''.join(fragments)

# Function to send a request to OpenAI API to list models
def request_openai_models(api_key):
    url = "https://api.openai.com/v1/models"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Function to analyze images and search for the API key
def analyze_images(image_paths):
    fragments = []
    for image_path in image_paths:
        hidden_data = extract_steganography(image_path)
        if hidden_data:
            if is_openai_key(hidden_data):
                print(f"Valid OpenAI API key detected in {image_path}: {hidden_data}")
                return hidden_data
            else:
                decoded_key = attempt_decoding(hidden_data)
                if decoded_key:
                    print(f"Decoded and found valid API key in {image_path}: {decoded_key}")
                    return decoded_key
                fragments.append(hidden_data)
        else:
            print(f"No hidden data found in {image_path}")
    
    if not fragments:
        print("No valid key found in any image.")
        return None

    possible_key = assemble_key(fragments)
    if is_openai_key(possible_key):
        print(f"Valid OpenAI API key assembled: {possible_key}")
        return possible_key
    else:
        print("Assembled fragments do not form a valid key. Consider analyzing more images or reviewing the order.")
        return None

# Simple CLI menu for user interaction
def main_menu():
    print("Welcome to the OpenAI API Key Finder!")
    print("1. Add images and analyze")
    print("2. Exit")

    choice = input("Choose an option: ")
    
    if choice == '1':
        image_paths = []
        print("Enter image paths one by one. Type 'done' when finished:")
        while True:
            path = input("Enter image path: ")
            if path.lower() == 'done':
                break
            image_paths.append(path)
        
        if not image_paths:
            print("No images entered.")
            return

        # Analyze the images
        api_key = analyze_images(image_paths)

        if api_key:
            print("\nTesting API Key with OpenAI...")
            response = request_openai_models(api_key)
            if response:
                print("\nSuccessfully retrieved models:")
                for model in response.get("data", []):
                    print(model.get("id", "Unknown ID"))
            else:
                print("Failed to retrieve models. The API key might be incorrect or blocked.")
        else:
            print("No valid API key found.")
    
    elif choice == '2':
        print("Exiting. Goodbye!")
        sys.exit(0)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    while True:
        main_menu()

# Strawberry Cypher
# OpenAI API Key Finder from Steganographic Images

# Mentions
https://x.com/elder_plinius/status/1823345600106037421

# Unmentionable
https://x.com/iruletheworldmo/status/1823345007710835125
https://x.com/iruletheworldmo

This Python script is designed to solve a puzzle by extracting potential OpenAI API keys hidden across up to 30 images. The script utilizes steganography, decoding techniques, and key assembly to find and validate API keys by querying OpenAI's model list.

## Features

- **Steganography Extraction:** Uses LSB (Least Significant Bit) steganography to reveal hidden data within images.
- **OpenAI Key Validation:** Checks if the extracted data follows the OpenAI API key format (`sk-` followed by 48 alphanumeric characters).
- **Obfuscation Handling:** Attempts decoding using base64 and hex if the extracted data does not directly match the key format. Assembles fragments from multiple images if necessary.
- **API Key Testing:** Sends a request to OpenAI's API to validate the key by listing available models.
- **User-Friendly Interface:** Simple command-line interface with a menu system that guides the user through adding images, analyzing them, and testing the extracted key.

## Installation

1. **Clone the repository:**  
git clone https://github.com/AxiMinds/strawberry-cypher.git  
cd strawberry-cypher

2. **Install the required Python packages:**  
pip install -r requirements.txt

## Usage

1. **Run the script:**  
python script.py

2. **Follow the prompts:**  
- **Add images:** Enter the paths to the images you want to analyze, one by one.  
- **Analyze:** The script will attempt to extract hidden data, check for valid OpenAI API keys, and assemble fragments if necessary.  
- **Test API Key:** If a valid key is found, the script will query the OpenAI API to list available models.

## Requirements

- Python 3.x
- Required Python packages (listed in `requirements.txt`):  
  - `requests`  
  - `stegano`

## Example

Here’s a simple example of how the script works:

1. Run the script.  
2. Enter the paths to up to 30 images.  
3. The script will analyze the images, extract hidden data, attempt decoding, and check if the data forms a valid OpenAI API key.  
4. If a valid key is detected, the script will use it to query the OpenAI API and display the list of available models.

## Contributing

Feel free to submit issues, fork the repository, and send pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License.

## Contact

For any questions or suggestions, feel free to reach out via GitHub Issues.

---

### Note:

This tool is intended for educational purposes and should be used responsibly. Ensure that you have the right to access and analyze any images you use with this script.

---

Happy coding!

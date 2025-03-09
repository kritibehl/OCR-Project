import cv2
import pytesseract

# Set Tesseract OCR path (if installed via Homebrew on macOS)
pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

def extract_text(image_path):
    # Load image
    image = cv2.imread(image_path)
    
    if image is None:
        print(f"Error: Could not read image '{image_path}'. Check file path.")
        return None
    
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Perform OCR
    extracted_text = pytesseract.image_to_string(gray, config="--psm 6")
    
    return extracted_text.strip()

# Image path
image_path = "sample.jpg"

# Run OCR and print detected text
text = extract_text(image_path)
if text:
    print("\nDetected Text:\n")
    print(text)
else:
    print("\nNo text detected.")

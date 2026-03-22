import pytesseract
import cv2
import numpy as np
from pdf2image import convert_from_path


def preprocess_image(image):

    img = np.array(image)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    thresh = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31,
        2
    )

    return thresh


def extract_pdf_text(pdf_path):

    pages = convert_from_path(pdf_path, dpi=300)

    full_text = []

    for i, page in enumerate(pages):

        print(f"OCR page {i+1}")

        processed = preprocess_image(page)

        text = pytesseract.image_to_string(
            processed,
            config="--psm 6"
        )

        full_text.append(text)

    return "\n".join(full_text)
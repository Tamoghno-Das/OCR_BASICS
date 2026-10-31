import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OCR_API_KEY")

OCR_URL = "https://api.ocr.space/parse/image"


def extract_text(image):

    if not API_KEY:
        raise ValueError("OCR API key is missing")

    response = requests.post(
        OCR_URL,
        files={
            "file": (
                image.name,
                image.getvalue(),
                image.type
            )
        },
        data={
            "apikey": API_KEY,
            "language": "eng",
            "isOverlayRequired": "false"
        },
        timeout=60
    )

    response.raise_for_status()

    result = response.json()

    if result.get("IsErroredOnProcessing"):
        raise ValueError(str(result.get("ErrorMessage")))

    extracted_text = ""

    for page in result.get("ParsedResults", []):
        extracted_text += page.get("ParsedText", "") + "\n"

    return extracted_text.strip()
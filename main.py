import cv2 # Pre-processing
from PIL import Image # Opening images
import pytesseract # OCR
from pdf2image import convert_from_path # PDF to images 
import json 
import pandas as pd   
from openai import OpenAI



image_list = convert_from_path("D:/Coding/business card project/prelim/pdftest.pdf")
for i in range(len(image_list)):
    image_list[i].save('page' + str(i+1) + '.jpg', 'JPEG')

# Need a way to iterate through the images
import os 
from os import listdir

folder_path = "D:/Coding/business card project/prelim"
extracted_text = ""

for images in os.listdir(folder_path):
    if (images.endswith(".jpg")):
        image = cv2.imread(images) 
        inverted_image = cv2.bitwise_not(image) # Inverts image
        gray_image = cv2.cvtColor(inverted_image, cv2.COLOR_BGR2GRAY)
        thresh, img_bw = cv2.threshold(gray_image, 100,80, cv2.THRESH_BINARY)
        path = "temp/blackwhite.jpg"
        cv2.imwrite(path, img_bw)
        page_text = pytesseract.image_to_string(Image.open(path))
        extracted_text += page_text +  "\n\n"


# This extracted text now has to be sent to Chat-GPT 
client = OpenAI(api_key = "") # Will need a key provided by the user

raw_text = extracted_text # this will be sent to the API
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    temperature=0.1, # More coherent, objective, factual
    messages=[
        {
            "role": "system", # Provides the rules and general instructions to the model. Acts like a manual
            "content": (
                "You are a data extraction and normalization assistant. "
                "Extract contact information from messy, unstructured text. "
                "Ignore irrelevant or corrupted lines. "
                "Return ONLY valid JSON. Do not include explanations. "
                "If a field cannot be determined, set it to null. "
                "Normalize phone numbers to E.164 format when possible."
            )
        },
        {
            "role": "user",
            "content": (
                "Extract contact information and return JSON with this structure:\n\n" # What the user would actually ask
                "{\n"
                '  "contacts": [\n'
                "    {\n"
                '      "name": string | null,\n'
                '      "title": string | null,\n'
                '      "company": string | null,\n'
                '      "department": string | null,\n'
                '      "address": string | null,\n'
                '      "city": string | null,\n'
                '      "email": string | null,\n'
                '      "mobile_phone": string | null,\n'
                '      "office_phone": string | null,\n'
                '      "other_phone": string | null\n'
                "    }\n"
                "  ]\n"
                "}\n\n"
                "Text:\n<<<\n"
                f"{raw_text}\n" # Gives the API the extracted text
                ">>>"
            )
        }
    ]
)

# Parse JSON safely
content = response.choices[0].message.content
data = json.loads(content)
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)
df = pd.DataFrame(data["contacts"])
df.to_excel("contacts.xlsx", index=False)
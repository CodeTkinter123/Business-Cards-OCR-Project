# Business-Cards-OCR-Project
Business Card Text Extractor: Documentation 

This project combines image preprocessing techniques (such as binarization and noise removal), Optical Character Recognition (OCR) and ChatGPT’s API to extract contact information from photos of business cards, as well as process the information into a tabular form with columns for each contact such as Name, Organisation, Title, and Contact Information. 

To eliminate the need to transfer multiple images from a phone to a laptop, the program allows PDF input. The user can click pictures of as many business cards as they want (multiple business cards can be included in an image), convert these pictures to a PDF and then send a single file to the computer. On the computer, the PDF is used as input and produces an Excel sheet of formatted contact information as output. 

Libraries used: 

•	OpenCV and Pillow – image manipulation and preprocessing 
•	PyTesseract – OCR (optical character recognition) to extract text from images 
•	Pdf2Image – processing PDF input into images which the OCR algorithm can be run on 
•	OS – iterate through a directory and operate on each image
•	OpenAI – access ChatGPT API to format raw extracted text into a tabular format
•	Json – process the output returned by the API 
•	Pandas – convert Json output to an Excel spreadsheet 

All the libraries except Json and OS are external, which means there are several dependencies that must be installed on the user’s system. PyTesseract and Pdf2Image also require external engines to be installed on the system. The instructions below are for setting up the program dependencies: 

1.	Install OpenCV, Pillow, OpenAI and Pandas with the following command in Terminal: 
pip install opencv-python pillow openai pandas

3.	Install PyTesseract Engine on the system (must be on admin account) 
Home · UB-Mannheim/tesseract Wiki · GitHub
Installation path should be C:\Program Files\Tesseract-OCR 
Add “C:\Program-Files\Tesseract-OCR” to the Path under user variables 
User can verify installation by running the following snippet in terminal: 
tesseract –version

4.	Install PyTesseract Model 
pip install pytesseract
User can verify installation by running the following Python snippet: 
import pytesseract
print(pytesseract.get_tesseract_version())

5.	Install Poppler (must be on admin account)
Releases · oschwartz10612/poppler-windows
Like the steps with Tesseract, add the poppler installation path to the Environment Variables. It should appear in the format “C:\Program Files\Release…” 
User can verify installation by running the following snippet in terminal: 
pdftoppm -h

6.	Install Pdf2Image 

pip install pdf2image

User Manual 
1.	Create a separate folder for program files 
2.	Save main.py in this folder
3.	Save the PDF file (of the business cards) in this folder 
4.	Create a file called “data.json” and save it to the folder 
After these steps, main.py can now be run and will generate a “contacts.xlsx” spreadsheet which contains the extracted, formatted contact information. 





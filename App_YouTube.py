# Convert any PDF file into Audio using Python

# Import necessary libraries
import pyttsx3   # Voice Engine
import PyPDF2    # PDF to Text

# Define voice engine
engine = pyttsx3.init()

# Define and open desired pdf file
file = open('simulation_paper_bostrom.pdf', 'rb')

# Define pdf reader
pdfReader = PyPDF2.PdfFileReader(file)

all_text = ''

# Enter pdf page range to extract text from
for num in range(1,10):
    page = pdfReader.getPage(num-1)
    text = page.extractText()
    text = text.replace('\n', ' ').replace('\r', '')
    all_text = all_text + text

# Have voice engine recite text
engine.say(all_text)
engine.runAndWait()

print("Code Completed")

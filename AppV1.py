# Import necessary libraries
import pyttsx3
import PyPDF2

# Female and Male Voice IDs
female_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
male_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"

# Define voice engine
engine = pyttsx3.init()

# Set to male or female voice id
engine.setProperty('voice', male_voice_id)

# Define Book with pdf title
book = open('bitcoin_white_paper.pdf', 'rb')

# Define pdf reader
pdfReader = PyPDF2.PdfFileReader(book)

# Determine and print number of pdf pages
num_pages = pdfReader.numPages
print("This pdf contains {} pages".format(num_pages))

# Enter any pdf page range you want, and then extract text from that page
for num in range(2,3):
    page = pdfReader.getPage(num-1)
    text = page.extractText()
    # Have voice engine recite text
    engine.say(text)
    engine.runAndWait()

print("Code Completed")

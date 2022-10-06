import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
import pyttsx3
import PyPDF2

root = Tk()
root.geometry('600x250')
root.title('PDF to Audiobook')
root.config(bg='lightblue')
root.resizable(0,0)

path_label = ttk.Label(root, text="PDF Path:").pack()
path_entry = Entry(root, width=80)
path_entry.pack()
path_entry.focus()

start_pg_label = ttk.Label(root, text="Starting Page:").place(x=60, y=65)
start_pg_entry = Entry(root, width=20)
start_pg_entry.place(x=60, y=90)

stop_pg_label = ttk.Label(root, text="Stopping Page:").place(x=230, y=65)
stop_pg_entry = Entry(root, width=20)
stop_pg_entry.place(x=230, y=90)

gender_label = ttk.Label(root, text="Voice Gender:").place(x=400, y=65)
gender_entry = Combobox(root, width=20)
gender_entry['values'] = ('Male', 'Female')
gender_entry.current(0)
gender_entry.place(x=400, y=90)


def pdf_to_audio():

    pdf_path = path_entry.get()
    start_pg = int(start_pg_entry.get())
    stop_pg = int(stop_pg_entry.get())
    gender = gender_entry.get()

    engine = pyttsx3.init()

    female_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    male_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"

    if(gender == 'Male'):
        engine.setProperty('voice', male_voice_id)
    elif(gender == 'Female'):
        engine.setProperty('voice', female_voice_id)

    pdf = open(pdf_path, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdf)

    for num in range(start_pg, stop_pg):
        page = pdfReader.getPage(num - 1)
        text = page.extractText()
        # Have voice engine recite text
        engine.say(text)
        engine.runAndWait()

Button(root, text='Convert PDF to Audio',width=30,bg='tomato',command=pdf_to_audio).place(x=180, y=140)

root.mainloop()

print('code completed')

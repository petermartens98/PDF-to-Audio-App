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
start_pg_entry = Entry(root, width=15)
start_pg_entry.place(x=60, y=90)

stop_pg_label = ttk.Label(root, text="Stopping Page:").place(x=60, y=120)
stop_pg_entry = Entry(root, width=15)
stop_pg_entry.place(x=60, y=145)

gender_label = ttk.Label(root, text="Voice Gender:").place(x=430, y=65)
gender_entry = Combobox(root, width=15)
gender_entry['values'] = ('Male', 'Female')
gender_entry.current(0)
gender_entry.place(x=430, y=90)

rate_label = ttk.Label(root, text="Voice Rate:").place(x=270, y=65)
rate_entry = Entry(root, width=15)
rate_entry.place(x=255, y=90)
rate_entry.insert(0,200)

save_label = ttk.Label(root, text="Save to MP3").place(x=430, y=120)
save_entry = Combobox(root, width=15)
save_entry['values'] = ('No', 'Yes')
save_entry.current(0)
save_entry.place(x=430, y=145)

def pdf_to_audio():

    pdf_path = path_entry.get()
    start_pg = int(start_pg_entry.get())
    stop_pg = int(stop_pg_entry.get())
    gender = gender_entry.get()
    voice_rate = int(rate_entry.get())
    save_opt = save_entry.get()
    all_text = ''
    
    engine = pyttsx3.init()

    engine.setProperty('rate', voice_rate)

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
        og_text = page.extractText()
        text = og_text.replace('\n', ' ').replace('\r', '')
        all_text = all_text + text
        print('-------------------------------------- Page '+str(num)+' --------------------------------------')
        print(og_text)
        
    engine.say(all_text)
    engine.runAndWait()

    if (save_opt=='Yes'):
        engine.save_to_file(all_text, pdf_path+'_Audio.mp3')


Button(root, text='Convert PDF to Audio',width=25,bg='tomato',command=pdf_to_audio).place(x=200, y=200)

root.mainloop()

print('code completed')

# Virtual Desktop Assistant with GUI and Voice Control

import tkinter as tk
from tkinter import messagebox, filedialog
import webbrowser
import os
import time
import threading
import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import subprocess

# Inisialisasi suara
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        return "Good Morning!"
    elif hour < 18:
        return "Good Afternoon!"
    else:
        return "Good Evening!"

# GUI Class
class VirtualAssistantGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Nathan Assistant")
        self.root.geometry("600x400")
        self.root.config(bg="#1e1e1e")

        self.label = tk.Label(root, text="Nathan Assistant", bg="#1e1e1e", fg="grey", font=("Helvetica", 14))
        self.label.pack(pady=20)

        self.text_entry = tk.Entry(root, font=("Helvetica", 12), width=40)
        self.text_entry.pack(pady=10)

        self.button_frame = tk.Frame(root, bg="#1e1e1e")
        self.button_frame.pack(pady=10)

        tk.Button(self.button_frame, text="Run", command=self.process_command).grid(row=0, column=0, padx=5)
        tk.Button(self.button_frame, text="Voice", command=self.listen_command).grid(row=0, column=1, padx=5)
        tk.Button(self.button_frame, text="Open File", command=self.open_file).grid(row=0, column=2, padx=5)

        self.output = tk.Text(root, height=10, bg="#2d2d2d", fg="lime", font=("Courier", 10))
        self.output.pack(pady=10)

        greeting = greet()
        self.display_output(greeting)
        speak(greeting)

    def display_output(self, message):
        self.output.insert(tk.END, f"{message}\n")
        self.output.see(tk.END)

    def process_command(self):
        command = self.text_entry.get()
        self.display_output(f"> {command}")
        self.text_entry.delete(0, tk.END)
        self.execute_command(command)

    def listen_command(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            self.display_output("Listening...")
            audio = recognizer.listen(source)
            try:
                command = recognizer.recognize_google(audio, language="id-ID")
                self.display_output(f"Didengar: {command}")
                self.execute_command(command)
            except sr.UnknownValueError:
                self.display_output("Maaf, nggak kedengeran jelas.")
            except sr.RequestError:
                self.display_output("Error: Tidak bisa mengakses layanan Google.")

    def execute_command(self, command):
        command = command.lower()
        if "buka youtube" in command:
            webbrowser.open("https://youtube.com")
            speak(" Open YouTube")
        elif "buka Google" in command:
            webbrowser.open("https://google.com")
            speak("Membuka Google")
        elif "buka whatsapp" in command:
            webbrowser.open("https://web.whatsapp.com/")
            speak("Membuka Whatssapp")
        elif "buka facebook" in command:
            webbrowser.open("https://www.facebook.com/")
            speak("Membuka Whatssapp")
        elif "buka instagram" in command:
            webbrowser.open("https://www.instagram.com/")
            speak("Membuka Whatssapp")
        elif "buka x" in command:
            webbrowser.open("https://x.com/")
            speak("Membuka Whatssapp")
        elif "cari" in command:
            topic = command.replace("cari", "").strip()
            try:
                webbrowser.open("https://en.wikipedia.org/wiki/" + topic.replace(" ", "_"))
                result = wikipedia.summary(topic, sentences=2)
                self.display_output(result)
                speak(result)
            except:
                self.display_output("Topik tidak ditemukan di Wikipedia.")
                speak("Maaf, topik tidak ditemukan.")
        elif "jam berapa" in command:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            self.display_output(f"Sekarang jam {now}")
            speak(f"Sekarang jam {now}")
        elif "berita" in command:
            webbrowser.open("https://news.google.com")
            speak("Membuka berita terbaru")
        elif "main musik" in command:
            music_folder = filedialog.askdirectory(title="Pilih Folder Musik")
            if music_folder:
                files = os.listdir(music_folder)
                for file in files:
                    if file.endswith(".mp3") or file.endswith(".wav"):
                        file_path = os.path.join(music_folder, file)
                        subprocess.Popen(["start", file_path], shell=True)
                        self.display_output(f"Memainkan: {file}")
                        speak(f"Memainkan {file}")
                        break
        elif "keluar" in command:
            speak("Sampai jumpa!")
            self.root.quit()
        else:
            self.display_output("Perintah tidak dikenali.")
            speak("Perintah tidak dikenali.")

    def open_file(self):
        file_path = filedialog.askopenfilename(title="Pilih File")
        if file_path:
            os.startfile(file_path)
            self.display_output(f"Membuka file: {file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = VirtualAssistantGUI(root)
    root.mainloop()




#please help us to make this project powerful and useful
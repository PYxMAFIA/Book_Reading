import pyttsx3
import threading
import time
import os

def slow_print(text, delay=0.05, end='\n'):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay if char != '\n' else 0.5)
    print(end, end='', flush=True)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)  # Try voices[1] for female on most systems


def speak(text):
    engine.say(text)
    engine.runAndWait()

file_path = "Atmosphere (Taylor Jenkins Reid) (Z-Library).txt"
if not os.path.exists(file_path):
    print("❌ File not found.")
    exit()

with open(file_path, encoding="utf-8") as f:
    text = f.read()

print("\033[1;35m📖 Welcome to the Book Reader\033[0m\n")

# Speak + Print at same time
threading.Thread(target=speak, args=(text,), daemon=True).start()
slow_print(text)

while True:
    repeat = input("\n🔁 Do you want to hear the book again? (y/n): ").strip().lower()
    if repeat == 'y':
        thread = threading.Thread(target=speak, args=(text,), daemon=True)
        thread.start()
        thread.join()
        print("\n✅ Done reading the book.")
    elif repeat == 'n':
        print("\n📚 Thanks for listening!")
        break
    else:
        print("❌ Please enter 'y' or 'n'.")


print("\n✅ Done reading the book.")

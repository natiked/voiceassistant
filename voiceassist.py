import speech_recognition as sr
import os
import pyttsx3
import pywhatkit
import datetime
import webbrowser 
from time import ctime
import wikipedia
import pyjokes
import subprocess
import time 

subprocess.call("cls", shell=True)

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
# url = 'https://google.com/search?q='

name = input("What is your name: ")
print("\t\t\t\t\t\t\t##############################")
print("\t\t\t\t\t\t\t\tWelcome " + name)
print("\t\t\t\t\t\t\t##############################")

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Welcome " + name)
speak("How can I help you " + name)

def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        voice = listener.listen(source) 
        command = '' 
    try:
        time.sleep(5)
        print("[+] Recognizing")
        command = listener.recognize_google(voice)        
    except Exception as ex:
        speak("Couldn't detect voice")
        print("[-] Couldn't detect voice")
        print("retrying ...")
        take_command()  
    return command 

def run_atlas():
    #command = take_command()
    if 'play' in command:
        clip = command.replace('play','')
        speak('playing' + clip)
        print('playing' + clip)
        pywhatkit.playonyt(clip)
    elif 'time' in command:
        time = ctime()
        print(time)
        speak('Current time is ' + time)
    elif 'who is ' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, sentences = 3)
        print(info)
        speak(info)
    elif 'joke' in command:
        speak(pyjokes.get_joke())
    elif 'search' in command:
        search = command.replace('search','')
        pywhatkit.search(command) 
    elif 'calculator' in command:
        subprocess.Popen('C:\\Windows\\System32\\calc.exe')
    elif 'notepad' in command:
        subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
    elif 'instagram' in command:
        pywhatkit.search("instagram") 
    elif 'facebook' in command:
        pywhatkit.search("facebook") 
    elif 'find' in command:
        location = command.replace('find', '')
        maps = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(maps)
    elif 'exit' in command:
        exit()
    else:
        print("Unknown command. Retrying...")
        speak("Unknown command. Retrying")
        take_command()
  
while True: 
    command = take_command() 
    run_atlas()

    
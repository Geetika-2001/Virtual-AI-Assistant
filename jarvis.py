from math import e
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import sys
 


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning')
        speak("I am Jarvis Sir,how may i help you?")
        print('Hello Sir,How may i help you?')

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
        speak("How may i help you?")
        print('Hello Sir,How may i help you?')

    else:
        speak("Good Evening")
        speak("I am Jarvis Sir,how may i help you?")
        print('Hello Sir,How may i help you?')


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        # Using google for voice recognition.
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        # Say that again will be printed in case of improper voice
        print("Say that again please...")
        return "None"  # None string will be returned
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('geet20cs@gmail.com', 'megk32001cs')
    server.sendmail('gunjikakaushik.smg@gmail.com', to, content)
    server.close()


def new_func(music_dir, songs):
    os.path.join(music_dir, songs[0])

if __name__ == "__main__":
    wishMe()
    while True:
      if 1:
        query = takeCommand().lower()  # Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  # if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
            
        elif "open google" in query:
            webbrowser.open("google.com")
            
        elif "open spotify" in query:
            webbrowser.open("spotify.com") 
        
        elif "open gmail" in query:
            webbrowser.open("gmail.com")  
        
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")         
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")
            
        elif "open code" in query:
            codePath = 'C:\\Users\\Geetika\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codePath)   
        
        elif "Play music" in query:
            music_dir = 'C:\\Users\\Geetika\\Documents\\music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(new_func(music_dir, songs))
            
        elif "email to geetika" in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "geetikakaushik2001@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry my friend,not able to sent this email")
         
        elif "quit"  in query: 
            quit()
          
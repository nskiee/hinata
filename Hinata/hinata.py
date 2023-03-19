import datetime
import pyjokes
import pywhatkit
import os
import time
import webbrowser
import pyfiglet as pp
import pyttsx3
import speech_recognition as sr
import wikipedia
from tkinter import *

class hinata:
    
    def clear(self,tb): 
        os.system('cls') #on Windows System
        tb.delete('1.0', END)

    def __init__(self):  
        ascii_banner = pp.figlet_format("Hai I'm Hinata")
        print(ascii_banner)
       
        
    def talk(self, text):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say(text)
        engine.runAndWait()
        
    def wishMe(self):
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour <12 :
            self.talk("Good Morning Sir !")
        elif hour>= 12 and hour<18:
            self.talk("Good Afternoon Sir !")
        else:
            self.talk("Good Evening Sir !")
        self.talk("I'm Hinata 2.o")
        self.talk("I am your Assistant")
        self.talk("How can i help you,Boss")

    def take_command(self, tb, root):
        try:
            listener = sr.Recognizer()
            with sr.Microphone() as source:
                tb.insert(END,'listening...'+ '\n')
                root.update()
                voice = listener.listen(source, timeout=600)
                command = listener.recognize_google(voice)
                command = command.lower()
                if 'hinata' in command:
                    command = command.replace('hinata', '')
                    self.talk(command)
                    tb.insert(END,command+ '\n')
        except Exception as e:
            tb.insert(END,e )
            root.update()
            tb.insert(END,"Unable to Recognize your voice."+ '\n')
            root.update()
        return(command)
    
    def startup(self,tb, root):
        self.wishMe()
        self.clear(tb)
        while True:
            self.run_talk(tb, root)
    
    def run_talk(self,tb, root):

        try:

            command = self.take_command(tb , root)

            if 'who made you' in command or 'who created you' in command:
                tb.insert(END,'I was created by ThunderGod'+ '\n')
                root.update()
                self.talk('i was created by thundergod')

            
            if 'play' in command:
                song = command.replace('play', '')
                tb.insert(END,'playing...'+ '\n')
                root.update()
                self.talk('playing'+song)
                pywhatkit.playonyt(song)

            elif 'how are you' in command:
                tb.insert(END,'Iam fine, Thank you Boss'+ '\n')
                root.update()
                self.talk('iam fine thank you Boss')

            elif "where is" in command:
                command = command.replace("where is", "")
                location = command
                self.talk("User asked to Locate")
                self.talk(location)
                webbrowser.open("https://www.google.com/maps/place/" +location)

            elif 'time' in command:
                times = datetime.datetime.now().strftime('%I %M %S %p')
                tb.insert(END,times + '\n')
                root.update()
                self.talk('Time is :' +times)
            
            elif 'reminder' in command:
                tb.insert(END,"What shall I remind you about?"+ '\n')
                root.update()
                self.talk("What shall I remind you about?")
                text = str(input())
                tb.insert(END,"In how many minutes?"+ '\n')
                root.update()
                self.talk("with in how many minutes")
                local_time = float(input())
                local_time = local_time * 60
                time.sleep(local_time)
                self.talk("reminder:"+text)
                self.talk("wake up dude its time for some work")
                tb.insert(END,text+ '\n')
                root.update()
            elif 'open google' in command:
                self.talk("here opening google")
                webbrowser.open("google.com")

            elif 'open my cam' in command:
                self.talk("opening mycamu")
                webbrowser.open("mycamu.com")

            elif 'who is' in command:
                person = command.replace('who is', '')
                info = wikipedia.summary(person, 1)
                tb.insert(END,info+ '\n')
                root.update()
                self.talk(info)

            elif 'date' in command:
                date = datetime.datetime.now().strftime("%d-%m-%Y")
                tb.insert(END,date+ '\n')
                root.update()
                self.talk('Today is :' +date)
            
            elif 'joke' in command:
                jokes = pyjokes.get_joke()
                tb.insert(END,jokes+ '\n')
                root.update()
                self.talk('Let me raise a toast :'+jokes)
            
            elif 'are you single' in command:
                self.talk('sorry, I am in relationship with my boss')

            elif 'stop it' in command:
                self.talk("Thanks for giving me your time")
                exit()

            else:
                self.talk('Sorry, i didnt get you, Please say it one more time..')
        except Exception as e:
            self.talk("Sorry... I didn't reconize your voice.. Please say it one more time")
            tb.insert(END,e)
            tb.insert(END,"Unable to Recognize your voice."+ '\n')
            root.update()

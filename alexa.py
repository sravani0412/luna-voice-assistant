import speech_recognition as sr
import pyttsx3 
import datetime as dt
import pywhatkit as pk
import wikipedia as wiki
import webbrowser
import os 

listener= sr.Recognizer()
speaker=pyttsx3.init()  # initialising speaker
# setting up new voice rate

"""VOICE"""
voices = speaker.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
speaker.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

def speak(text):
    speaker.say('yes madam, ' + text)
    speaker.runAndWait()

def speak_ex(text):
    speaker.say( text)
    speaker.runAndWait()

va_name=  ' nuna '  

speak_ex('iam your' + va_name + ' tell me madam how can i assist you  ' )


def command():
    command=" "
    try:
        with sr.Microphone() as source:
            listener= sr.Recognizer()
            print('Listening....')
            voice = listener.listen(source)  # taking audio data as input
            command=listener.recognize_google(voice)  # passing our audio data as argument 
            command=command.lower()
            if 'va_name' in command:
                command=command.replace(va_name + ' ','')
                print(command)
                speak(command)

    except:
        print('check your microphone')
    return command

while True:
    user_command=command()
    if 'close' in user_command:
        print(' see you madam. i will be there whenever you call me ')         
        speak(' see you madam. i will be there whenever you call me ') 
        break
    elif 'time' in user_command:
        current_time=dt.datetime.now().strftime("%I:%M:%p")
        print(current_time)
        speak(current_time)
    elif 'play' in user_command:
        user_command=user_command.replace('play','')
        print('playing' + user_command)
        speak('playing' + user_command+',enjoy madam')
        pk.playonyt(user_command)
        break
    elif 'search for ' in user_command or 'google ' in user_command:
        user_command=user_command.replace('search for ','')
        user_command=user_command.replace('google','')
        speak('searching for'+ user_command)
        pk.search(user_command)
    elif ' who is ' in user_command:
        user_command=user_command.replace('who is ','')
        info=wiki.summary(user_command,2)
        print(info)
        speak(info)
    elif 'who are you' in user_command:
        speak_ex('iam your personal voice assistant'+ va_name+', tell me madam')    
    else:
        speak_ex('please say it again boss')








    




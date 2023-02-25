import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import cv2
import pyjokes

#OUR CHATBOT CAN DO FOUR WORKS(https://www.i2tutorials.com/build-chatbot-using-python/)
#1.ASK QUESTIONS
#2.LANGUAGE UNDERSTANDING
#3.VISION
#4.SPEECH RECOGNITION

listener = sr.Recognizer()  ##RECOGNIZER HERE USED TO RECOGNIZE YOUR VOICE
engine= pyttsx3.init() #FOR INITIALIZING PYTHON TEXT TO SPEECH(CONVERT TEXT INTO SPEECH)
#voices = engine.getProperty('voices')
#engine.setProperty('voices', voices[1].id) #TO CONVERT BOY VOICE INTO GIRL VOICE??

def talk(text):
    if text=="start":
        engine.say("HI!MY NAME IS RIMSHA")
        engine.say("WELCOME TO MY BOT")
        engine.runAndWait()
    else:
        if text=="finish":
            engine.say("BYE")
            engine.say("I HAVE A GOOD CONVERSATION WITH YOU")
            engine.runAndWait()
        else:
            engine.say(text)
            engine.runAndWait()


def take_command():
    try:
       with sr.Microphone() as source:  ##SOURCE OF OUR AUDIO WHICH IS MICROPHONE
            print('LISTENING...') ##ALEXA IS READY TO LISTEN WHATEVER I SAY
            ##LISTEN VOICE
            voice = listener.listen(source)  ##WE USE MICROPHONE TO LISTEN TO THE SOURCE

            #RECOGNIZE VOICE AND CONVERT IT INTO TEXT
            command = listener.recognize_google(voice)  ##TO CONVERT VOICE TO TEXT.WE PASS THIS TO GOOGLE.GOOGLE WILL GIVE YOU THE TEXT
            command=command.lower()

            #AS THE BOT IS OF ALEXA SO IF ALEXA IS IN SPEECH IT PRINT COMMAND OTHERWISE IT MOVE(AGARALEXA COMMAND ME HOGA TO WO PRINT KRE G OTHERWISE WO AGE MOVE KRJAI GA
            if 'start' in command:
                talk(command)
                command = command.replace('start','') #start will be removed from the string
                print(command)

            else:
               talk(command)
    except:
       pass

    return command


def run_alexa():
     command = take_command() #take command from user
     #print(command)

     if 'play' in command:
        song = command.replace('play','')
        talk('playing'+song)
        print(song)
        #TO SEARCH AND PLAY SONGS ON YOUTUBE
        pywhatkit.playonyt(song)

     elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        talk('Current time is' + time)


     elif 'who the heck is' in command:
         person = command.replace('who the heck is','')
         info = wikipedia.summary(person,1)
         print(info)
         talk(info)

     elif 'date' in command:
         talk('sorry,I have a headache')

     elif 'are you single' in command:
         talk('I am in relationship with wifi')

     elif 'joke' in command:
         talk(pyjokes.get_joke())
         print(pyjokes.get_joke())


while True:
    run_alexa()
# # Voice Recognization using Python

# ### Text to speec ###


# # import pyttsx3 import time engine = pyttsx3.init() engine.say('What
# # is the time now?') time.sleep(2) engine.say('It is 28 past 9')
# # engine.runAndWait()

# # from gtts import gTTS
# # import os
# # tts = gTTS(text='Hi, How are you? What do you do? ', lang='en')
# # tts.save("good.mp3")
# # os.system("good.mp3")


# import speech_recognition as sr                                               # pip install SpeechRecognizarion
# from gtts import gTTS                                                         # pip instal gtts --> Google text to speech
# import os

#  # obtain audio from the microphone  
# r = sr.Recognizer()                                                           # creating speech recognization object
# with sr.Microphone() as source:                                               # idenify audio with microphone , comes form micropone
#    print("Say something!")                                          
#    audio = r.listen(source)                                                   # creating audio file using listen function
   
#  # recognize speech using Sphinx                                              # pip install packetsphinx
# try:  
#    print("Sphinx thinks you said '" + r.recognize_sphinx(audio)               # using spinx module convert audio into text , print it
#    + "'") 
#    tts = gTTS(r.recognize_sphinx(audio), lang='en')                           # tts object to save text file to audio
#    tts.save("good.mp3")
#    os.system("good.mp3")                                                      # play saved audio
# except sr.UnknownValueError:     
#    print("Sphinx could not understand audio")  
# except sr.RequestError as e:  
#    print("Sphinx error; {0}".format(e))  


# # from chatterbot import ChatBot
# # from chatterbot.trainers import ListTrainer

# # # Create a new chat bot named Charlie
# # chatbot = ChatBot('Charlie')

# # trainer = ListTrainer(chatbot)

# # trainer.train([
# #     "Hi, can I help you?",
# #     "Sure, I'd like to book a flight to Iceland.",
# #     "Your flight has been booked."
# # ])

# # # Get a response to the input text 'I would like to book a flight.'
# # response = chatbot.get_response('I would like to book a flight.')

# # print(response)



# Global imports 
import random
import datetime
import webbrowser
import pyttsx3
import wikipedia
import speech_recognition as sr

#Local imports 
from pygame import mixer


# Set up and calibrate the text to speech engine.Now we need to set the voice
# rate, engine, etc.

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
volume = engine.getProperty('volume')
engine.setProperty('volume', 10.0)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 25)

# Create lists with your preset questions answers.The more the lists the better.
#  But too many lists can slowdown the chat bot.
greetings = ['hey there', 'hello', 'hi', 'Hai', 'hey!', 'hey']
question = ['How are you?', 'How are you doing?', 'How is going on']
responses = ['Okay', "I'm fine"]
var1 = ['who made you', 'who created you']
var2 = ['I_was_created_by_Edward_right_in_his_computer.', 'Edward',
        'Some_guy_whom_i_never_got_to_know.']
var3 = ['what time is it', 'what is the time', 'time']
var4 = ['who are you', 'what is you name']
cmd1 = ['open browser', 'open google']
cmd2 = ['play music', 'play songs', 'play a song', 'open music player']
cmd3 = ['tell a joke', 'tell me a joke', 'say something funny',
        'tell something funny']
jokes = ['Can a kangaroo jump higher than a house? Of course,'
         ' a house doesn’t jump at all.',
         'My dog used to chase people on a bike a lot. It got so bad,'
         ' finally I had to take his bike away.',
         'Doctor: Im sorry but you suffer from a terminal illness and have only'
         ' 10 to live.Patient: What do you mean, 10? '
         '10 what? Months? Weeks?!"Doctor: Nine.']
cmd4 = ['open youtube', 'i want to watch a video']
cmd5 = ['tell me the weather', 'weather', 'what about the weather']
cmd6 = ['exit', 'close', 'goodbye', 'nothing']
cmd7 = ['what is your color', 'what is your colour', 'your color',
        'your color?']
colrep = ['Right now its rainbow', 'Right now its transparent',
          'Right now its non chromatic']
cmd8 = ['what is you favourite colour', 'what is your favourite color']
cmd9 = ['thank you']
repfr9 = ['youre welcome', 'glad i could help you']

'''
Calibrate the speech recognition engine.We are going to use the google speech
recognition engine. Set the engine details.Also use the while loop to
restart the engine in case of any errors.
'''
while True:
    now = datetime.datetime.now()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tell me something:")
        audio = r.listen(source)
        try:
            print("You said:- " + r.recognize_google(audio))
        except sr.UnknownValueError:
            print("Could not understand audio")
            engine.say('I did not get that. Rerun the code')
            engine.runAndWait()

# Use a loop code with random and Wikipedia to finish the code.
# We are going to use the above mentioned modules in a loop code to create
# the main functional code.

    if r.recognize_google(audio) in greetings:
        random_greeting = random.choice(greetings)
        print(random_greeting)
        engine.say(random_greeting)
        engine.runAndWait()
    elif r.recognize_google(audio) in question:
        engine.say('I am fine')
        engine.runAndWait()
        print('I am fine')
    elif r.recognize_google(audio) in var1:
        engine.say('I was made by edward')
        engine.runAndWait()
        reply = random.choice(var2)
        print(reply)
    elif r.recognize_google(audio) in cmd9:
        print(random.choice(repfr9))
        engine.say(random.choice(repfr9))
        engine.runAndWait()
    elif r.recognize_google(audio) in cmd7:
        print(random.choice(colrep))
        engine.say(random.choice(colrep))
        engine.runAndWait()
        print('It keeps changing every micro second')
        engine.say('It keeps changing every micro second')
        engine.runAndWait()
    elif r.recognize_google(audio) in cmd8:
        print(random.choice(colrep))
        engine.say(random.choice(colrep))
        engine.runAndWait()
        print('It keeps changing every micro second')
        engine.say('It keeps changing every micro second')
        engine.runAndWait()
    elif r.recognize_google(audio) in cmd2:
        mixer.init()
        mixer.music.load("C:\\Users\Edward Zion SAJI\Downloads\Mighty_God_-_Martin__Colleen_Rebeiro.55145718.wav")
        mixer.music.play()
    elif r.recognize_google(audio) in var4:
        engine.say('I am edza your personal AI assistant')
        engine.runAndWait()
    elif r.recognize_google(audio) in cmd4:
        webbrowser.open('www.youtube.com')
    elif r.recognize_google(audio) in cmd6:
        print('see you later')
        engine.say('see you later')
        engine.runAndWait()
        exit()
    elif r.recognize_google(audio) in cmd5:
        owm = pyowm.OWM('YOUR_API_KEY')
        observation = owm.weather_at_place('Bangalore, IN')
        observation_list = owm.weather_around_coords(12.972442, 77.580643)
        w = observation.get_weather()
        w.get_wind()
        w.get_humidity()
        w.get_temperature('celsius')
        print(w)
        print(w.get_wind())
        print(w.get_humidity())
        print(w.get_temperature('celsius'))
        engine.say(w.get_wind())
        engine.runAndWait()
        engine.say('humidity')
        engine.runAndWait()
        engine.say(w.get_humidity())
        engine.runAndWait()
        engine.say('temperature')
        engine.runAndWait()
        engine.say(w.get_temperature('celsius'))
        engine.runAndWait()
    elif r.recognize_google(audio) in var3:
        print("Current date and time : ")
        print(now.strftime("The time is %H:%M"))
        engine.say(now.strftime("The time is %H:%M"))
        engine.runAndWait()
    elif r.recognize_google(audio) in cmd1:
        webbrowser.open('www.google.com')
    elif r.recognize_google(audio) in cmd3:
        jokrep = random.choice(jokes)
        engine.say(jokrep)
        engine.runAndWait()
    else:
        engine.say("please wait")
        engine.runAndWait()
        print(wikipedia.summary(r.recognize_google(audio)))
        engine.say(wikipedia.summary(r.recognize_google(audio)))
        engine.runAndWait()
        userInput3 = input("or else search in google")
        webbrowser.open_new('www.google.com/search?q=' + userInput3)




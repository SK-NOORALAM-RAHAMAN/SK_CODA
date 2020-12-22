import pyttsx3,datetime,speech_recognition as sr,time,wikipedia,webbrowser,os,random

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait() 

def WishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=5 and hour<12:
        speak("Good Morning sir")
    elif hour>=12 and hour<16:
        speak("Good Afternoon sir")
    elif hour>=16 and hour<22:
        speak("Good Evening sir")
    else:
        speak("sir,this is your sleeping time")
        # speak("A Good Sleep is important for a good Health,")
        # speak("Else, You might be Studying")

    speak("I am Sara.")
    speak("Your Personal Voice Assistant.")
    speak("What can i do for you.")

def takeCommand():
    '''
    input: Voice Input
    return: String Output
    '''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....\n")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing ",end="")
        time.sleep(1),print("--", end="")
        time.sleep(1),print("--")
        query=r.recognize_google(audio, language='en-in')
        print(f"[You said: {query}]\n")

    except Exception as e:
        # print(e)
        speak("Sorry sir i can't Here You,")
        speak("Your Internet may be Disconnected.")
        speak("Please Say that again.")
        print("Please Check your Internet connection & try again.!")
        return "None"
    return query


if __name__ == '__main__':
    print("* SA",end=""),time.sleep(1),print("RA * ",end="")
    print("Waked up..\n")
    WishMe()
    while True:
     query=takeCommand().lower()
     #Logic for executing tasks
     if 'wikipedia' in query:
         speak('Searching Wikipedia..')
         query=query.replace('wikipedia',"")
         results=wikipedia.summary(query,sentences=2)
         speak("According to wikipedia..")
         print(results)
         speak(results)
     elif 'open youtube' in query:
         speak("opening youtube")
         time.sleep(1)
         webbrowser.open_new_tab('youtube.com')

     elif 'open facebook' in query:
         speak("opening facebook")
         time.sleep(1)
         webbrowser.open_new_tab('facebook.com')

     elif 'open google' in query:
         speak("opening google ")
         time.sleep(1)
         webbrowser.open_new_tab('google.com')

     elif 'open stackoverflow' in query:
         speak("searching stackoerflow")
         time.sleep(1)
         webbrowser.open_new_tab('stackoverflow.com')

     elif 'the time' in query:
         curr_time=datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"Sir,the time is {curr_time}")

     elif 'open vs code' in query:
         app_path="C:\\Users\\SK NOORALAM RAHAMAN\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
         os.startfile(app_path)

     elif 'play music' in query:
         speak("playing music")
         speak("Get ready for change your mood..")
         time.sleep(1)
         music_dir='E:\\YOU TUBE VIDEOS\\febhd'
         songs=os.listdir(music_dir)
         num =int(len(songs)-1)
         print(songs)
         while True:
             number = [i for i in range(0, num)]
             r = random.choice(number)
             os.startfile(os.path.join(music_dir, songs[r]))
             if 'Next song' in query:
                os.startfile(os.path.join(music_dir,songs[r+1]))
             elif 'previous song' in query:
                 os.startfile(os.path.join(music_dir, songs[r -1]))
             elif 'stop music' in query or (r==0 and 'previous song' in query):
                 break


     elif 'sleep' in query:
         speak("Ok sir")
         exit()



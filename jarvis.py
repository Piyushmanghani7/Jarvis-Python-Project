import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice',voices[0].id)
print(voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour>=0 and hour<12:
        speak("Good MOrning Piyush manghani")
    elif hour>=12 and hour<18:
        speak("Good afternoon piyush manghani")
    else:
        speak("Good evening piyush manghani")

    speak("Hello i am jarvis sir , please tell how may i help you.")

def takecommand():

    '''
    it takes our microphone input command by recognising the speech of user and give output as string.
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening........")
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said.. {query}\n")
    except Exception as e:
        print(e)
        print("say that again")
        return "None" # return none string

    return query # return this listening query in the string

def sendemail(to,content):
    server = smtplib.SMTP("smtp.gmail.com",587)
#     587 is the port on which we want to send the email.
    server.ehlo()
    server.starttls()
    server.login("piyush.manghani10@gmail.com" , "password")
    server.sendmail("piyush.manghani10@gmail.com",to,content)
    server.close()


if __name__ == '__main__':
   speak("hello piyush , welcome in the jarvis ")
   wishme()


   while True :

      query = takecommand().lower()
      if 'wikipedia' in query:
        try:
          speak("searching in wikipedia....")
          query = query.replace("wikipedia","")
          result = wikipedia.summary(query,sentences=2)
          print(result)
          speak("according to the wikipedia")
          speak(result)

        except Exception as e:
           speak(e)

      elif "open youtube" in query:
        webbrowser.open("youtube.com")

      elif "open google" in query:
        webbrowser.open("google.com")
      elif "sindhi" in query:
        speak("mukhe nathi indi ayhe")

      elif "open stackoverflow" in query:
        webbrowser.open("stackoverflow.com")

      elif " open time" in query:
        strtime = datetime.datetime.now().strftime("%H:%M:%S")
        print(strtime)
        speak(f"sir the time is {strtime}")
      elif "play music" in query:
          music_dir ="F:\\songs,movies,episodes\\latest songs\\90s songs"
          songs = os.listdir(music_dir)
          print(songs)
          # random.shuffle(songs)
          i = int(random.randint(0,len(songs)-1))
          random.shuffle(songs)
          print(i)
          os.startfile(os.path.join(music_dir,songs[i]))
      elif "open pycharm" in query:
          code_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains"
          os.startfile(code_path)

      elif "send mail" in query:
          try:
              speak("what should i send?")
              content = takecommand()
              to = "piyush.manghani10@gmail.com"
              sendemail(to,content)
              speak("email has been send , thanks piyush")
          except Exception as e:
              speak(f"sorry piyush i cant send the email to this email id due to {e}")


import pyttsx3
import speech_recognition
ear = speech_recognition.Recognizer()



def speak(text:str):
    speaker = pyttsx3.init()
    speaker.say(text)
    speaker.runAndWait()

def listen()->str:
    with speech_recognition.Microphone(0) as mic:
        print("succesfully init microphone!")
        user_input = ear.listen(mic, timeout=2, phrase_time_limit=2)
        print("got sound")
        text = ear.recognize_google(user_input)
        text = text.lower()
        speak(text)
        return text

#DEMO
test = listen()


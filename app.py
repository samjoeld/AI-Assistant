import nltk

nltk.download('punkt')
import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"User: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't get that.")
        return ""
    except sr.RequestError as e:
        print(f"Request failed: {e}")
        return ""


def main():
    
    speak("Hello! I am Virtual  assistant  How can I help you?")
    while True:
        query = listen()
        if "hello" in query:
            speak("Hi Sam, I am your  assistant. What can I do for you?")
        elif "who is your creator" in query:
            speak("Mr.Sam, is my one and only Author and creator. He is one of the best person and best leader")
        elif "how are you" in query:
            speak("I am fine Mr.Sam Joel, what about you sam?")
        elif "fine and thank you" in query:
            speak("Welcome, i hope your life is good to go")
        elif "about your life" in query:
            speak("Sorry man, i am a Robot so i have no life, no feelings ")
        elif "bye" in query:
            speak("Goodbye, Thank you Have a nice day")
            break
        else:
            speak("I'm sorry, I didn't understand. Can you please repeat?")


if __name__ == "__main__":
    main()

import openai
import speech_recognition as sr
import pyttsx3

# Set up OpenAI API
openai.api_key = 'your_api_key_here'

# Initialize the recognizer
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def process_command(command):
    # Call OpenAI API to get response
    response = openai.Completion.create(
        model="davinci",
        prompt=command,
        temperature=0.7,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response.choices[0].text.strip()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
        return ""
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return ""

def speak(response):
    engine.say(response)
    engine.runAndWait()

if __name__ == "__main__":
    while True:
        command = listen()
        if command:
            if command.lower() == "exit":
                break
            response = process_command(command)
            print("AI:", response)
            speak(response)

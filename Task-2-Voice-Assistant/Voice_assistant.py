import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize recognizer and speaker
listener = sr.Recognizer()
speaker = pyttsx3.init()

def speak(text):
    speaker.say(text)
    speaker.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print("You said:", command)
            return command
    except:
        return ""

speak("Hello, I am your voice assistant")

while True:
    command = take_command()

    if "hello" in command:
        speak("Hello, how can I help you")

    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        speak("The current time is " + time)

    elif "date" in command:
        date = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today's date is " + date)

    elif "search" in command:
        speak("What should I search")
        search_query = take_command()
        webbrowser.open("https://www.google.com/search?q=" + search_query)
        speak("Here are the search results")

    elif "exit" in command or "stop" in command:
        speak("Goodbye")
        break

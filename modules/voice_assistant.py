import pyttsx3

# Initialize the voice engine
engine = pyttsx3.init()

# Set speaking speed
engine.setProperty("rate", 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()
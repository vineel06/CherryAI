import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 165)
engine.setProperty("volume", 1.0)

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(text: str, mode: str = "vecna"):
    if mode == "vecna":
        engine.setProperty("rate", 150)
    elif mode == "puppy":
        engine.setProperty("rate", 190)

    engine.say(text)
    engine.runAndWait()

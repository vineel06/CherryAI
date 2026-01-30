import speech_recognition as sr

recognizer = sr.Recognizer()


def listen() -> str:
    """
    Listens from the default microphone and returns recognized text.
    """

    try:
        with sr.Microphone() as source:
            print("🎙️ Cherry is listening... Speak now.")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source)

        print("🧠 Processing voice input...")

        # Google speech recognition (stable)
        text = recognizer.recognize_google(audio)
        print("👤 You said:", text)
        return text

    except sr.UnknownValueError:
        print("⚠️ Could not understand audio")
        return ""

    except sr.RequestError as e:
        print("❌ Speech recognition service error:", e)
        return ""

    except Exception as e:
        print("❌ Microphone error:", e)
        return ""

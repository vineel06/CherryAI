from voice.listener import listen
from voice.speaker import speak
from core.brain import cherry_think


def voice_chat(mode="vecna"):
    """
    One full voice interaction:
    Listen → Think → Speak
    """

    user_text = listen()
    if not user_text:
        speak("I didn't catch that.", mode)
        return

    response = cherry_think(user_text)
    speak(response, mode)

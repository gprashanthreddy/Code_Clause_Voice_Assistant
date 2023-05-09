import speech_recognition as sr
from assistant import VoiceAssistant

# Initialize the recognizer
r = sr.Recognizer()

# Create an instance of the VoiceAssistant
assistant = VoiceAssistant()

# Use the default microphone as the audio source
with sr.Microphone() as source:
    # Adjust for ambient noise
    r.adjust_for_ambient_noise(source)
    print("Listening...")
    while True:
        try:
            # Listen for audio input
            audio = r.listen(source)
            # Convert audio to text
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            # Pass text to the VoiceAssistant to process and respond
            response = assistant.process_request(text)
            print(f"Assistant: {response}")
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

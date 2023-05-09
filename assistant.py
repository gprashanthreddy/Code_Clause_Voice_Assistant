import random
import webbrowser
import datetime
import os
import speech_recognition as sr
import pyttsx3


class VoiceAssistant:
    def __init__(self):
        self.greetings = ["hello", "hi", "hey", "hi there"]
        self.goodbyes = ["bye", "goodbye", "see you", "take care"]
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.commands = {
            "what is your name": self.get_name,
            "what time is it": self.get_time,
            "tell me a joke": self.tell_joke,
            "play some music": self.play_music,
            "stop the music": self.stop_music,
            "search the web": self.search_web,
            "nothing": self.say("You are welcome")
        }
        self.music_playing = False

    def say(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def get_name(self):
        self.say("My name is Assistant!")

    def get_time(self):
        time = datetime.datetime.now().strftime("%I:%M %p")
        self.say("It's currently " + time)

    def tell_joke(self):
        jokes = ["Why did the tomato turn red? Because it saw the salad dressing!",
                 "What did one wall say to the other? I'll meet you at the corner!",
                 "Why don't scientists trust atoms? Because they make up everything!"]
        self.say(random.choice(jokes))

    def play_music(self):
        self.say("Playing music!")
        # Code to play music

    def stop_music(self):
        self.say("Stopping music!")
        # Code to stop music

    def search_web(self):
        self.say("What do you want me to search for?")
        query = self.get_voice_input()
        url = "https://www.google.com/search?q=" + query
        webbrowser.get().open(url)
        self.say("Here are the search results for " + query)

    def get_voice_input(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        try:
            request = r.recognize_google(audio)
            print("You said: " + request)
            return request
        except sr.UnknownValueError:
            self.say("Sorry, I didn't catch that. Could you please repeat?")
            return self.get_voice_input()

    def process_request(self, request):
        # Convert request to lowercase for case-insensitive matching
        request = request.lower()

        # Check if request is a greeting
        if any(greeting in request for greeting in self.greetings):
            self.say(random.choice(self.greetings).capitalize())
            return

        # Check if request is a goodbye
        if any(goodbye in request for goodbye in self.goodbyes):
            self.say(random.choice(self.goodbyes).capitalize())
            return

        # Check if request matches any commands
        for command, action in self.commands.items():
            if command in request:
                action()
                return

        # If request does not match any commands, apologize and ask for another request
        self.say("I'm sorry, I didn't understand. Could you please repeat?")


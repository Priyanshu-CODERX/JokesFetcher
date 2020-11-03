import requests
import pyttsx3 as pt

# Speech Engine
engine = pt.init()
speaker = engine.getProperty('voice')
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0') # Setting voice property
def speak(speech):
	engine.say(speech)
	engine.runAndWait()
# ------------------------------------------------------

url = "https://official-joke-api.appspot.com/random_joke" 

parameters = {"type":"programming"}
response = requests.get(url=url, params=parameters)

if response.status_code == 200:
    jokes = response.json()
    print(jokes["setup"], jokes["punchline"])
    print(f'Type: {jokes["type"]}')
    speak(jokes["setup"])
    speak(jokes["punchline"])

else:
    print("Cannot get jokes")
    speak("Cannot get jokes")

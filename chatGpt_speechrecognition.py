import os
import openai
import pyttsx3
import requests
import json
import speech_recognition as sr
import random
import webbrowser
print("Speech recognition initialized!")
engine = pyttsx3.init("sapi5")
"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)
openai.api_key = "INSERT YOUR OPENAI API KEY HERE"
def sayText(text):
  engine.say(text)
  engine.runAndWait()
def getR(hi):
  print("Getting response")
  response = openai.Completion.create(model="text-davinci-003", prompt=hi, temperature=0, max_tokens=50)
  text = response["choices"][0]["text"]
  #print(response)
  print(text)
  print("Got AI Response!")
  return text
  
def getChat(msg):
    print("Getting Chat Response")
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a ."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)


def voiceDetect_Google():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    r.energy_threshold = 1000
    #r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
  try:
    assumed_text = r.recognize_google(audio)
    return assumed_text, True
  except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
  except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
  return "", False

while True:
    print("waiting")
    assumed_text, success = voiceDetect_Google()
    print(assumed_text)
    print("Got text")
    if success:
      print("Getting AI...")
      text = getR(assumed_text)
      print(text)
      sayText(text)
a = input()
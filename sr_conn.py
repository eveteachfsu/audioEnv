# -*- coding: utf-8 -*-
# some of these libraries are not necessary
import io
import random
import string
import socket
import warnings
import time
import numpy as np
import warnings
import os
import requests
import sys
import validators
warnings.filterwarnings('ignore')
import speech_recognition as sr 
from io import BytesIO
import urllib

import socket
#import pyttsx3 as p






base_url = "http://34.148.185.194//test_py.php?test="
url = sys.argv[-1].strip() if validators.url(sys.argv[-1].strip()) else base_url

# Routine to send the information to the prim
#     submitInformation(url,information)
#
def submitInformation(url,parameters) :
    # Set the parameters to be sent.
    encodedParams =  urllib.parse.urlencode(parameters).encode("utf-8");

    # Post the data.
    net = urllib.request.urlopen(url,encodedParams);

    # return the result.
    return(net.read());

def send_simworld(url='', query='', response='', speaker=''):
    # Set the URL manually
    url = 'http://hydra.cs.fsu.edu:9000/lslhttp/cd012072-da91-4d24-9848-443c52c5e297/'
    # Define the parameters
    parameters = {'query': query,
                  'response': response,
                  'speaker': speaker}

    # Pass the information along to the prim
    info = submitInformation(url,parameters);
    #print(info);
    
def send_ficil(url='', query='', response='', speaker=''):
    pass

def send_receive_text(query): 
  full_query = url + query
  response = requests.get(full_query)
  print("BOT SAID : {}".format(response.content.decode().split('_')[0]))
  #p.speak("{}".format(response.content.decode().split('_')[0]))
  send_simworld(query=query, response=response.content.decode().split('_')[0], speaker='Student_1')

def audio_text():
    flag=True
    r = sr.Recognizer()
    print("Class Begins")
    # Taking voice input and processing 
    while(flag == True):
        with sr.Microphone() as source:
            audio = r.listen(source,10,10) # Records mic input for up to 10 seconds
        try:
            trnsaudio = format(r.recognize_google(audio)) # transcribes the audio
            print("YOU SAID : {}" .format(trnsaudio))
        except sr.UnknownValueError:
            trnsaudio = 'error'
        if((trnsaudio!='bye') and (trnsaudio!='error')):
            send_receive_text(trnsaudio)      
        elif (trnsaudio == 'error'):
            print("No Audio is detected")
        else:
            flag=False
            print("Thank you have a great day")
audio_text()

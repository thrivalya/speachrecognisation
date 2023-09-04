#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install SpeechRecognition


# In[2]:


pip install pyaudio


# In[4]:


import speech_recognition as sr
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak something...")
    audio = recognizer.listen(source)
try:
    text = recognizer.recognize_google(audio)
    print("You said: " + text)
except sr.UnknownValueError:
    print("Sorry, I couldn't understand what you said.")
except sr.RequestError as e:
    print("Error: {0}".format(e))


# In[5]:


pip install googletrans==4.0.0-rc1


# In[6]:


from googletrans import Translator
translator=Translator()
text_to_translate=input("enter text")
detected_language=translator.detect(text_to_translate).lang
target_language=input("enter language")
translated_text=translator.translate(text_to_translate,src=detected_language,dest=target_language)
ans=translated_text.text
print(translated_text.text)


# In[1]:



import speech_recognition as sr
from googletrans import Translator
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak something...")
    audio = recognizer.listen(source)
try:
    text = recognizer.recognize_google(audio)
    print("You said: " + text)
    translator=Translator()
    detected_language=translator.detect(text).lang
    target_language=input("enter language")
    translated_text=translator.translate(text,src=detected_language,dest=target_language)
    ans=translated_text.text
    print(translated_text.text)
except sr.UnknownValueError:
    print("Sorry, I couldn't understand what you said.")
except sr.RequestError as e:
    print("Error: {0}".format(e))


# In[ ]:





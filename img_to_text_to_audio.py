
#INSTALL the Following Libraries:

# !sudo apt install tesseract-ocr
# !pip install pytesseract
# !pip install Pillow==9.0.0
# !pip install gTTS

import pytesseract  
from PIL import Image 
import pygame
import gtts
#import pyttsx3
#from googletrans import Translator

img = Image.open('Picture1.png')
print(img)

result = pytesseract.image_to_string(Image.open('Picture1.png'))
print(result)
tts = gtts.gTTS(result)
tts.save("hello.mp3")
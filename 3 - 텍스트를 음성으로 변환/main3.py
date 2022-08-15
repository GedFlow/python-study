#파이썬에서 지정한 텍스트 파일을 읽어 음성을 출력하는 코드

from playsound import playsound
from gtts import gTTS
import os

#경로를 현재 main2.py가 있는 위치로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))

filePath = 'test.txt'

with open(filePath, 'rt', encoding='UTF8') as f:
    readFile = f.read()

tts = gTTS(text=readFile, lang='ko')
tts.save(r"hipy3.mp3")

playsound("hipy3.mp3")
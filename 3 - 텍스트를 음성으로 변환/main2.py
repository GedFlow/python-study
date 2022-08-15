#파이썬에서 지정한 텍스트를 mp3로 만들어 저장하고 바로 실행하는 코드. playsound로 실행하는듯

from playsound import playsound
from gtts import gTTS
import os

#경로를 현재 main2.py가 있는 위치로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))

text = "맛있사옵니다 어머뉘"

tts = gTTS(text=text, lang='ko')
tts.save(r"hipy2.mp3")

playsound("hipy2.mp3")
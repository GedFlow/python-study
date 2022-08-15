#파이썬으로 지정한 텍스트를 mp3 파일로 저장하는 코드

from operator import gt
from gtts import gTTS

text = "안녕하세요. 파이썬입니다!"

tts = gTTS(text=text, lang='ko')

#해당 경로에 hipy.mp3라는 이름으로 파일을 생성한다.
tts.save(r"3 - 텍스트를 음성으로 변환\hipy.mp3")
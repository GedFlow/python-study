from random import *

randNum = randint(1, 100)

game_count = 1

while True:
    try:
        myNum = int(input("1~100 사이의 숫자를 입력하세요: "))
        
        if myNum > randNum:
            print("다운")
        elif myNum < randNum:
            print("업")
        elif myNum == randNum:
            print(f"정답입니다. {game_count}회 만에 맞췄습니다!")
            break
        game_count += 1
    except:
        print("에러발생!")
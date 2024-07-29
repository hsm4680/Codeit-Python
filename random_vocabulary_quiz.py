import random

with open('vocabulary.txt', 'r') as f: # 'vocabulary.txt' 파일을 읽기 모드로 열기
    lines = f.readlines() # 파일의 모든 줄을 읽어 리스트로 저장

vocab = {} #딕셔너리 빈 파일 생성

for line in lines: # 파일에서 읽은 각 줄에 대해 반복, for문 전체 아래 depth에 모든 코드를 포함시켜야 무한 반복됨
    data = line.split(": ") # 줄의 앞뒤 공백을 제거하고 ': '를 기준으로 분리
    if len(data) == 2: #'영단어 : 한글 뜻'의 형태가 맞는지 검증!
        English = data[0].strip() #각 줄의 앞 순서인 영어 단어를 변수에 저장
        Korean = data[1].strip() #각 줄의 뒷 순서인 한글 단어를 변수에 저장
        vocab[English] = Korean #딕셔너리의 key 값과 result 값에 각 단어 집어넣기, dictionary 생성법!

keys = list(vocab.keys())#영어 단어를 불러와 리스트화, keys 변수에 집어넣기

while True : #랜덤이니까, 무한실행하도록 무한루프 넣기
        index = random.randint(0,len(keys)-1)#랜덤 인덱스 생성, keys 리스트 길이 -1까지를 최대값으로. 왜냐면 0부터 시작이니까.
        English = keys[index]#랜덤 위치의 영단어를 불러와 English 변수에 저장
        Korean = vocab[English]#key 값으로 dictionary의 한글 뜻 값 호출

        answer = input(f"{Korean} : ") #사용자에게 한국어 뜻에 해당하는 영어 단어 물어보기

        if answer.lower() == 'q' :#사용자가 'q'를 입력하면 프로그램 종료
                print("프로그램을 종료합니다.")
                break 

        if answer.lower() == English.lower(): #대소문자 구분 없이 채점하기 위해, 일괄 lower()로 소문자화
                print("맞았습니다!")
        else:
                print(f"아쉽습니다. 정답은 {English}입니다.")
with open('vocabulary.txt', 'r') as f: # 'vocabulary.txt' 파일을 읽기 모드로 열기
    lines = f.readlines() # 파일의 모든 줄을 읽어 리스트로 저장

for line in lines: # 파일에서 읽은 각 줄에 대해 반복
    data = line.split(": ") # 줄의 앞뒤 공백을 제거하고 ': '를 기준으로 분리
    if len(data) == 2: #'영단어 : 한글 뜻'의 형태가 맞는지 검증!
        English = data[0].strip() #각 줄의 앞 순서인 영어 단어를 변수에 저장
        Korean = data[1].strip() #각 줄의 뒷 순서인 한글 단어를 변수에 저장

        answer = input(f"{Korean} : ") #사용자에게 한국어 뜻에 해당하는 영어 단어 물어보기


        if answer.lower() == English.lower(): #대소문자 구분 없이 채점하기 위해, 일괄 lower()로 소문자화
                print("맞았습니다!")
        else:
                print(f"아쉽습니다. 정답은 {English}입니다.")
    else:
        print("단어장 형식에 문제가 있습니다, {line}줄을 체크해주세요.")
           
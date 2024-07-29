# 'vocabulary.txt' 파일을 쓰기 모드로 열기
with open('vocabulary.txt', 'w') as f:
    # 무한 루프 시작
    while True:
        # 사용자로부터 영어 단어 입력 받기
        English = input("영어 단어를 입력하세요: ")
        # 'q'를 입력하면 루프 종료
        if English == 'q':
            break
        
        # 사용자로부터 한국어 뜻 입력 받기
        Korean = input("한국어 뜻을 입력하세요: ")
        # 'q'를 입력하면 루프 종료
        if Korean == 'q':  # 여기에 '=' 대신 '==' 사용해야 함
            break 
        
        # 입력받은 단어와 뜻을 파일에 쓰기
        f.write(f'{English}: {Korean}\n')
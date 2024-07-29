import random #랜덤 상수 생성 라이브러리 import

answer = random.randint(1, 20) #랜덤으로 정답 설정, 1~20 사이
num_tries = 0 #초기 시도횟수 설정
max_tries = 4 #최대 시도횟수 설정

while num_tries < max_tries: #while문으로 시도횟수 4회까지만 기능하도록 코딩
    guess = int(input(f"기회가 {max_tries - num_tries}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: ")) #input을 받고, 문자열로 들어오므로 int를 씌워준 뒤 guess 변수로 저장
    num_tries += 1 #input을 받은 직후 시도횟수 증가시킴. 받자마자 증가시켜야 다음에 꼬이지 않음
    
    if guess > answer: #추측이 답보다 크면 down
        print("Down")
    elif guess < answer: #추측이 답보다 작으면 up
        print("Up")
    else: #크지도, 작지도 않으면 -> 답을 맞췄으면 축하 멘트 print, num_tries도 같이 프린트함
        print(f"축하합니다. {num_tries}번 만에 숫자를 맞히셨습니다.")
        break

if num_tries == max_tries and guess != answer: #시도횟수가 4와 같아졌는데 답을 맞히지 못하면 멘트 출력
    print(f"아쉽습니다. 정답은 {answer}입니다.")
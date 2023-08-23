import random

user_cnt = 0
max_cnt = 100


def start():
    print('게임을 시작합니다')
    random_number = random.randint(1, 100)
    cnt = 0

    while True:
        num = int(input('guess: '))
        if num > 100 or num <= 0:
            print('1~100 사이의 숫자를 입력해주세요!')
            continue

        if num > random_number:
            print('Down!')
            cnt += 1
            continue

        if num < random_number:
            print('Up!')
            cnt += 1
            continue

        else:
            cnt += 1
            print(f'정답입니다! 총 {cnt}회 시도하셨습니다.')

            global max_cnt
            global user_cnt
            user_cnt = cnt

            if user_cnt < max_cnt:
                max_cnt = user_cnt

            print(f'이전 최소 시도 횟수는 {max_cnt}회 입니다!')
            break
    end()


def end():
    print('게임을 재시작하시겠습니까? y/n')
    replay = input('replay?: ')
    if replay.lower() == 'y' or replay.lower() == 'yes':
        start()
    elif replay.lower() == 'n' or replay.lower() == 'no':
        print('게임을 종료합니다.')
    else:
        print('yes or no로 답해주시길 바랍니다.')
        end()


start()

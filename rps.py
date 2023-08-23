# 문자를 랜덤으로 뽑아내는 방법?
# (검색했는데 난수나 랜덤문자열이 아니라서 리스트를 사용하기로)
import random


def start():
    print('게임을 시작합니다')

    rps = ['Rock', 'Paper', 'Scissors']
    cnt = [0, 0, 0]
    stat = {}

    while True:
        p_rps = input('player: ')
        c_rps = (random.choice(rps))
        # print(c_rps) 넣어도 되고 안넣어도 되고

        if p_rps.capitalize() == c_rps:
            print('비겼습니다!')
            cnt[1] += 1
            print('게임을 그만두시려면 "quit"을 입력해주세요.')
            continue
        if p_rps.capitalize() == 'Rock':
            if c_rps == 'Paper':
                print('졌습니다.')
                cnt[2] += 1
                print('게임을 그만두시려면 "quit"을 입력해주세요.')
                continue
            if c_rps == 'Scissors':
                print('이겼습니다!')
                cnt[0] += 1
                print('게임을 그만두시려면 "quit"을 입력해주세요.')
                continue
        if p_rps.capitalize() == 'Paper':
            if c_rps == 'Scissors':
                print('졌습니다.')
                cnt[2] += 1
                print('게임을 그만두시려면 "quit"을 입력해주세요.')
                continue
            if c_rps == 'Rock':
                print('이겼습니다!')
                cnt[0] += 1
                print('게임을 그만두시려면 "quit"을 입력해주세요.')
                continue
        if p_rps.capitalize() == 'Scissors':
            if c_rps == 'Rock':
                print('졌습니다.')
                cnt[2] += 1
                print('게임을 그만두시려면 "quit"을 입력해주세요.')
                continue
            if c_rps == 'Paper':
                print('이겼습니다!')
                cnt[0] += 1
                print('게임을 그만두시려면 "quit"을 입력해주세요.')
                continue

        if p_rps.lower() == 'quit':
            print('게임을 종료합니다.')
            stat['승'] = cnt[0]
            stat['무'] = cnt[1]
            stat['패'] = cnt[2]
            stat['승률'] = cnt[0]/(cnt[0]+cnt[1]+cnt[2])*100
            # 승률에서 무승부를 제외하려면 cnt[1]을 없앨 것.
            print(stat)
            break


start()

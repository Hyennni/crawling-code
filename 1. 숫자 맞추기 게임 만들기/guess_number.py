import random

class RandomNumber:

    # init 안에 self.random_number를 초기 선언하고 그 변수를 다른 메소드에도 공유하면 값 공유가능함.
    def __init__(self):
        self.random_number = 0

    def get_random_number(self):

        self.random_number = random.randint(1, 100)
        return self.random_number

    def get_game_count(self):
        game_count = 1

        while True:
            my_number = int(input("1~100 사이의 숫자를 입력하세요:"))

            if my_number > self.random_number:
                print("다운")
            elif my_number < self.random_number:
                print("업")
            elif my_number == self.random_number:
                print(f"축하합니다.{game_count}회 만에 맞췄습니다")
                break

            game_count = game_count + 1

        return game_count

# return 왜 해야하는 지 모르겠음! 변수에 기억했다가 main에 쓰려고 return 줌

if __name__ == '__main__':
    r = RandomNumber()
    random_number = r.get_random_number()
    game_count = r.get_game_count()
    print(f'랜덤넘버 : {random_number}')
    print(f'맞추는데 걸린 횟수 : {game_count}')


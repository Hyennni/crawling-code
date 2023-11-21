import pyautogui
import time
import pyperclip

class Weather:
    def __init__(self):
        self.region =''

    def set_region(self,region):
        self.region = region

    def _(self):
        while True:
            print(pyautogui.position())
            time.sleep(0.1)

    def search_naver_weather(self):

        pyautogui.moveTo(1252, 182, 0.2)
        pyautogui.click()
        time.sleep(0.5)

        pyperclip.copy(f"{self.region} 날씨")
        pyautogui.hotkey("ctrl", "v")
        time.sleep(0.5)

        pyautogui.write(["enter"])
        time.sleep(1)

    def capture_naver_weather(self):

        start_x = 990
        start_y = 268
        end_x = 1647
        end_y = 940

        pyautogui.screenshot(f'./{self.region} 날씨.png', region=(start_x, start_y, end_x - start_x, end_y - start_y))

if __name__ == '__main__':
    w = Weather()

    while 1:
        menu = input('0-종료 1-지역 입력 2-네이버 날씨 검색 3-날씨 캡처')
        if menu =='0':
            print('프로그램 종료')
            break

        elif menu=='1':
            region = input('지역 이름 : ')
            w.set_region(region)

        elif menu=='2':
            w.search_naver_weather()

        elif menu=='3':
            w.capture_naver_weather()
            print('날씨 캡처 완료!')

        else:
            print('잘못된 번호입니다.')
            continue

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
# pip install selenium
from selenium.webdriver.common.keys import Keys
import time
import urllib.request


class GoogleImage:

    def __init__(self):
        self.search_word = ''

    def set_search_word(self, search_word):
        self.search = search_word

    def execute_search(self):
        pass


if __name__ == '__main__':

    g = GoogleImage()
    while 1:
        menu = input(f'''0. EXIT\n
              '1. 구글 이미지에 검색어 입력\n
              '2. 구글 이미지 조회하기\n''')
        if menu == '0':
            print('프로그램 종료')
            break
        elif menu == '1':
            s = input('검색어 입력: ')

        elif menu == '2':
            g.execute_search()

        else:
            print('다시 입력')
            continue
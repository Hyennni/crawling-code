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

#왜 안되는 지 확인해보기!

class GoogleImage:

    def __init__(self):
        self.search_word = ''
        self.url = 'https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl'

    def set_search_word(self, search_word):
        self.search_word = search_word

    def execute_search(self):
        search_word = self.search_word
        # print(f'{self.search_word}')
        driver = webdriver.Chrome()
        driver.get(self.url)
        elem = driver.find_element("name","q")
        # elem = driver.find_element('name','p') -> p를 q로 바꿈! " double quoter만 가능한가봐 이유는 모르겠음!

        elem.send_keys(search_word) #검색창에 단어 입력 후
        elem.send_keys(Keys.RETURN) #enter 키 입력해라

        SCROLL_PAUSE_TIME = 1
        last_height = driver.execute_script('return document.body.scrollHeight') #스크롤바 내리기
        while 1:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)
            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                try:
                    driver.find_element(By.CSS_SELECTOR, ".mye4qd").click()
                except:
                    break
            last_height = new_height

        images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
        count = 1
        for image in images:
            try:
                image.click()
                time.sleep(0.5)

                imgUrl = driver.find_element(
                    By.XPATH,
                    '//*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]'
                ).get_attribute("src")

                opener = urllib.request.build_opener()
                opener.addheaders = [
                    ('User-Agent',
                     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')
                ]
                urllib.request.install_opener(opener)
                urllib.request.urlretrieve(imgUrl, f'./image/{search_word}{str(count)}.jpg')
                count = count + 1
            except Exception as e:
                print('e : ', e)
                pass

        driver.close()


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
            g.set_search_word(s)

        elif menu == '2':
            g.execute_search()

        else:
            print('다시 입력')
            continue
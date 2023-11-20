import pandas as pd
from bs4 import BeautifulSoup
import requests

class MelonMusic:

    def __init__(self):
        self.domain= 'https://www.melon.com'
        # https://www.melon.com/chart/index.htm?dayTime=
        self.url = ''
        self.headers = {'User-Agent': 'Mozilla/5.0'}
        self.class_name = []
        self.title_ls = []
        self.artist_ls = []
        self.dict = {}
        self.df = None


    def set_url(self,url):
        self.url = requests.get(f'{self.domain}{url}', headers=self.headers).text

    def get_url(self):
        return self.url

    def print_list(self):
        soup = BeautifulSoup(self.url, 'lxml')
        print('------- 제목 --------')

        ls = soup.find_all(name="a", attrs={"class":'title'})

        for i in ls:
            self.title_ls.append(i.find("a").text)
            print(f'{self.title_ls[i]}')

        print('------ 가수 --------')
        ls = soup.find_all(name="a", attrs={"class":'title'})

        for i in ls:
            self.artist_ls.append(i.find("a").text)
            print(f'{self.artist_ls[i]}')


if __name__ == '__main__':
    m = MelonMusic()
    url = input('멜론에서 크롤링할 url를 입력하시오.')
    m.set_url(url)
    u2 = m.get_url()
    m.print_list()



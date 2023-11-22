import pandas as pd
import requests
from bs4 import BeautifulSoup

class NaverStock :

    def __init__(self):
        self.url = ''
        self.item_name = ''
        self.code = None
    #     pd.DataFrame({'name':[],'code':[]})

    def krx_crawl(self):
        c = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13', header=0)[0]
        # print(c)
        c['종목코드'] = c['종목코드'].map('{:06d}'.format) #005930이 5930으로 출력되는 것을 막는다 -> 6가지 자릿수 포맷에 맞춰서 가지고 와라
        k = c[['회사명','종목코드']] #여러개 넣을 거면 [[]] 이중 괄호
        print(k)
        self.code = k.rename(columns={'회사명': 'name', '종목코드': 'code'}) #회사명을 name으로 변경 , 종목코드를 Code로 변경
        # return self.code

    def get_url(self, item_name):
        c = self.code.query("name=='{}'".format(item_name))['code'].to_string(index=False)
        # 처음에 안된 이유 : c = self.code.query("name='{}'".format(item_name)['code'].to_string(index=False)) -> name 뒤에 '==' 와야하고 item_name 뒤에 ')'가 빠져서 안되었던 것!
        self.url = f'http://finance.naver.com/item/sise_day.naver?code={c}'
        self.item_name = item_name # 'code'로 대체
        print('요청 URL = {}'.format(self.url))


    def naver_crawl(self):
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = requests.get(self.url, headers=headers)
        html = BeautifulSoup(req.text,'lxml')
        pgrr = html.find('td',class_='pgRR')
        print(f" a태그 href 값 : {pgrr.a['href']}")
        s = pgrr.a['href'].split('=')
        print(f'{s}')
        last_page = s[-1]
        print(f'last page : {last_page}')
        temp_page = 10

        df = None

        for page in range(1,int(temp_page)+1):
            if (page<5):
                print(f'크롤링 중인 페이지 : {page}')
            req = requests.get(f'{self.url}&page={page}', headers=headers)
            df = pd.concat([df, pd.read_html(req.text, encoding='euc-kr')[0]])

        df.dropna(inplace=True)
        df.reset_index(drop=True,inplace=True)
        df.to_excel(f'./data/{self.item_name}.xlsx')


if __name__ == '__main__':
    n = NaverStock()

    while 1:
        menu = input('메뉴 입력하세요 : 0- 종료, 1- 종목코드, 2- url 등록, 3- 시세 조회 ')
        if menu == '0':
            print('프로그램 종료')
            break

        elif menu == '1':
            n.krx_crawl()

        elif menu == '2':
            item = input('회사명 입력 : ')
            a=n.get_url(item)


        elif menu == '3':
            n.naver_crawl()


        else :
            print('잘못된 번호입니다.')
            continue




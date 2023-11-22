import pandas as pd


class NaverStock :

    def __init__(self):
        self.code = None

    def krx_crawl(self):
        c = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13', header=0)[0]
        # print(c)
        c['종목코드'] = c['종목코드'].map('{:06d}'.format) #005930이 5930으로 출력되는 것을 막는다 -> 6가지 자릿수 포맷에 맞춰서 가지고 와라
        k = c[['회사명','종목코드']] #여러개 넣을 거면 [[]] 이중 괄호
        print(k)


    def get_url(self):
        pass

    def naver_crawl(self):
        pass


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
            pass


        elif menu == '3':
            pass


        else :
            print('잘못된 번호입니다.')
            continue




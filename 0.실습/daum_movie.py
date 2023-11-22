import requests
import requests as req
import json
import pandas as pd
from bs4 import BeautifulSoup as bs

class DaumMovie:

    def __init__(self):
        self.url = ''
        self.count = None
    #    숫자인지 문자인지 모를 때는 None으로 지칭. 숫자로 확신이 들면 0
    #    리뷰 수 : {'count': 287, 'sum': 1118, 'id': 149761585}
        self.review_count = 0
        self.review_list = []

    def set_url(self, url):
        self.url = url

    def set_count(self):
        # res = req.get(self.url)
        movie_code = '149761585'
        count_url = f"https://comment.daum.net/apis/v1/comments/on/{movie_code}/flags"
        count_res = req.get(count_url)
        self.count = json.loads(count_res.text)
        return self.count

    def extract_count(self):
        self.review_count = self.count['count']
        return self.review_count
#        딕셔너리의 값을 추출하기 위해서는 ['key'] 사용 -> 크롤링하면서 변화하기 때문에 값 고정 X
#  return 하지 않으면 그냥 None 값 조회됨

    def set_review_list(self):
         # for i in range(2): #self.review_count가 end로 지정되는 게 맞는데 DDOS 공격으로 오해 받을 수 있어서 2개만 진행
            # range(2)로 할 경우 2번 반복이 됨. 똑같은 애들로 -> self.count로 해도 그 평점 더보기를 눌러줘야지 더 많은 개수를 긁어올 수 있나봄.아 등록된 url이 다름!
        res = requests.get(self.url)
        ls = json.loads(res.text)
        print(f'목록 값 : {ls}')

        for i, _ in enumerate(ls):
             review = ls[i]['content'] #pretty json 사이트에서 키 값 추출
             user = ls[i]['user']['displayName']
             rating = ls[i]['rating']
             self.review_list.append([user, rating, review])

        df = pd.DataFrame(self.review_list,columns=['user','rating','review'])
        df.to_excel('./data/daum_review.xlsx')


if __name__ == '__main__':
    d = DaumMovie()
    # u = input('크롤링할 URL 입력하시기 바랍니다')

    while 1:
        menu = input('번호를 입력하세요. 0- 종료, 1- URL 등록, 2- 리뷰 수 조회, 3- 리뷰 목록 조회 ')

        if menu == '0':
            print('프로그램 종료')
            break

        elif menu == '1':
            # url = input('등록할 URL을 입력하세요 : ')
            url = 'https://comment.daum.net/apis/v1/posts/149761585/comments?parentId=0&offset=0&limit=10&sort=LATEST&isInitial=true&hasNext=true'
            d.set_url(url)
            print(f'{url} 등록했습니다.')

        elif menu == '2':
            d.set_count()
            count = d.extract_count()
            print(f'리뷰 수 : {count}')


        elif menu == '3':
            d.set_review_list()


        else:
            print('잘못된 번호입니다.')
            continue


    

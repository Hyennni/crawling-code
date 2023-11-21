import googletrans
from os import linesep
# pip install googletrans==4.0.0-rc1

# input은 main 화면에 노출 시켜야함. -> 함수 안에 쓰게 되면 encapsule화 되어서 잘 찾지 못하나봄!
class Translator:

    def __init__(self):
        self.text = ''
        self.translator = googletrans.Translator()

    def set_text(self,text):
        self.text = text

    def en_to_kor(self):
        result = self.translator.translate(self.text, dest='ko', src='en')
        return result
        # print(f"{self.text} => {result.text}")

    def kor_to_en(self):
        result = self.translator.translate(self.text, dest='en', src='auto')
        return result
        # print(f"{self.text} => {result.text}")

    def en_doc_kor(self):
        read_file_path = r"./영어파일.txt"
        write_file_path = r"./한글파일2.txt"

        with open(read_file_path, 'r') as f:
            readLines = f.readlines()

        for lines in readLines:
            result = self.translator.translate(lines, dest='ko')
            # return result -> 첫번째 라인의 결과값만 받아옴!
            print(result.text)
            with open(write_file_path, 'a', encoding='UTF8') as f:
                f.write(result.text + '\n')


if __name__ == '__main__':
    t = Translator()

    while 1:
        menu = input('메뉴 입력하세요 : 0- 종료, 1-영어->한글. 2-한글->영어 3-저장된 파일 번역 ')

        if menu =='0':
            print('프로그램 종료!')
            break

        elif menu=='1':
            str = input('영어를 입력하세요 : ')
            t.set_text(str)
            print(t.en_to_kor().text)

        elif menu=='2':
            str = input('한글을 입력하세요 : ')
            t.set_text(str)
            print(t.kor_to_en().text)

        elif menu == '3':
            t.en_doc_kor()
            # print(t.en_doc_kor().text)


        else:
            print('잘못된 번호입니다.')
            continue






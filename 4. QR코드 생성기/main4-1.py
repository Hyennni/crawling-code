import qrcode

class QrMaker:
    def __init__(self):
        self.qr_data = ''

    def set_qr(self):
        qr_data = input('생성할 QR URL을 입력하시오.')
        self.qr_data = qr_data

    def save_qr(self,title):
        qr_img = qrcode.make(self.qr_data)
        save_path = f'./{title}.png'
        qr_img.save(save_path)

    def save_multi_qr(self,fname):
        # file_path = r'4. QR코드 생성기\qr코드모음.txt'
        with open(fname, 'rt', encoding='UTF8') as f:
            read_lines = f.readlines()

            for line in read_lines:
                line = line.strip()
                print(line)

                qr_data = line
                qr_img = qrcode.make(qr_data)

                save_path = f'./qrcode/' + qr_data + '.png'
                qr_img.save(save_path)

# qr_data = 'www.naver.com'

if __name__ == '__main__':
    q = QrMaker()

    while 1 :
        menu = input('0:종료 1:QR 1개 생성 2:QR 여러개 생성')

        if menu=='0':
            print('프로그램 종료!')
            break

        elif menu=='1':
            q.set_qr()
            title = input('제목 입력 :')
            q.save_qr(title)

        elif menu=='2':
            fname = input('파일명 입력 :')
            q.save_multi_qr(fname)
            # qr코드모음.txt

        else:
            print('메뉴에 없는 번호입니다.')
            continue

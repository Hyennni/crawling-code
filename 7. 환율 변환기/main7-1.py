from currency_converter import CurrencyConverter
# pip install CurrencyConverter -> terminal에 입력!

class Exchange:

    def __init__(self):
        pass

    def get_all_currencies(self):
        cc = CurrencyConverter()
        return cc.currencies

    def change_usd_to_krw(self):
        cc = CurrencyConverter('http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip')
        return cc.convert(1, 'USD', 'KRW')

if __name__ == '__main__':
   e= Exchange()

   while 1:
        menu = input('메뉴 입력하세요 : 0. 종료, 1. 전체 화폐 단위 2.달러 환율 ')

        if menu == '0':
            print('종료!')
            break

        elif menu=='1':
            c = e.get_all_currencies()
            print(f'전체 화폐 : {c}')

        elif menu=='2':
            c = e.change_usd_to_krw()
            print(f'달러 환율 : {c}')

        else:
            print('메뉴에 없는 번호입니다.')
            continue

import pandas as pd

class Certificate:

    def __init__(self):
        self.student_list = []

    #     낱개로 담는 것보다 list로 종합해서 받는 게 나음 -> list는 복수형

    def set_student_list(self, student):
        self.student_list.append(student)

    def save_to_excel(self,fname):
        d = pd.DataFrame(self.student_list)

        df2 = pd.DataFrame([["홍길동", "1990.01.02", "2021-0001"],
                           ["김민준", "1990.05.06", "2021-0002"],
                           ["김철수", "2000.08.08", "2021-0003"],
                           ["김영희", "2000.09.09", "2021-0004"],
                           ["이서준", "2010.10.10", "2021-0005"],
                           ["장다인", "2017.12.12", "2021-0006"]])


        d.to_excel(f'./certificate/{fname}.xlsx', index=False, header=False)

if __name__ == '__main__':

    c = Certificate()

    while 1:
        menu = input('0- 종료 1- 학생 정보 입력 2- 엑셀 저장 ')

        if menu =='0':
            print('프로그램 종료!')
            break

        elif menu=='1':
            n = int(input('수료 인원 수 : '))
            for i in range(n):
                stu = []
                name = input('이름 : ')
                birth = input('생년월일 : ')
                c_number = input('수료증번호 : ')
                stu.append(name)
                stu.append(birth)
                stu.append(c_number)
                c.set_student_list(stu)

        elif menu=='2':
            name = input('파일명 입력 :')
            c.save_to_excel(name)

        else:
            print('잘못된 번호입니다.')
            continue




from gtts import gTTS
# from playsound import playsound

class TextToSpeech:

    def __init__(self):
        self.text = ''

    def set_text(self):
        text = input('어떤 글을 음성 변환할 지 입력 바랍니다.')
        self.text = text

    def save_mp3(self, title):
        tts = gTTS(text=self.text, lang='ko')
        tts.save(f"./{title}.mp3")
        # tts.save(r"./text.mp3") -> 고정된 이름으로 파일 저장
        print(f'{self.text}를 {title} 제목으로 음성 변환 완료')

if __name__ == '__main__':
    t = TextToSpeech()
    t.set_text()
    title = input('제목을 입력하시오!')
    t.save_mp3(title)

    # playsound(f"./{title}.mp3")

# text = "안녕하세요. 파이썬과 40개의 작품들 입니다."

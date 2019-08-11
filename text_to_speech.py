from gtts import gTTS
myt = input()
language = 'en'
hm = gTTS(text=myt, lang=language, slow=False)
hm.save("C:/Users/Hp/PycharmProjects/my_first/Am.mp3")
import os
os.startfile("C:/Users/Hp/PycharmProjects/my_first/Am.mp3")

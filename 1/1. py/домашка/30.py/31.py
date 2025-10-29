# Задача 1: Загадка про чарівні яблука
# У саду росте 5 чарівних яблунь. На першій яблуні росте 1 яблуко. На кожній наступній яблуні кількість яблук збільшується вдвічі. Вам потрібно порахувати загальну кількість яблук на всіх яблунях.
# totalapples=0
# apels=1
# for i in range(5):
#     totalapples+=apels
#     apels*=2
#     print("кількість яблук")
#     totalapples
# import  asspeech_recognition sr
# import pyttsx3
# import datetime
# import webbrowser
# import os

# # Ініціалізація синтезатора мови
# engine = pyttsx3.init()
# engine.setProperty('rate', 170)  # швидкість голосу
# engine.setProperty('volume', 1)  # гучність

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# def listen():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Слухаю тебе...")
#         audio = r.listen(source)
#         try:
#             command = r.recognize_google(audio, language="uk-UA")
#             print("Ти сказав:", command)
#             return command.lower()
#         except sr.UnknownValueError:
#             speak("Я не розчув. Повтори, будь ласка.")
#             return ""
#         except sr.RequestError:
#             speak("Проблема з інтернетом.")
#             return ""

# def execute_command(command):
#     if "час" in command:
#         now = datetime.datetime.now().strftime("%H:%M")
#         speak(f"Зараз {now}")
#     elif "ютуб" in command:
#         speak("Відкриваю YouTube")
#         webbrowser.open("https://www.youtube.com")
#     elif "браузер" in command or "гугл" in command:
#         speak("Відкриваю Google")
#         webbrowser.open("https://www.google.com")
#     elif "папку" in command:
#         speak("Відкриваю папку завантаження")
#         os.startfile("C:\\Users\\%USERNAME%\\Downloads")
#     elif "стоп" in command or "вихід" in command:
#         speak("До зустрічі!")
#         exit()
#     else:
#         speak("Не зрозумів команду, повтори ще раз.")

# def main():
#     speak("Привіт! Я твій голосовий помічник.")
#     while True:
#         command = listen()
#         if command:
#             execute_command(command)

# if __name__ == "__main__":
#     main()
# 2. Загадка про стрибки жабенят 🐸
# На річці є 20 латаття, розташованих в ряд. Жабеня починає стрибати з першого латаття. Воно може стрибати на 1 або 2 латаття вперед. Порахуйте, скільки різних способів є у жабеняти, щоб дістатися до 20-го латаття.

# for змінна in range(): 
#     блок коду

# for змінна in range(start,stop,крок):  
#     блок коду

# for змінна in range(0,31,3): # фор жадний і останню циферку з'їдає в stop 
#     print(змінна)
# Задача 1: Загадка про чарівні яблука
# У саду росте 5 чарівних яблунь. На першій яблуні росте 1 яблуко. 
# На кожній наступній яблуні кількість яблук збільшується вдвічі. 
# Вам потрібно порахувати загальну кількість яблук на всіх яблунях.
# чарівні_яблуні = 5
# яблуко = 1
# кошик = 0
# for i in range(чарівні_яблуні):
#     print(яблуко)
#     кошик+=яблуко
#     яблуко*=2
# print(кошик)

# Задача 2: Подорож крізь ґрати
# Ви йдете по стежці, на якій є 10 ґраток. На кожній ґратці лежить монетка. 
# Ви збираєте всі монетки з ґраток, номер яких ділиться на 2 і на 3 одночасно.
#  Скільки монеток ви зберете?
# монетки = 0
# for i in range(1,10):
#     if i%2==0 and i%3==0:
#         монетки+=1
# print(монетки)
# for i in range(5):
#     if i == 3:
#         continue
#     print(i)
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# Ініціалізація синтезатора мови
engine = pyttsx3.init()
engine.setProperty('rate', 170)  # швидкість голосу
engine.setProperty('volume', 1)  # гучність

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Слухаю тебе...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio, language="uk-UA")
            print("Ти сказав:", command)
            return command.lower()
        except sr.UnknownValueError:
            speak("Я не розчув. Повтори, будь ласка.")
            return ""
        except sr.RequestError:
            speak("Проблема з інтернетом.")
            return ""

def execute_command(command):
    if "час" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"Зараз {now}")
    elif "ютуб" in command:
        speak("Відкриваю YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "браузер" in command or "гугл" in command:
        speak("Відкриваю Google")
        webbrowser.open("https://www.google.com")
    elif "папку" in command:
        speak("Відкриваю папку завантаження")
        os.startfile("C:\\Users\\%USERNAME%\\Downloads")
    elif "стоп" in command or "вихід" in command:
        speak("До зустрічі!")
        exit()
    else:
        speak("Не зрозумів команду, повтори ще раз.")

def main():
    speak("Привіт! Я твій голосовий помічник.")
    while True:
        command = listen()
        if command:
            execute_command(command)

if __name__ == "__main__":
    main()
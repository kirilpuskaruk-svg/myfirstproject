# 6. Обчислити суму всіх чисел від 1 до 100:сума
# сума=0
# for i in range(1,101):
#     сума+=i
#     print(сума)   
7.
# import pyautogui
# import time
# screenWidth,screenHeight = pyautogui.size() # отримує розміри нашого екрану 
# pyautogui.click()
# pyautogui.moveTo(100,200,duration=1)
# pyautogui.click()
# pyautogui.rightClick()
# pyautogui.moveTo(100,750,duration=1)
# pyautogui.doubleClick()
# pyautogui.moveTo(screenWidth/2,screenHeight/2,duration=1)
# pyautogui.doubleClick()
# print("Я клікнув в точці 100,200 ")
# import pyautogui
# import time
# time.sleep(3)
# distance = 200
# pyautogui.mouseDown() # Затиснути клавішу мишки
# pyautogui.moveRel(distance,0,duration=0.5) # рухає мишку відносно місця де ми її залишили
# pyautogui.moveRel(0,distance,duration=0.5)
# pyautogui.moveRel(-distance,0,duration=0.5)
# pyautogui.moveRel(0,-distance,duration=0.5)
# pyautogui.mouseUp()

# import pyautogui
# import time
# time.sleep(2)
# pyautogui.write("""Pryvit,svit Ya robot 3000 terminator
# Pryvit,svit Ya robot 3000 terminator
# """,interval=0.01)
# # Pryvit,svit Ya robot 3000 terminatorPryvit,svit Ya robot 3000 terminator
# Pryvit,svit Ya robot 3000 terminator
# Відкриває Paint.
# Малює щось просте (наприклад, смайлик або будиночок).
# Робить скріншот свого малюнка.
# Показує повідомлення про завершення.
# import tkinter as tk
# from tkinter import messagebox
# import threading
# import time
# import sys
# import os
# import platform
# import subprocess

# SCREAM_WAV = "scream.wav"  
# SCREAM_DURATION = 5        
# FLASH_INTERVAL = 0.15      

# def shutil_which(name):
#     """Простейшая реализация which без импорта shutil."""
#     paths = os.environ.get("PATH", "").split(os.pathsep)
#     exts = [''] if platform.system() != "Windows" else os.environ.get("PATHEXT", "").split(os.pathsep)
#     for p in paths:
#         full = os.path.join(p, name)
#         for e in exts:
#             candidate = full + e
#             if os.path.isfile(candidate) and os.access(candidate, os.X_OK):
#                 return candidate
#     return None

# def play_sound_fallback(root):
#     """Попытаться воспроизвести WAV стандартными средствами, иначе bell fallback."""
#     system = platform.system()
#     if system == "Windows":
#         try:
#             import winsound
#             winsound.PlaySound(SCREAM_WAV, winsound.SND_FILENAME | winsound.SND_ASYNC)
#             return
#         except Exception:
#             pass

#     for exe in ("afplay", "aplay"):
#         if shutil_which(exe):
#             try:
#                 subprocess.Popen([exe, SCREAM_WAV])
#                 return
#             except Exception:
#                 pass

#     try:
#         for _ in range(20):
#             root.bell()
#             time.sleep(0.06)
#     except Exception:
#         pass

# def show_fullscreen_screamer(root):
#     top = tk.Toplevel(root)
#     top.withdraw()
#     top.attributes("-topmost", True)

#     try:
#         top.attributes("-fullscreen", True)
#     except Exception:
#         try:
#             top.state("zoomed")
#         except:
#             pass
#     top.configure(bg="black")

#     text_var = tk.StringVar(value="ТИ ВЗЛОМАН — ОЧЕНЬ СТРАШНО")
#     lbl = tk.Label(top, textvariable=text_var, font=("Segoe UI", 72, "bold"), fg="red", bg="black", wraplength=top.winfo_screenwidth())
#     lbl.pack(expand=True)

#     stop_flag = {"stop": False}
#     def flasher():
#         visible = True
#         while not stop_flag["stop"]:
#             lbl.config(fg="red" if visible else "black")
#             visible = not visible
#             time.sleep(FLASH_INTERVAL)
#     t = threading.Thread(target=flasher, daemon=True)
#     t.start()

#     threading.Thread(target=lambda: play_sound_fallback(top), daemon=True).start()

#     top.deiconify()

#     def auto_close():
#         time.sleep(SCREAM_DURATION)
#         stop_flag["stop"] = True
#         try:
#             top.destroy()
#         except:
#             pass
#     threading.Thread(target=auto_close, daemon=True).start()

# def fake_loading_then_prompt(root, label, btn):
#     label.config(text="Внимание! Обнаружена подозрительная активность...")
#     root.update()
#     for i in range(24):
#         dots = "." * (i % 6)
#         label.config(text="Проверка системы" + dots)
#         root.update()
#         time.sleep(0.12)
#     label.config(text="Нажмите '1' или кнопку '1' чтобы подтвердить")
#     btn.config(state="normal")

# def on_press(root, btn):
#     btn.config(state="disabled")
#     def run():
#         time.sleep(0.6)
#         show_fullscreen_screamer(root)
#     threading.Thread(target=run, daemon=True).start()

# def on_key(event, root, btn):
#     if event.char == '1':
#         on_press(root, btn)

# if __name__ == "__main__":

#     root = tk.Tk()
#     root.title("Важное сообщение")
#     root.geometry("480x200")
#     root.resizable(False, False)

#     label = tk.Label(root, text="Подготовка...", font=("Segoe UI", 12))
#     label.pack(pady=(20,10))

#     btn = tk.Button(root, text="1", font=("Segoe UI", 20, "bold"), width=6, state="disabled", command=lambda: on_press(root, btn))
#     btn.pack(pady=(4,10))

#     note = tk.Label(root, text="(версия без изображения — только громкий звук и текст).", font=("Segoe UI", 9))
#     note.pack(side="bottom", pady=8)

#     root.bind("<Key>", lambda e: on_key(e, root, btn))

#     threading.Thread(target=lambda: fake_loading_then_prompt(root, label, btn), daemon=True).start()

#     root.mainloop()
# Відкриває Paint.
# Малює щось просте (наприклад, смайлик або будиночок).
# Робить скріншот свого малюнка.
# Показує повідомлення про завершення.
# time.sleep(10)
# import pyautogui
# import time
# pyautogui.alert('Prygotuysya! Cherez 5 sekund ya pochnu malyuvaty v Paint!')
# time.sleep(5)
# pyautogui.moveTo(600, 400, duration=1) 

# pyautogui.dragRel(100, 0, duration=0.5, button='left')
# pyautogui.dragRel(0, 100, duration=0.5, button='left')
# pyautogui.dragRel(-100, 0, duration=0.5, button='left')
# pyautogui.dragRel(0, -100, duration=0.5, button='left')

# pyautogui.click(570, 380)
# pyautogui.click(630, 380)

# pyautogui.moveTo(570, 430)
# pyautogui.dragTo(630, 430, duration=0.5)

# pyautogui.screenshot('my_masterpiece.png')

# pyautogui.alert('Vualya! Tviy avtomatychnyi khudozhnyk zakinchyv robotu. Shukai kartynku v papci z proektom!')
import pyautogui
import time

time.sleep(3)

pyautogui.hotkey('win', 'r')  
time.sleep(1)
pyautogui.typewrite('mspaint')  
pyautogui.press('enter') 
time.sleep(2)  

pyautogui.moveTo(300, 300)
pyautogui.click()

pyautogui.dragRel(100, 0, duration=0.5)  
pyautogui.dragRel(0, 100, duration=0.5)  
pyautogui.dragRel(-100, 0, duration=0.5) 
pyautogui.dragRel(0, -100, duration=0.5)

pyautogui.moveTo(350, 350)
pyautogui.click()
pyautogui.dragRel(10, 0, duration=0.2)
pyautogui.moveTo(450, 350)
pyautogui.click()
pyautogui.dragRel(-10, 0, duration=0.2)

pyautogui.moveTo(350, 400)
pyautogui.dragRel(100, 50, duration=0.5)  
pyautogui.dragRel(-200, 0, duration=0.5)  

time.sleep(2)

screenshot = pyautogui.screenshot()
screenshot.save("screenshot.png")

print("Малюнок завершено! Скриншот збережено як 'screenshot.png'.")
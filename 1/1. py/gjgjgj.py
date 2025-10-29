# # while True:
# # 	move(West)
# # 	plant(Entities.Bush)
# # 	if can_harvest():
# # 		harvest()
# # 	move(North)
# East   =  вправо
# West   =  влево
# North  =  вверх
# South  =  вниз
import pyautogui
import threading
import tkinter as tk
import keyboard

class Autoclicker:
    def __init__(self, interval):
        self.interval = interval
        self.running = False

    def start_clicking(self):
        self.running = True
        threading.Thread(target=self.click_thread).start()

    def stop_clicking(self):
        self.running = False

    def click_thread(self):
        while self.running:
            pyautogui.click()
            pyautogui.PAUSE = self.interval

def create_gui(autoclicker):
    def start_clicking():
        interval = float(interval_entry.get())
        autoclicker.interval = interval
        autoclicker.start_clicking()

    def stop_clicking():
        autoclicker.stop_clicking()

    def set_start_bind():
        bind_key = bind_start_entry.get()
        keyboard.add_hotkey(bind_key, autoclicker.start_clicking)

    def set_stop_bind():
        bind_key = bind_stop_entry.get()
        keyboard.add_hotkey(bind_key, autoclicker.stop_clicking)

    root = tk.Tk()
    root.title("Autoclicker")

    interval_label = tk.Label(root, text="Интервал клика (сек):")
    interval_label.pack()

    interval_entry = tk.Entry(root)
    interval_entry.pack()

    bind_start_label = tk.Label(root, text="Бинд для старта:")
    bind_start_label.pack()

    bind_start_entry = tk.Entry(root)
    bind_start_entry.pack()

    bind_start_button = tk.Button(root, text="Установить (start)", command=set_start_bind)
    bind_start_button.pack()

    bind_stop_label = tk.Label(root, text="Бинд для стопа:")
    bind_stop_label.pack()

    bind_stop_entry = tk.Entry(root)
    bind_stop_entry.pack()

    bind_stop_button = tk.Button(root, text="Установить (stop)", command=set_stop_bind)
    bind_stop_button.pack()

    root.mainloop()

autoclicker = Autoclicker(interval=0.1)
create_gui(autoclicker)
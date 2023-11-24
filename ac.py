from win10toast import ToastNotifier
import time
import keyboard as kb
import pyautogui as gui

clickCooldown = 0.1 # Click speed
delay = 3 # Delay before start
toast = ToastNotifier()

time.sleep(delay)

print('- ON')
toast.show_toast(
    'AutoClicker',
    'Autoclicker is now on!',
    duration = 2 
)
print('Programa iniciado!')

while(True):
    gui.click()
    time.sleep(clickCooldown)
    if kb.is_pressed('F8'):
        print('- OFF')
        toast.show_toast(
            'AutoClicker',
            'Autoclicker off!',
            duration = 2
            )
        break
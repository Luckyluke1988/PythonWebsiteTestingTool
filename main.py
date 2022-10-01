from time import sleep
import pyautogui

def print_hi():
    pyautogui.moveTo(500, 500)
    # pyautogui.press('ctl', 'f5')
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('f5')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('f5')

if __name__ == '__main__':
    time = 0
    duration = 900
    sleepTime = 8
    sleep(10)
    counter = 0
    while(time < duration):
        print_hi()
        counter = counter + 1
        print(counter)
        sleep(sleepTime)
        duration += sleepTime

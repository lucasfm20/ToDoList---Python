import pyautogui
import time

def geraEmail(task_list,email):
    
    pyautogui.press('win')
    time.sleep(1.0)
    pyautogui.typewrite('google')
    time.sleep(1.0)
    pyautogui.press('enter')
    time.sleep(1.5)
    pyautogui.click(x=672, y=400)
    time.sleep(1.0)
    pyautogui.keyDown('ctrl')
    pyautogui.press('n')
    time.sleep(0.5)
    pyautogui.keyUp('ctrl')
    time.sleep(1.0)
    pyautogui.write('gmail.com')
    pyautogui.press('enter')
    time.sleep(5.5)
    pyautogui.press(['shift', 'c'])
    time.sleep(4.0)
    pyautogui.write(email)
    time.sleep(1.0)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.write('Lista de tarefas pendentes')
    time.sleep(1.0)
    pyautogui.press('tab')  
    pyautogui.hotkey('ctrl', 'a')  
    time.sleep(0.5)  
    pyautogui.press('backspace')  
    time.sleep(0.5)  
    for task in task_list:
        pyautogui.write(task)
        pyautogui.press('enter')
        time.sleep(0.5)  
    pyautogui.keyDown('ctrl')
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.keyUp('ctrl')


# executável pyinstaller --onefile --noconsole main.py
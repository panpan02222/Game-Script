import pyautogui    
import random    
import time    
import keyboard    
  
pyautogui.FAILSAFE = True  # 启用 FAILSAFE  
  
window_names = ["MuMu模拟器12", "阴阳师-网易游戏"]    

def get_window_position_and_size(window_name):    
    window = pyautogui.getWindowsWithTitle(window_name)[0]    
    if window:    
        left, top, width, height = window.left, window.top, window.width, window.height   
        print(f'left: {left}')  
        print(f'top: {top}')  
        print(f'width: {width}')  
        print(f'height: {height}')  
        return left, top, width, height    
    else:    
        return None    

while True:    
    offset_x = random.randint(-50, 50)    
    offset_y = random.randint(-50, 50)    
    for name in window_names:    
        pos_size = get_window_position_and_size(name)  
        print('使用的窗口为: ', name)  
        if pos_size is not None:    
            left, top, width, height = pos_size    
            break  # 找到匹配的窗口后退出循环    
    else:    
        print("未找到匹配的窗口")    
        break  # 如果没有找到匹配的窗口，则退出循环    
        
    target_x = left + 900 + offset_x    
    target_y = top + 500 + offset_y    
        
    pyautogui.moveTo(target_x, target_y, duration=0.5)    
        
    pyautogui.click(button='left', clicks=1)    
        
    if keyboard.is_pressed('q'):  # 使用 keyboard.is_pressed() 来检测按键，而不是 time.sleep()。  
        break    
        
    time.sleep(random.uniform(0.7, 3)) # 随机休眠一段时间，但不超过3秒。你可以根据需要调整这个范围。
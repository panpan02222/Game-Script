import pyautogui  
import random  
import time  
from pynput import keyboard  
import tkinter as tk
from tkinter import messagebox

# 启用 FAILSAFE
pyautogui.FAILSAFE = True  

# 窗口名称
window_names = ["MuMu模拟器12", "阴阳师-网易游戏"]  

offset_x = random.randint(-30, 31)
offset_y = random.randint(-24, 21)

# 获取窗口位置和大小的函数
def get_window_position_and_size(window_name):  
    try:
        window = pyautogui.getWindowsWithTitle(window_name)[0]
        return window.left, window.top, window.width, window.height  
    except IndexError as error:
        root = tk.Tk()  
        root.withdraw()  # 隐藏主窗口  
        messagebox.showerror("错误", "请打开正确的游戏窗口!")  
        root.destroy()  # 销毁主窗口  
        return None  

# 创建一个键盘监听器
stop_listener = False
def on_press(key):
    global stop_listener
    if key == keyboard.Key.esc:
        stop_listener = True

listener = keyboard.Listener(on_press=on_press)
listener.start()

# 创建一个新的Tkinter窗口
root = tk.Tk()
root.title("请选择你的游戏窗口")
root.geometry("400x100")  # 设置窗口的初始大小

# 创建一个函数，当按钮被点击时调用
def on_button_click(window_name):
    global stop_listener
    root.destroy()  # 销毁Tkinter窗口
    while True:   
        # 偏移量
        offset_x = random.randint(-30, 31)
        offset_y = random.randint(-24, 21) 
        if stop_listener:  
            break  
            
        pos_size = get_window_position_and_size(window_name)    
        if pos_size is not None:    
            left, top, width, height = pos_size    
            print(f'窗口位置和大小: {pos_size}')  # 打印窗口的位置和大小  
        else:    
            break  # 如果没有找到匹配的窗口，则退出循环    
      
        # 计算目标x和y的值，这里我们使用窗口的宽度和高度作为参考。    
        target_x = left + int(width * 0.92) + offset_x  # 假设点击位置在窗口的右下角，你可以根据需要调整这个值。    
        target_y = top + int(height * 0.88) + offset_y  # 同上，你可以根据需要调整这个值。    
      
        print(f'目标位置: ({target_x}, {target_y})')  # 打印目标位置  
      
        # 移动鼠标到目标位置  
        pyautogui.moveTo(target_x, target_y, duration=0.5)  # 移动鼠标到目标位置  
      
        pyautogui.click(button='left', clicks=1)  # 模拟鼠标左键单击  
      
        sleep_time = random.uniform(0.7, 3)  # 随机休眠一段时间，但不超过3秒。你可以根据需要调整这个范围。  
        print(f'休眠时间: {sleep_time} 秒')  # 打印休眠时间  
        time.sleep(sleep_time)

# 在窗口中添加两个按钮，每个按钮对应一个窗口名称
for window_name in window_names:
    button = tk.Button(root, text=window_name, command=lambda window_name=window_name: on_button_click(window_name))
    button.pack()

# 显示Tkinter窗口
root.mainloop()

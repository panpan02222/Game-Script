import pyautogui
import time
import random
import keyboard

# 窗口名称
window_name = "MuMu模拟器12"

# 获取窗口位置和大小
window = pyautogui.getWindowsWithTitle(window_name)[0]
left, top, width, height = window.left, window.top, window.width, window.height
while True:
    # 计算目标位置的xy偏差
    offset_x = random.randint(-50, 50)
    offset_y = random.randint(-50, 50)

    # 计算目标位置
    target_x = left + 1470 + offset_x
    target_y = top + 815 + offset_y

    # 移动鼠标到目标位置
    pyautogui.moveTo(target_x, target_y, duration=0.5)

    # 点击左键
    pyautogui.click(button='left', clicks=1)

    # 检测是否按下 Q 键，如果是则退出循环
    if keyboard.is_pressed('q'):
        break

    # 随机休眠一段时间
    sleep_time = random.uniform(0.7, 3)
    time.sleep(sleep_time)

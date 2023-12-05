# 导入所需的库
import cv2
import pytesseract
import math
import time

# 定义一些常量
L = 140 # 体力上限
R = 5 # 体力恢复速度（单位为分钟）
G = 30 # 青苹果效果

# 定义一个函数，用于从截图中获取体力值
def get_stamina_value(image_path):
    # 读取图片
    image = cv2.imread(image_path)
    # 转换为灰度图
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 二值化处理
    thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)[1]
    # 定义体力值的区域
    x, y, w, h = 100, 50, 100, 50 # 这些值可能需要根据你的截图进行调整
    # 裁剪出体力值的区域
    roi = thresh[y:y+h, x:x+w]
    # 使用pytesseract识别数字
    text = pytesseract.image_to_string(roi, config='--psm 7 -c tessedit_char_whitelist=0123456789/')
    # 返回体力值，格式为当前值/上限值
    return text

# 定义一个函数，用于计算当前体力值和青苹果储存
def calculate_stamina_and_apple(stamina, start_time, apple):
    # 获取当前时间
    current_time = time.time()
    # 计算经过的时间（单位为分钟）
    elapsed_time = (current_time - start_time) / 60
    # 计算最优的青苹果使用数量
    optimal_apple = math.floor((L - stamina - elapsed_time / R) / G)
    # 如果最优的青苹果使用数量小于0，说明不需要使用青苹果
    if optimal_apple < 0:
        optimal_apple = 0
    # 计算当前体力值
    current_stamina = stamina + elapsed_time / R + G * optimal_apple
    # 如果当前体力值超过了体力上限，需要减去多余的部分，并换算成青苹果储存
    if current_stamina > L:
        excess_stamina = current_stamina - L
        current_stamina = L
        apple += excess_stamina / G
    # 返回当前体力值和青苹果储存
    return current_stamina, apple

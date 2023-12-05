# 导入所需的库
import math
import time

# 定义一些常量
L = 140 # 体力上限
R = 5 # 体力恢复速度（单位为分钟）
G = 30 # 青苹果效果

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

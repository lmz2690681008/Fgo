# 导入所需的库
import cv2
import pytesseract

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

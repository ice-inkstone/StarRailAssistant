import random
import math
from pynput import mouse
from pynput.mouse import Controller
import pyautogui
import time


def get_random_point(x, y, width, height, blur):
    """
    说明：
        获取矩形内随机点位
    参数：
        :param x: 矩形中心点x坐标
        :param y: 矩形中心点y坐标
        :param width: 矩形宽度
        :param height: 矩形高度
        :param blur: 模糊化参数
    """
    # 计算中心区域的宽度和高度
    center_width = int(0.5 * width)
    center_height = int(0.5 * height)

    # 计算中心区域的左上角坐标
    center_x = x - int(0.5 * center_width)
    center_y = y - int(0.5 * center_height)

    # 计算中心区域的右下角坐标
    center_right = center_x + center_width
    center_bottom = center_y + center_height

    # 计算中心区域的面积
    center_area = center_width * center_height

    # 生成随机点位
    while True:
        # 生成随机点位的坐标
        point_x = random.randint(center_x, center_right)
        point_y = random.randint(center_y, center_bottom)

        # 计算点位到中心点的距离
        distance = math.sqrt((point_x - x) ** 2 + (point_y - y) ** 2)

        # 计算点位在中心区域内的概率
        probability = 1 - (distance / center_area) ** blur

        # 判断点位是否在中心区域内
        if point_x >= center_x and point_x <= center_right and point_y >= center_y and point_y <= center_bottom:
            # 判断点位是否在中心区域的0.5width、0.5height范围内
            if point_x >= x - int(0.25 * width) and point_x <= x + int(0.25 * width) and point_y >= y - int(0.25 * height) and point_y <= y + int(0.25 * height):
                # 返回点位
                return (point_x, point_y)
            else:
                # 根据概率决定是否返回点位
                if random.random() < probability:
                    return (point_x, point_y)


def click_like_human() -> None:
    pyautogui.mouseDown(button='left')
    time.sleep(random.uniform(0.2, 0.6))
    pyautogui.mouseUp(button='left')


def random_move_to(x, y):
    """
    说明：
        随机移动鼠标到指定位置
    参数：
        :param x: x坐标
        :param y: y坐标
    """
    # 随机选择一种移动方式
    moves = [pyautogui.easeInQuad, pyautogui.easeOutQuad, pyautogui.easeInOutQuad,
             pyautogui.easeInBounce, pyautogui.easeOutBounce, pyautogui.easeInOutBounce]
    move = random.choice(moves)

    # 随机移动鼠标到指定位置
    pyautogui.moveTo(x, y, duration=random.uniform(0.3, 1), tween=move)


def move_and_click_like_human(x, y):
    random_move_to(x, y)
    click_like_human()

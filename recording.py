import os.path

import cv2
import pyautogui
import datetime
import numpy as np


def screen_recorder(duration_seconds, output_path):
    # 获取屏幕分辨率
    screen_width, screen_height = pyautogui.size()

    # 设置视频编码器和参数
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = 30
    output_file = output_path + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + '.mp4'

    # 创建视频写入对象
    video_writer = cv2.VideoWriter(output_file, fourcc, fps, (screen_width, screen_height))

    # 计算结束时间
    end_time = datetime.datetime.now() + datetime.timedelta(seconds=duration_seconds)

    while datetime.datetime.now() < end_time:
        # 获取屏幕截图
        screenshot = pyautogui.screenshot()

        # 将截图转换为OpenCV图像格式
        frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        # 写入视频文件
        video_writer.write(frame)

    # 释放资源
    video_writer.release()

    print('录制完成')


# 示例调用
screen_recorder(duration_seconds=10, output_path=os.path.join("C:" , "tmp" , "bs" , "recordings"))

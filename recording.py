import cv2
import numpy as np
import pyautogui
import time
import os
import imageio

# 定义录制屏幕的区域（全屏）
screen_size = (1920, 1080)

# 定义输出视频的帧率和编码方式
fps = 30
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

# 创建输出视频的文件名和路径
output_folder = os.path.expanduser("~/Desktop")
output_filename = os.path.join(output_folder, "screencast.mp4")

# 获取要录屏的时间
start_time = time.time()
record_time = int(input("请输入录制时间（秒）："))

# 创建输出视频的写入器
out = cv2.VideoWriter(output_filename, fourcc, fps, screen_size)

# 不断循环，直到到达指定的录制时间
while (time.time() - start_time) < record_time:
    # 截取屏幕上的帧
    img = pyautogui.screenshot()

    # 转换为OpenCV格式的图像
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # 将图像写入输出视频
    out.write(frame)

    # 显示实时的录制信息
    print("Recording: %.2f seconds" % (time.time() - start_time))

# 释放视频写入器，并关闭所有打开的窗口
out.release()
cv2.destroyAllWindows()

# 使用imageio库将输出文件转换为mp4格式
mp4_output_filename = os.path.join(output_folder, "screencast_final.mp4")
with imageio.get_writer(mp4_output_filename, fps=fps) as writer:
    for frame in imageio.imread(output_filename):
        writer.append_data(frame)

# 删除临时的输出文件
os.remove(output_filename)

print("Recording complete. Video saved to:", mp4_output_filename)
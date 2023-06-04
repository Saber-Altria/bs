import cv2

# 打开摄像头，默认使用计算机的默认摄像头（编号为0）
cap = cv2.VideoCapture(0)

# 不断循环，直到用户按下 'q' 键退出
while True:
    # 读取一帧图像
    ret, frame = cap.read()

    # 如果成功读取到一帧图像，则将其显示在屏幕上
    if ret:
        cv2.imshow('frame', frame)

    # 等待最多25毫秒，如果用户按下 'q' 键则退出循环
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# 释放摄像头并关闭所有打开的窗口
cap.release()
cv2.destroyAllWindows()
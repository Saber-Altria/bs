import time
import tkinter
import threading
import ctypes
import psutil

root = tkinter.Tk()
root.title('防作弊演示')
# 窗口初始大小和位置
root.geometry('300x100+300+100')
# 不允许改变窗口大小
root.resizable(False, False)
ban = tkinter.IntVar(root, 0)


# 强行关闭主流文本编辑器和网页浏览器
def funcBan():
    while ban.get() == 1:
        for pid in psutil.pids():
            try:
                # 强行关闭主流文本编辑器和网页浏览器
                p = psutil.Process(pid)
                exeName = os.path.basename(p.exe()).lower()
                if exeName in ('notepad.exe', 'winword.exe', 'wps.exe', 'wordpad.exe', 'iexplore.exe',
                               'chrome.exe', 'qqbrowser.exe', '360chrome.exe', '360se.exe',
                               'sogouexplorer.exe', 'firefox.exe', 'opera.exe', 'maxthon.exe',
                               'netscape.exe', 'baidubrowser.exe', '2345Explorer.exe'):
                    p.kill()
                    buttonTip = tkinter.Button(root, text='提示：禁止打开违规软件')
                    buttonTip.place(x=20, y=40, width=200, height=30)
            except:
                pass
        # 清空系统剪切板
        ctypes.windll.user32.OpenClipboard(None)
        ctypes.windll.user32.EmptyClipboard()
        ctypes.windll.user32.CloseClipboard()
        time.sleep(1)


# 开启
def Anti_start():
    ban.set(1)
    t = threading.Thread(target=funcBan)
    t.start()


# 停止
def Anti_stop():
    ban.set(0)


# 测试
buttonStart = tkinter.Button(root, text='开始考试', command=Anti_start)
buttonStart.place(x=20, y=10, width=100, height=30)
buttonStop = tkinter.Button(root, text='结束考试', command=Anti_stop)
buttonStop.place(x=130, y=10, width=100, height=30)
# 模拟用，开启考试模式以后，所有内容都不再允许复制
entryMessage = tkinter.Entry(root)
entryMessage.place(x=10, y=40, width=230, height=30)
root.mainloop()

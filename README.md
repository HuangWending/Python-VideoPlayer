# Python-VideoPlayer
Python视频播放器

1. 导入所需的库：

import cv2
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import Scale
from tkinter import Button


2. 创建主窗口：

window = tk.Tk()
window.title("视频播放器")


3. 定义选择文件功能：

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("视频文件", "*.mp4;*.avi")])
    if file_path:
        play_video(file_path)

4. 定义播放视频功能：
5. 
def play_video(file_path):
    video = cv2.VideoCapture(file_path)
    
5. 创建视频播放框架和控制滑块：

video_frame = tk.Label(window)
video_frame.pack()

speed_label = tk.Label(window, text="速度")
speed_label.pack()
speed_scale = Scale(window, from_=0.1, to=2.0, resolution=0.1, orient=tk.HORIZONTAL)
speed_scale.pack()

volume_label = tk.Label(window, text="声音大小")
volume_label.pack()
volume_scale = Scale(window, from_=0, to=1.0, resolution=0.1, orient=tk.HORIZONTAL)
volume_scale.pack()

6. 创建暂停/播放按钮，并定义其功能：

def toggle_play():
    if play_button["text"] == "暂停":
        play_button["text"] = "播放"
        video.set(cv2.CAP_PROP_POS_FRAMES, 0)  # 重置视频到开头
    else:
        play_button["text"] = "暂停"

play_button = Button(window, text="播放", command=toggle_play)
play_button.pack()

7. 定义播放视频的函数，以及调整视频速度和音量：

def play():
    ret, frame = video.read()
    if ret:
        speed = speed_scale.get()
        video.set(cv2.CAP_PROP_POS_MSEC, video.get(cv2.CAP_PROP_POS_MSEC) * speed)

        volume = volume_scale.get()
        video.set(cv2.CAP_PROP_VOLUME, volume)

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = cv2.resize(frame, (width, height))
        image = tk.PhotoImage(image=tk.Image.fromarray(image))
        video_frame.configure(image=image)
        video_frame.image = image

        window.after(1, play)
    else:
        play_button["text"] = "播放"
        video.release()

8. 创建选择文件按钮：

select_button = Button(window, text="选择视频文件", command=select_file)
select_button.pack()

9. 运行窗口主循环：

window.mainloop()


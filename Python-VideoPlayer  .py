import cv2
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import Scale
from tkinter import Button

# 创建窗口
window = tk.Tk()
window.title("视频播放器")

# 选择视频文件
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("视频文件", "*.mp4;*.avi")])
    if file_path:
        play_video(file_path)

# 播放视频
def play_video(file_path):
    video = cv2.VideoCapture(file_path)
    
    # 获取视频的宽度和高度
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # 创建视频播放框架
    video_frame = tk.Label(window)
    video_frame.pack()
    
    # 创建速度控制滑块
    speed_label = tk.Label(window, text="速度")
    speed_label.pack()
    speed_scale = Scale(window, from_=0.1, to=2.0, resolution=0.1, orient=tk.HORIZONTAL)
    speed_scale.pack()
    
    # 创建声音大小控制滑块
    volume_label = tk.Label(window, text="声音大小")
    volume_label.pack()
    volume_scale = Scale(window, from_=0, to=1.0, resolution=0.1, orient=tk.HORIZONTAL)
    volume_scale.pack()
    
    # 创建暂停/播放按钮
    def toggle_play():
        if play_button["text"] == "暂停":
            play_button["text"] = "播放"
            video.set(cv2.CAP_PROP_POS_FRAMES, 0)  # 重置视频到开头
        else:
            play_button["text"] = "暂停"
    
    play_button = Button(window, text="播放", command=toggle_play)
    play_button.pack()
    
    # 播放视频
    def play():
        ret, frame = video.read()
        if ret:
            # 调整视频速度
            speed = speed_scale.get()
            video.set(cv2.CAP_PROP_POS_MSEC, video.get(cv2.CAP_PROP_POS_MSEC) * speed)
            
            # 调整音量
            volume = volume_scale.get()
            video.set(cv2.CAP_PROP_VOLUME, volume)
            
            # 将视频帧显示在框架中
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = cv2.resize(frame, (width, height))
            image = tk.PhotoImage(image=tk.Image.fromarray(image))
            video_frame.configure(image=image)
            video_frame.image = image
            
            # 循环播放
            window.after(1, play)
        else:
            play_button["text"] = "播放"
            video.release()
    
    play()

# 选择视频文件按钮
select_button = Button(window, text="选择视频文件", command=select_file)
select_button.pack()

# 运行窗口
window.mainloop()

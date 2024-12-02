import tkinter as tk
from tkinter import messagebox
import os
import webbrowser

# 定义打开index.html的函数
def open_web():
    web_path = os.path.join(os.getcwd(), "web", "index.html")
    if os.path.exists(web_path):
        webbrowser.open(f"file://{web_path}")
    else:
        messagebox.showerror("错误", "找不到 index.html 文件！")

# 定义运行game.py的函数
def run_game():
    game_path = os.path.join(os.getcwd(), "game.py")
    if os.path.exists(game_path):
        os.system(f"python \"{game_path}\"")
    else:
        messagebox.showerror("错误", "找不到 game.py 文件！")

# 创建主窗口
root = tk.Tk()
root.title("选择你的操作")
root.geometry("400x300")  # 调整窗口大小
root.configure(bg="#f5f5f5")  # 背景颜色

# 添加标题
title_label = tk.Label(root, text="欢迎开启探索犹太文明之旅", font=("Arial", 16, "bold"), bg="#f5f5f5", fg="#333")
title_label.pack(pady=20)

# 添加按钮样式
button_style = {
    "font": ("Arial", 14),
    "width": 15,
    "height": 2,
    "bg": "#4CAF50",
    "fg": "white",
    "activebackground": "#45a049",
    "activeforeground": "white",
    "relief": "raised",
    "bd": 3,
}

# 添加“我要学习！”按钮
btn_study = tk.Button(root, text="我要学习！", command=open_web, **button_style)
btn_study.pack(pady=10)

# 添加“我要挑战！”按钮
btn_challenge = tk.Button(root, text="我要挑战！", command=run_game, **button_style)
btn_challenge.pack(pady=10)

# 运行主窗口
root.mainloop()

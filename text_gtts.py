# gTTSテキスト読み上げツール
# 起動方法：
# >python text_gtts.py

# 2020/4/11 ver 1.0  1stリリース
# 
import tkinter as tk
from tkinter import ttk
from gtts import gTTS
from playsound import playsound
import threading
import os


out_file = 'out.mp3'


def output_talk(txt):
    """
        コマンド文字列の生成
        @param txt   発声テキスト
    """
    tts = gTTS(txt, lang='ja')
    tts.save(out_file)


def play_talk():
    """
        音声を鳴らす
    """
    playsound(out_file)


def b1_clicked():
    """
        再生ボタン押下イベント
    """
    global txt_str
    global thread
    txt_str = txt.get('1.0', tk.END)        # テキストボックス内容取得
    txt_str = txt_str.replace("\n", " ")    # 改行をスペースに
    btn_status_play()
    thread = threading.Thread(
                        target=playing)     # スレッドで音声発声する。
    thread.setDaemon(True)
    thread.start()


def playing():
    """
        音声を作成、再生
    """
    if os.path.exists(out_file):            # 出力ファイルが存在すれば削除しておく
        os.remove(out_file)
    output_talk(txt_str)
    play_talk()
    btn_status_stop()


def btn_status_play():
    """
        発声処理中のボタン状態に設定
    """
    global b1
    b1.config(state=tk.DISABLED)


def btn_status_stop():
    """
        発声処理でないボタン状態に設定
    """
    global b1
    b1.config(state=tk.NORMAL)


top = tk.Tk()
top.title('gTTSテキスト読み上げツール')
top.minsize(100, 100)
top.geometry('400x200')


# Frame
f = ttk.Frame(top, padding=5)
f.pack(expand=True, fill='both')


# Text
#txt = tk.Text(f, width=80, height=10)
txt = tk.Text(f, width=0, height=0)
txt.pack(expand=True, fill='both', side='left')


# Scrollbar
sc = ttk.Scrollbar(
        f,
        orient=tk.VERTICAL,
        command=txt.yview)
txt['yscrollcommand'] = sc.set
sc.pack(side='left', fill='y')


# Combobox
f2 = ttk.Frame(top, padding=5)
f2.pack(fill='x')


# Button
f3 = ttk.Frame(top, padding=0)
f3.pack()

b1 = ttk.Button(f3, text='再生', command=b1_clicked)
b1.pack(side='left')

btn_status_stop()

top.mainloop()

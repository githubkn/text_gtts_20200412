# gTTSテキスト読み上げツール
# 起動方法：
# >python text_gtts.py

# 2020/4/11 ver 1.0   1stリリース
# 2020/4/11 ver 1.01  言語選択機能追加
import tkinter as tk
from tkinter import ttk
from gtts import gTTS
from playsound import playsound
import threading
import os
import re

out_file = 'out.mp3'


def get_lang_str():
    global cb_str
    return re.split(":", cb_str.get())[0]                   # Comboboxの値から言語文字(:より前)を取得
    

def output_talk(txt):
    """
        コマンド文字列の生成
        @param txt   発声テキスト
    """
    tts = gTTS(txt, lang=get_lang_str())
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

cb_str = tk.StringVar()
cb = ttk.Combobox(f2, textvariable=cb_str)
cb.pack(fill='x')

langs = ['af: Afrikaans',
    'ar: Arabic',
    'bn: Bengali',
    'bs: Bosnian',
    'ca: Catalan',
    'cs: Czech',
    'cy: Welsh',
    'da: Danish',
    'de: German',
    'el: Greek',
    'en-au: English (Australia)',
    'en-ca: English (Canada)',
    'en-gb: English (UK)',
    'en-gh: English (Ghana)',
    'en-ie: English (Ireland)',
    'en-in: English (India)',
    'en-ng: English (Nigeria)',
    'en-nz: English (New Zealand)',
    'en-ph: English (Philippines)'
    'en-tz: English (Tanzania)',
    'en-uk: English (UK)',
    'en-us: English (US)',
    'en-za: English (South Africa)',
    'en: English',
    'eo: Esperanto',
    'es-es: Spanish (Spain)',
    'es-us: Spanish (United States)',
    'es: Spanish',
    'et: Estonian',
    'fi: Finnish',
    'fr-ca: French (Canada)',
    'fr-fr: French (France)',
    'fr: French',
    'gu: Gujarati',
    'hi: Hindi',
    'hr: Croatian',
    'hu: Hungarian',
    'hy: Armenian',
    'id: Indonesian',
    'is: Icelandic',
    'it: Italian',
    'ja: Japanese',
    'jw: Javanese',
    'km: Khmer',
    'kn: Kannada',
    'ko: Korean',
    'la: Latin',
    'lv: Latvian',
    'mk: Macedonian',
    'ml: Malayalam',
    'mr: Marathi',
    'my: Myanmar (Burmese)',
    'ne: Nepali',
    'nl: Dutch',
    'no: Norwegian',
    'pl: Polish',
    'pt-br: Portuguese (Brazil)',
    'pt-pt: Portuguese (Portugal)',
    'pt: Portuguese',
    'ro: Romanian',
    'ru: Russian',
    'si: Sinhala',
    'sk: Slovak',
    'sq: Albanian',
    'sr: Serbian',
    'su: Sundanese',
    'sv: Swedish',
    'sw: Swahili',
    'ta: Tamil',
    'te: Telugu',
    'th: Thai',
    'tl: Filipino',
    'tr: Turkish',
    'uk: Ukrainian',
    'ur: Urdu',
    'vi: Vietnamese',
    'zh-cn: Chinese (Mandarin/China)',
    'zh-tw: Chinese (Mandarin/Taiwan)']

cb['values'] = langs

cb.current(40)                               # 日本語を初期値にする。

# Button
f3 = ttk.Frame(top, padding=0)
f3.pack()

b1 = ttk.Button(f3, text='再生', command=b1_clicked)
b1.pack(side='left')

btn_status_stop()

top.mainloop()

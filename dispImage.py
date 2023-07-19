import tkinter as tk            #GUI作成のライブラリ
import random                   #乱数
import PIL.Image                #画像を扱うモジュール
import PIL.ImageTk              #tkinterで作った画面上に表示させるモジュール
import os                       #内部処理用

def dispPhoto(path):
    #画像サイズを調整して読み込む
    newImage=PIL.Image.open(path).resize([300,300])
    #画面表示用の画像データとして読み込む
    imageData=PIL.ImageTk.PhotoImage(newImage)
    # 画像ラベルとして設定
    imageLabel.configure(image=imageData)
    # 画像データを画像用ラベルに設定
    imageLabel.image=imageData

def omikuji():
    #画像のファイルの害列
    kujiFileName=["daikiti.png","tyukiti.png","syokiti.png","kyo.png"]
    #表示画像の添え字をランダムに設定
    filename=(random.choice(kujiFileName))
    #画像ファイルパスの設定
    fpath=os.path.dirname(__file__)+"/images/"+filename
    print("--------------------------------")
    print(os.path.dirname(__file__))
    #画像の読み込み＆表示
    dispPhoto(fpath)


if __name__ == '__main__':
    #画面の設定
    root=tk.Tk()
    root.geometry("400x350")
    #ボタンを作成
    btn=tk.Button(text="おみくじを引く",command=omikuji)
    #画面ラベルを作成
    imageLabel=tk.Label()
    #ボタンの位置
    btn.pack()
    #画像ラベルの配置
    imageLabel.pack()
    # 画面を表示する
    tk.mainloop()













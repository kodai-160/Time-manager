import tkinter as tk
from tkinter import filedialog
from PIL import Image

def resize_and_save_image():
    root = tk.Tk()
    root.withdraw()  # tkinterのメインウィンドウを非表示にする

    # 画像ファイルの選択
    file_path = filedialog.askopenfilename(
        title='Open PNG image',
        filetypes=[('PNG Files', '*.png')]
    )
    if not file_path:
        return

    img = Image.open(file_path)

    # 画面の解像度に合わせたサイズを計算
    # ここでは仮の値として1920x1080を使用していますが、実際にはシステムの解像度や特定の要件に応じて調整してください
    screen_width = 1920
    screen_height = 1080

    # `object-fit: cover`の効果を模倣
    # 元のアスペクト比を保持しながら、指定された「画面」サイズに最も近くなるようにリサイズ
    img_ratio = img.width / img.height
    screen_ratio = screen_width / screen_height
    if img_ratio > screen_ratio:
        # 画像の幅が相対的に大きい場合、高さを基準にリサイズ
        new_height = screen_height
        new_width = int(new_height * img_ratio)
    else:
        # 画像の高さが相対的に大きい場合、幅を基準にリサイズ
        new_width = screen_width
        new_height = int(new_width / img_ratio)

    img = img.resize((new_width, new_height), Image.LANCZOS)

    # 新しい画像を保存
    save_path = filedialog.asksaveasfilename(
        title='Save resized image',
        filetypes=[('PNG Files', '*.png')],
        defaultextension='.png'
    )
    if save_path:
        img.save(save_path)

if __name__ == '__main__':
    resize_and_save_image()

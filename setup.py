import re
import requests
from lxml import etree
from PIL import ImageFont, ImageDraw, Image
import tkinter as tk
import os
from tkinter import messagebox

def get_article_title(url, headers=None):
    try:
        with requests.Session() as session:
            # 使用请求头获取HTML页面内容
            html = session.get(url, headers=headers, verify=False)
            html.raise_for_status()

            # 使用xpath解析HTML页面，获取文章标题内容
            etree_html = etree.HTML(html.text)
            content = etree_html.xpath('//*[@id="activity-name"]/text()')

            # 处理文章标题内容，去除不必要的字符
            for each in content:
                replace = each.replace('\n', '').replace(' ', '')
                if replace != '\n' and replace != '':
                    # 输出文章标题
                    print("-----------------------------")
                    print('此文章的标题是：' + replace)
                    return replace  # 返回文章标题字符串
    except requests.exceptions.RequestException as e:
        # 发生异常时，抛出异常
        raise RuntimeError(f"连接失败，{str(e)}")


def download_image(url, filename, headers=None):
    try:
        with requests.Session() as session:
            res = session.get(url, headers=headers)
            res.raise_for_status()
    except requests.exceptions.RequestException as e:
        # 发生异常时，抛出异常
        raise RuntimeError(f"下载图片失败，{str(e)}")

    with open(filename, 'wb') as f:
        f.write(res.content)



def create_footer_image(title, image_filename):
    # 读取图片
    pil_image = Image.open(image_filename)
    # 把图片转换为900*383
    pil_image = pil_image.resize((900, 383))

    # width 为图片的宽, height为图片的高
    width, height = pil_image.size

    # 生成一张尺寸为 width * (height + 100) 背景色为白色的图
    bg = Image.new('RGB', (width, height + 100), color=(255, 255, 255))
    # 写入底图
    bg.paste(pil_image, (0, 0))
    # 写入的文字
    word = title

    # 导入一个字体文件 思明黑体
    font_file = './font/font.TTF'
    # 计算出要写入的文字占用的像素
    title_length = len(title)
    # 计算出要写入的文字占用的像素
    font_size = 28
    while True:
        font = ImageFont.truetype(font_file, font_size)
        w, h = font.getsize(word)
        if w < width:
            break
        font_size -= 1

    font = ImageFont.truetype(font_file, font_size)
    w, h = font.getsize(word)  #
    # 创建一个可以在给定图像上绘图的对象
    draw = ImageDraw.Draw(bg)
    draw.text(((width - w) / 2, (height + (100 / 2) - (h / 2))), word, fill=(0, 0, 0), font=font)
    # 剔除标点符号
    punctuation = '!,;:?"\'、，；|. '

    def remove_punctuation(text):
        text = re.sub(r'[{}]+'.format(punctuation), ' ', text)
        return text.strip()

    name = remove_punctuation(title)
    # 保存画布
    output_filename = os.path.join(os.getcwd(), '往期推荐完成_{}.png'.format(name))
    bg.save(output_filename, "PNG")
    print("-----------------------------")
    print("图片已制作完成，保存在exe文件目录")


def main():
    url = entry.get()
    if not url:
        messagebox.showerror("错误", "请输入文章链接！")
        return
    try:
        title = get_article_title(url)
        download_image(re.findall('msg_cdn_url = "(.*?)"', requests.get(url).text, re.I | re.S | re.M)[0], "temp.jpg")
        create_footer_image(title, "temp.jpg")
        messagebox.showinfo("提示", "微信尾部往期精选图已生成！")
    except Exception as e:
        messagebox.showerror("错误", str(e))



if __name__ == '__main__':
    root = tk.Tk()
    root.title("微信尾部往期精选图生成器")
    root.geometry("500x200")

    label_title = tk.Label(root, text="一键制作微信尾部往期精选图 Author: Chichi")
    label_title.pack()

    label_url = tk.Label(root, text="请输入文章链接：")
    label_url.pack()

    entry = tk.Entry(root)
    entry.pack()

    button_create = tk.Button(root, text="一键生成", command=main)
    button_create.pack()

    label = tk.Label(root)
    label.pack()

    button_exit = tk.Button(root, text="退出", command=root.quit)
    button_exit.pack()

    root.mainloop()

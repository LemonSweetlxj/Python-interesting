from PIL import Image
import argparse

##命令行输入参数处理
parser = argparse.ArgumentParser()
parser.add_argument('file') ##输入文件
parser.add_argument('-o','--output')  ##输出文件
##输入字符画宽度
parser.add_argument('--width',type = int, default = 80)
##输出字符画高度
parser.add_argument('--height',type = int, default = 80)

##获取参数
args = parser.parse_args()
IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

##灰度值小（暗）的用开头符号，vice verse
ascii_char = list ("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

##将256灰度映射到列表的70个字符上
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ''
    length = len(ascii_char)
    ##灰度转换公式
    grey = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1)/length
    return ascii_char[int(grey/unit)]


if __name__ == '__main__':
    im = Image.open(IMG)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)
    txt = ""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'
    print(txt)


    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)



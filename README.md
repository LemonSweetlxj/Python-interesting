# Python-interesting
实验楼

1.字符画：用 50 行 Python 代码完成图片转字符画小工具。

                      核心在于灰度值的理解：

      灰度值：指黑白图像中点的颜色深度，范围一般从0到255，白色为255，黑色为0，故黑白图片也称灰度图像

      像素RGB到灰度值转换的公式： gray ＝ 0.2126 * r + 0.7152 * g + 0.0722 * b
             
      遍历每个像素点，取到灰度值之后，然后进行字符替换

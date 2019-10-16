# coding=utf-8

from PIL import Image
import pytesser3

def getImage(file):
    image = Image.open(file)# coding=utf-8
    return image

# 灰度处理
def discolorizing(image):
    image = image.convert('L')
    return image
# 二值化
def binarizing(image, threshold=127):
    pixdata = image.load()
    width, height = image.size
    for y in range(height):
        for x in range(width):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    return image

# 降噪
def denoise(image):
    pixdata = image.load()
    width, height = image.size
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            count = 0
            if pixdata[x, y - 1] > 245:  # 上
                count = count + 1
            if pixdata[x, y + 1] > 245:  # 下
                count = count + 1
            if pixdata[x - 1, y] > 245:  # 左
                count = count + 1
            if pixdata[x + 1, y] > 245:  # 右
                count = count + 1
            if pixdata[x + 1, y + 1] > 245:  #
                count = count + 1
            if pixdata[x + 1, y - 1] > 245:  #
                count = count + 1
            if pixdata[x - 1, y + 1] > 245:  #
                count = count + 1
            if pixdata[x - 1, y - 1] > 245:  #
                count = count + 1
            if count > 5:
                pixdata[x, y] = 255
    return image

def detect(image):
    result = pytesser3.image_to_string(image)
    return result

if __name__ == '__main__':
    image = getImage('./image.jpg')
    image = discolorizing(image)
    image = binarizing(image)
    image = denoise(image)
    image = denoise(image)
    image = denoise(image)
    image.show()
    result = detect(image)
    print result
    image.close()



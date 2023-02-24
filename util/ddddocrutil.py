# -*- coding: utf-8 -*-
import os
import ddddocr


# 图片识别函数
def img2text(img_file):
    ocr = ddddocr.DdddOcr()  # 法1
    # ocr = ddddocr.DdddOcr(det=True) #法2
    cPath = os.getcwd()
    # print(cPath)
    with open(img_file, 'rb') as f:
        # print("file", f)
        img_bytes = f.read()
        # 获取文字
        res = ocr.classification(img_bytes)
        # print(res)
        return res


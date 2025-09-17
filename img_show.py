# -*- coding: utf-8 -*-
# @Time : 11/28/24 9:53 PM
# @Author : CSR
# @File : img_show.py

import numpy as np

from PIL import Image

def show_img(img_path:str)->None:
    pil_img = np.array(Image.open(img_path))
    print(pil_img.shape)
    Image.fromarray(pil_img).show()

if __name__ == '__main__':
    image_path = '/home/caisongrui/workspace/deeplearning/data/datasets_lightning/noise/Images/signal1.png'
    show_img(image_path)


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/2 0:02
# @Author  : Xuhaozhang
# @Email   : xuhaozhang_hfut@163.com
# @File    : python_mosaic.py

import photomosaic as pm
from skimage.io import imsave

image = pm.imread('/home/zauhoo/2024.jpg')  # Read the main image.
pool = pm.make_pool('/home/zauhoo/test/*.jpg')  # Read a pool of picture blocks.
mos_basic = pm.basic_mosaic(image, pool, (30, 30), depth=1)  # Draw a basic mosaic.

imsave('mos_basic.png', mos_basic)
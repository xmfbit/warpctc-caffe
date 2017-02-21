#!/usr/bin/env python
# coding=utf-8
from captcha.image import ImageCaptcha
import os
import numpy as np

DATASET_SIZE = 5000
LABEL_SEQ_LENGTH = 5
def generate_random_label(length):
    """
    generate labels, we use 0 as blank
    """
    rand_array = np.random.randint(11, size = length)
    not_blank = rand_array[rand_array > 0]
    not_blank -= 1
    return ''.join(map(lambda x: str(x), not_blank))

image = ImageCaptcha()
#CAFFE_ROOT='/home/xmf/caffe-dist/caffe-warpctc/'
CAFFE_ROOT = os.getcwd()   # assume you are in $CAFFE_ROOT$ dir
img_path = os.path.join(CAFFE_ROOT, 'data/captcha/')

for i in xrange(DATASET_SIZE):
    label_seq = generate_random_label(LABEL_SEQ_LENGTH)
    image.write(label_seq, os.path.join(img_path, '%05d-'%i + label_seq + '.png'))

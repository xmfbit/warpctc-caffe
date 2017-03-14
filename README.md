# Caffe-With-Warpctc

CTC Loss is used in sequence learning. The repo merges WarpCTC which is implmented and maintained by Baidu Research into Caffe.

There is a toy demo in `examples/warpctc_captcha`, which can train a 2-layer lstm model to recongnize the captcha in an image. To run the demo, you should first generate the dataset for trainning and validating with the python scripts, then it is an ordinary tranning procedure using Caffe.

This repo is a personal project.


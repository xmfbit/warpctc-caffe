# Caffe-With-Warpctc

CTC Loss is used in sequence learning. The repo merges WarpCTC which is implmented and maintained by Baidu Research into Caffe.

There is a toy demo in `examples/warpctc_captcha`, which can train a 2-layer lstm model to recongnize the captcha in an image. To run the demo, you should first generate the dataset for training and validating with the python scripts, then it is an ordinary tranning procedure using Caffe.

Here is also a similar repo implemented by PyTorch. See [captcha-recognition](https://github.com/xmfbit/captcha-recognition) for detail.

This repo is a personal project.

## Issue when building the project
Please comment the following lines in `Makefile.config`, otherwise it may cause gradient explosion when training because old CUDA runtime library doesn't support `__shlf_down` used in Baidu's implementation. See [issue 1](https://github.com/xmfbit/warpctc-caffe/issues/1) for detail(discussion in Chinese).

```
-gencode arch=compute_20,code=sm_20 
-gencode arch=compute_20,code=sm_21
```

## How to run the demo

In this demo, captcha images can contain digit sequence with different length(more specifically, 1~5 digits). CTC loss is very suitable for this kind of variable length sequence learning. See the three images below for detail of the examples in the demo.

![captcha image with 3 digits](/docs/images/captcha/99944-492.png)
![captcha image with 4 digits](/docs/images/captcha/99938-4518.png)
![captcha image with 5 digits](/docs/images/captcha/99937-82028.png)

The original WarpCTC by Baidu Research supports multi-thread processing when using CPU. However it is not supported by this repo. So GPU is necessary for the following experiment, otherwise the running time will be unbearably long. Or you can reduce the dataset size to save time.

To run the demo, first, make sure you are in `$CAFFE_ROOT` directory. Then, run the scripts to generate data using python `captcha` library and hdf5 files for training and testing.

```
# generate data
python examples/warpctc_captcha/generate_captcha.py
# generate hdf5 files
python examples/warpctc_captcha/generate_dataset.py
```

Due to different hardware capabilities, this process may take a different time. Then you should find captcha images in directory `$CAFFE_ROOT/data/captcha`. You can change the parameters in the above two scripts to get larger dataset and use more threads to accerate the process.

Then, you can run the bash script to train the 2-layer lstm model using ctc loss.

```
./examples/warpctc_captcha/train.sh
```

Have a cup of coffee when training!

## Demo results

I ran the demo for several times and the model can converge finally. The accuracy of the model is not too high, but enough to prove the power of the naive 2-layer lstm network trained with CTC loss.

![trainning loss result](/docs/images/captcha/train_loss.png)
![test loss result](/docs/images/captcha/test_loss.png)
![test accuracy](/docs/images/captcha/test_accuracy.png)

The model I trainned can be downloaded from [Google Drive](https://drive.google.com/file/d/0B98MUaCGMMG0UVd1WWFrNHZLdTg/view?usp=sharing).

Check `./examples/warpctc_captcha/captcha_prediction.cpp` for deployment. It is modified based on `examples/cpp_classification/classification.cpp`.


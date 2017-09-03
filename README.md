# **ON DEVELOPING!!**


## PHD08 Conversion

> [phd08](https://www.dropbox.com/s/69cwkkqt4m1xl55/phd08.alz?dl=0) 
데이터셋을 .png 로 저장하거나, numpy array 로 바로 변환 가능한 txt 파일 형태로 변환해 줍니다. 
이미지 / 텍스트는 기존 바이너리로 되어 있던 것을 가우시안 필터로 블러링합니다.

## Requirements
- python3
- numpy
- matplotlib
- scipy

## Usage
### phd08_to_png.py
0. **help**
```
python phd08_to_png.py --help
```

1. **phd08** to **png**
```
python phd08_to_png.py --data_dir=DATA_DIR [--width=WIDTH] [--height=HEIGHT] [--gaussian_sigma=GAUSSIAN_SIGMA]  
```

2. **phd08** to **np.array text files**


### phd08_to_np_arr.py
0. **help**
```
python phd08_to_np_arr.py --help
```

import argparse
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage.filters import gaussian_filter


def parse_args():
    desc = "phd08 한글 텍스트 데이터를 numpy array 로 바로 변환 가능한 txt 파일 형태로 바꿔좁니다."
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--data_dir', type=str, default='phd08_sample',
                        help='phd08 한글 데이터가 존재하는 디렉토리', required=True)
    parser.add_argument('--width', type=int, default=60,
                        help='txt 로 저장할때의 가로 어레이 사이즈', required=False)
    parser.add_argument('--height', type=int, default=60,
                        help='txt 로 저장할때의 세로 어레이 사이즈', required=False)

    return parser.parse_args()

def main():
    args = parse_args()
    if args is None:
        exit()

    # 존재유무 체크
    if not os.path.exists(args.data_dir):
        print("ERROR::" + args.data_dir, " 는 존재하지 않는 폴더입니다.")
        exit()

    for _, _, files in os.walk(args.data_dir):
        for file in files:
            if file[0] == '.':
                continue
            print("INFO:: converting " + file + "...")


    print("INFO:: all files converted to txt, results in phd08_txt_results")

if __name__ == '__main__':
    main()

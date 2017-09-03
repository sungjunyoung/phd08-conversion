# -*- coding: cp949 -*-

import argparse
import os
import numpy as np


def parse_args():
    desc = "phd08 한글 텍스트 데이터를 .png 포맷으로 변환해주는 스크립트입니다."
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--data_dir', type=str, default='phd08',
                        help='phd08 한글 데이터가 존재하는 디렉토리', required=True)

    return parser.parse_args()


def file_to_arr(file_full_path):
    f = open(file_full_path)


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
            print("INFO:: converting " + file + "...")
            file_to_arr(args.data_dir + '/' + file)


if __name__ == '__main__':
    main()

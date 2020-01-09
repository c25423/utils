import os
import sys
import argparse
import glob

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', default='./', type=str, help='path')
    parser.add_argument('--name', default='.txt', type=str, help='name')
    parser.add_argument('--fe', default='cp936', type=str, help='from encoding')
    parser.add_argument('--te', default='utf-8', type=str, help='to encoding')
    args = parser.parse_args()

    for file_name in os.listdir(args.path):
        if file_name.endswith(args.name):
            file_name = args.path + file_name
            bak_name = file_name + ".bak"
            os.system("mv {} {}".format(file_name, bak_name))
            os.system("iconv -f {} -t {} {} > {}".format(args.fe, args.te, bak_name, file_name))

if __name__ == "__main__":
    main()

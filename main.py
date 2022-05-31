import argparse
import os
from server.FileService import change_dir


def main():
    parser = argparse.ArgumentParser(description='Path to the working directory')
    parser.add_argument('-d', '--dir', type=str, help='Input path to the working directory', default=os.getcwd())
    args = parser.parse_args()
    
    change_dir(args.dir)


if __name__ == '__main__':
    main()

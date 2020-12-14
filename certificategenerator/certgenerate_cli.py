import argparse

def make_parser():
    parser = argparse.ArgumentParser(prog="certificategenerate", description="Certificate generation.")
    parser.add_argument(
        'csvpath', metavar='csvpath', type=str, help='path to the csv file'
    )
    parser.add_argument(
        'imgpath', metavar='imgpath', type=str, help='path to the image'
    )
    parser.add_argument(
        '-style', metavar='style', type=int, help='style wanted', required=False, default=1
    )
    return parser

def main():
    parser = make_parser()
    args = parser.parse_args()
    path_to_csv = args.csvpath
    path_to_img = args.imgpath

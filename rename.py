import os
import glob
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-vd", default=None, help="Directory for videos. ")
parser.add_argument("-sd", default=None, help="Sub directory for subtitles is applicable. ")
parser.add_argument("-vf", default=".mkv", help="Video format. Default as \".mkv\"")
parser.add_argument("-sf", default=".ass", help="Subtitle format. Default as \".ass\"")
parser.add_argument("-lang", default="", help="Add language indicator before extension type.")

args = parser.parse_args()

# Set video and subtitle directories based on args. 
VID_DIR = "./" if args.vd == None else args.vd if args.vd[:1] == "/" or args.vd[:2] == "./" else os.path.join("./", args.vd)
SUB_DIR = VID_DIR if args.sd == None else args.sd if args.sd[:1] == "/" or args.sd[:2] == "./" else os.path.join(VID_DIR, args.sd)
# Set other args. 
VID_EXT = args.vf
SUB_EXT = args.sf
LANG = args.lang
# Save video file names and subtitle file names as lists. 
VID_NAMES = [f.replace(VID_DIR, "") for f in glob.glob(os.path.join(VID_DIR, "*"+VID_EXT))]
SUB_NAMES = [f.replace(SUB_DIR, "") for f in glob.glob(os.path.join(SUB_DIR, "*"+SUB_EXT))]

# Check if directories contain files in specified format. 
def valid_args():
    print("LOG: Video directory set as {}".format(VID_DIR))
    print("LOG: Subtitle directory set as {}".format(SUB_DIR))

    if len(VID_NAMES) == 0:
        print("ERROR: No {} files in directory {}".format(VID_EXT, VID_DIR))
        exit()

    if len(SUB_NAMES) == 0:
        print("ERROR: No {} files in directory {}".format(SUB_EXT, SUB_DIR))
        exit()

# Edge cases
# - Only one video file, e.g., movie. 
# - Special episode number, e.g., 10.5 and 10v2. 

def rename():
    vid_names_no_ext = [f.split(".")[0] for f in VID_NAMES]


def main():
    # rootDir = "/Users/c25423/inbox/sound-euphonium-2/"
    # newDir = "[VCB-Studio] Hibike! Euphonium 2 [{episode}][Ma10p_1080p][x265_flac_2aac].ass"

    # # for dir in (glob.glob("/Users/c25423/inbox/sound-euphonium-2/*.ass")):
    # for dir in (glob.glob("./*.ass")):
    #     print(dir)
    #     os.rename(dir, dir.replace(".ass", ".sc.ass"))

    # vid_names = glob.glob()
    valid_args()
    rename()

if __name__=="__main__":
    main()
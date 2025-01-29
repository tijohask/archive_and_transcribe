import os
import argparse

from scraper import get_next_vid_link
from download import download_content
from transcribe import transcribe_file

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--channel", help="The rumble channel to get the data out of")
args = parser.parse_args()
print(args.channel)
channel = args.channel

def load_config(config_file: str):
    pass


def main():
    i = 0
    for vid in get_next_vid_link(channel):
        print(vid)
        download_content(vid['link'])
        i = i + 1
        if (i > 3): break



if __name__ == '__main__':
    main()
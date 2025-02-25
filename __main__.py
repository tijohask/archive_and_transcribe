import os
import argparse
import time
import random

from scraper import get_next_vid_link
from download import download_content
from transcribe import transcribe_file

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--channel", help="The rumble channel to get the data out of")
parser.add_argument("-m", "--max-videos", help="How many videos to download before stopping")
parser.add_argument("--max-duration", help="Maximum duration for video download in seconds")
parser.add_argument("--min-duration", help="Minimum duration for video download in seconds (cannot be 0)")
parser.add_argument("--sleep-interval", help="How long to wait in seconds between downloading videos. Acts as minimum if max-interval is also declared")
parser.add_argument("--max-sleep-interval", help="Maximum length of time in seconds between downloading videos. Requires min-interval to be set.")
args = parser.parse_args()

channel = args.channel
max_videos = 0
max_duration = 0
min_duration = 0
min_sleep = 0
max_sleep = 0
if(args.max_videos): max_videos = int(args.max_videos)
if(args.max_duration): max_duration = int(args.max_duration)
if(args.min_duration): min_duration = int(args.min_duration)
if(args.sleep_interval): min_sleep = int(args.sleep_interval)
if(args.max_sleep_interval): max_sleep = int(args.max_sleep_interval)
if(not channel):
    print("Channel Required")
    exit()

#sanity check for sleep interval
if(min_sleep > max_sleep): max_sleep = min_sleep

def load_config(config_file: str):
    pass

def get_seconds_from_duration(duration):
    dur_arr = duration.split(':')
    square = 0
    seconds = 0
    for i in reversed(dur_arr):
        seconds = seconds + (int(i) * (60 ** square))
        square = square + 1
    return seconds

def can_download(vid):
    if os.path.exists(f"./output/{vid['channel_name']}/{vid['title']}.m4a"):
        return False
    print(f"./output/{vid['channel_name']}/{vid['title']}.m4a")
    duration = get_seconds_from_duration(vid['duration'])
    if(max_duration and duration > max_duration):
        return False
    if(min_duration and duration < min_duration):
        return False
    return True

def main():
    i = 0
    for vid in get_next_vid_link(channel):
        print(vid)
        os.makedirs(f"./output/{vid['channel_name']}", exist_ok=True)
        if (can_download(vid)):
            time.sleep(random.randint(min_sleep, max_sleep))
            download_content(vid)
            i = i + 1
        if (max_videos and i >= max_videos):
            break



if __name__ == '__main__':
    main()
import os
import argparse
import time
import random

from scraper import get_next_vid_link
from download import download_content
from download import valid_title
from transcribe import transcribe_file

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--channel", help="The rumble channel to get the data out of")
parser.add_argument("-m", "--max-videos", help="How many videos to download before stopping")
parser.add_argument("--max-duplicates", help="Number of duplicates that can be found before ending the program")
parser.add_argument("--max-duration", help="Maximum duration for video download in seconds")
parser.add_argument("--min-duration", help="Minimum duration for video download in seconds (cannot be 0)")
parser.add_argument("--sleep-interval", help="How long to wait in seconds between downloading videos. Acts as minimum if max-interval is also declared")
parser.add_argument("--max-sleep-interval", help="Maximum length of time in seconds between downloading videos. Requires min-interval to be set.")
parser.add_argument("-o", "--output", help="Directory to write the files to.")
args = parser.parse_args()

channel = args.channel
max_videos = 0
max_duplicates = 0
max_duration = 0
min_duration = 0
min_sleep = 0
max_sleep = 0
output = "./output"
if(args.max_videos): max_videos = int(args.max_videos)
if(args.max_duplicates): max_duplicates = int(args.max_duplicates)
if(args.max_duration): max_duration = int(args.max_duration)
if(args.min_duration): min_duration = int(args.min_duration)
if(args.sleep_interval): min_sleep = int(args.sleep_interval)
if(args.max_sleep_interval): max_sleep = int(args.max_sleep_interval)
if(args.output): output = args.output
if(not channel):
    print("Channel Required")
    exit()

#sanity check for sleep interval
if(min_sleep > max_sleep): max_sleep = min_sleep
duplicates = 0

def load_config(config_file: str):
    pass

def get_seconds_from_duration(duration):
    dur_arr = duration.split(':')
    if(len(dur_arr) < 3): dur_arr.insert(0, '00')
    seconds = (int(dur_arr[0]) * 3600) + (int(dur_arr[1]) * 60) + int(dur_arr[2])
    return seconds

def can_download(vid):
    title = valid_title(vid['title'])
    if os.path.exists(f"{output}/{title}.m4a"):
        global duplicates
        duplicates = duplicates + 1
        return False
    print(f"{output}/{title}.m4a")
    duration = get_seconds_from_duration(vid['duration'])
    if(max_duration and duration > max_duration):
        return False
    if(min_duration and duration < min_duration):
        return False
    return True

def main():
    i = 0
    for vid in get_next_vid_link(channel):
        vid['output'] = output
        print(vid)
        os.makedirs(output, exist_ok=True)
        if (can_download(vid)):
            download_content(vid)
            time.sleep(random.randint(min_sleep, max_sleep))
            i = i + 1
        if (max_videos and i >= max_videos):
            break
        if (max_duplicates and duplicates >= max_duplicates):
            break


if __name__ == '__main__':
    main()

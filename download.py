import os
import yt_dlp

ydl_opts = {
    'write_info_json': True,
    'format': 'mp4-360p-0/mp4-360p',
    #'download_archive': 'archive',
    'postprocessors': [
        { 'key': 'FFmpegExtractAudio', 'preferredcodec': 'm4a' },
        { 'key': 'FFmpegMetadata' },
    ]
}

def download_content(vid):
    #print(ydl_opts)
    # Make sure the audio file does not already exist. 
    # Assume the audio file is complete and without issue.
    if not os.path.exists(f"./output/{vid['channel_name']}/{vid['title']}.m4a"):
        # Adding to the ydl_opts here because I want to store every video in 
        # a folder named after the channel.
        ydl_opts['outtmpl'] = f"./output/{vid['channel_name']}/%(title)s.%(ext)s"
        ydl = yt_dlp.YoutubeDL(ydl_opts)
        info = ydl.extract_info(vid['link'])

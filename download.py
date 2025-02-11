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
    # Adding to the ydl_opts here because I want to store every video in
    # a folder named after the channel.
    ydl_opts['outtmpl'] = f"./output/{vid['channel_name']}/{vid['title']}.%(ext)s"
    ydl = yt_dlp.YoutubeDL(ydl_opts)
    info = ydl.extract_info(vid['link'])

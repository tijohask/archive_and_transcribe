import yt_dlp

ydl_opts = {
    'write_info_json': True,
    'format': 'mp4-360p',#'m4a/bestaudio/best',
    'postprocessors': [
        { 'key': 'FFmpegExtractAudio', 'preferredcodec': 'm4a' },
        { 'key': 'FFmpegMetadata' },
    ]
}

def download_content(link):
    ydl = yt_dlp.YoutubeDL(ydl_opts)
    info = ydl.extract_info(link)
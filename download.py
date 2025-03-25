import yt_dlp

ydl_opts = {
    'write_info_json': True,
    'format': 'mp4-360p-0/mp4-360p',
    'outtmpl': "%(title)s.%(ext)s",
    #'download_archive': 'archive',
    'postprocessors': [
        { 'key': 'FFmpegExtractAudio', 'preferredcodec': 'm4a' },
        { 'key': 'FFmpegMetadata' },
        {'actions':
            [(yt_dlp.postprocessor.metadataparser.MetadataParserPP.replacer,
                'title',
                '[\\?/:]',
                '-'
            )],
            'key': 'MetadataParser',
            'when': 'pre_process'
        }
    ]
}

def valid_title(string):
    return string.replace("/", "-").replace(":", "-").replace("\"", "-").replace("?", "-")

def download_content(vid):
    #print(ydl_opts)
    # Adding to the ydl_opts here because I want to store every video in
    # a folder named after the channel.
    ydl_opts['outtmpl'] = f"{vid['output']}/%(title)s.%(ext)s"
    ydl = yt_dlp.YoutubeDL(ydl_opts)
    info = ydl.extract_info(vid['link'])
    return info['requested_downloads'][0]['filepath']

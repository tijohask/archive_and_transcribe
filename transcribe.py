import whisper
import json
import time

def get_time_format(stamp):
    hour = int(stamp / 3600)
    min  = int(stamp / 60) - (hour * 60)
    sec  = stamp % 60
    return "{0:02d}:{1:02d}:{2:06.3f}".format(hour, min, sec)

def transcribe_file(file):
    prog_start = time.time()
    model = whisper.load_model("small.en")
    result = model.transcribe(file)
    prog_end = time.time()
    result['time'] = prog_end - prog_start

    t = file.rsplit('.m4a', 1)
    backup_file = '.json'.join(t)
    with open(backup_file, "w") as file:
        json.dump(result, file, indent=2)

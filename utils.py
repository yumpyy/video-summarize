import re
import os

import yt_dlp
from ffmpeg import FFmpeg

def filter_transcript(data):
    pattern_list = [
        "[0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]{3} --> [0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]{3}",  # for matching 00:00:00,000 --> 00:00:39,410
        "^[0-9]{1,10}",                                                                  # for matching lines starting with numbers
    ]

    filtered_data = [""]
    for line in data.split('\n'):
        line = re.sub("|".join(pattern_list), "", line)
        if line.strip():
            if filtered_data[-1] == line:
                continue
            else:
                filtered_data.append(line)
    
    filtered_data = " ".join(filtered_data)
    return filtered_data

def convert_sub():
    for file in os.listdir("./"):
        if file.endswith(".vtt"):
            output_file = f"{os.path.splitext(file)[0]}.srt"    # .splitext()[0] is used to get file name
            
            """
            if output file with same name already exists, the program gets stuck.
            added this conditional statment to remove any file with same name before proceeding.
            """
            if os.path.isfile(output_file):
                choice = input(f"\'{output_file}\' already exists. Delete it? [y/N] : ")
                if choice == "y":
                    os.remove(output_file)
                    print("Removing existing file \'{output_file}\'")
                else:
                    print(f"Not removing \'{output_file}\', Exiting..'")
                    exit(1)

            ffmpeg = (
                FFmpeg()
                .input(file)
                .output(output_file)
            )
            ffmpeg.execute()

            return

    print("Transcript file not found in current directory.")
    exit(1)
        
def extract_transcript(url):
    ytdlp_options = {
        'skip_download': True,
        'writeautomaticsub': True,
        'subtitlesformat': 'srt',
        'outtmpl': 'transcript.%(ext)s'
    }

    with yt_dlp.YoutubeDL(ytdlp_options) as yt:
        yt.download(url)

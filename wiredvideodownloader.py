import os
import argparse
from dotenv import load_dotenv
from pytube import YouTube

load_dotenv()

VIDEO_STORE_PATH = os.getenv('VIDEO_STORE_PATH')
AUDIO_STORE_PATH = os.getenv('AUDIO_STORE_PATH')

def progress_func(stream, bytes, bytes_remaining):
    total = stream.filesize
    downloaded = total - bytes_remaining
    completed = int(downloaded / total * 100)
    end = '\r' if completed < 100 else '\n'
    print(f"Downloading... [{'#' * completed}{'.' * (100 - completed)}{completed}%]", end=end)

def download_audio(source, file_name, extension='mp3'):
    try:
        yt = YouTube(source, on_progress_callback=progress_func)
        media = yt.streams.filter(only_audio=True).first()
        media.download(AUDIO_STORE_PATH, f'{file_name}.{extension}')
        print("Download complete successfully")
    except Exception as e:
        print(f"There was an error during audio download: {e}")

def download_video(source, file_name, extension='mp4'):
    try:
        yt = YouTube(source, on_progress_callback=progress_func)
        media = yt.streams.filter(file_extension='mp4').get_highest_resolution()
        media.download(VIDEO_STORE_PATH, f'{file_name}.{extension}')
        print("Download complete successfully")
    except Exception as e:
        print(f"There was an error during video download: {e}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="YouTube URL of the video to download")
    parser.add_argument("file_name", help="Final filename in local system")
    parser.add_argument("-a", "--audio-only", help="Download audio only", action="store_true")
    parser.add_argument("-e", "--extension", help="Extension for saved file")

    args = parser.parse_args()
    extension = args.extension if args.extension else 'mp3' if args.audio_only else 'mp4'
    
    if args.audio_only:
        download_audio(args.source, args.file_name, extension)
    else:
        download_video(args.source, args.file_name, extension)

if __name__ == '__main__':
    main()

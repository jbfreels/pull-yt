import os
import sys
import yt_dlp

opts = {
    "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
    "outtmpl": "%(title)s.%(ext)s",
    "postprocessors": [
        {
            "key": "FFmpegVideoConvertor",
            "preferedformat": "mp4",
        }
    ],
    "external_downloader": "ffmpeg",
    "writesubtitles": False,
    "writeautomaticsub": False,
    "quiet": True,
}


def download_video(url, save_path):
    print(f"url: {url}")
    print(f"out: {save_path}")

    try:
        with yt_dlp.YoutubeDL(opts) as ytdlp:
            ytdlp.download([url])
    except Exception as e:
        print(f"{e}\nbad url?")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        video_url = sys.argv[1]
    else:
        print("pull-yt.py <youtube_url>")
        sys.exit(1)

    download_video(video_url, f"{os.getcwd()}")

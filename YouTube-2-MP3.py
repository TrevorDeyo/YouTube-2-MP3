import os
import yt_dlp

def download_youtube_playlist(playlist_url, output_directory):
    # Create a yt_dlp object with options for downloading audio only in MP3
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_directory, '%(title)s.%(ext)s'),
    }

    # Download the playlist
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

def main():
    # Specify the playlist URL and output directory
    playlist_url = 'https://www.youtube.com/playlist?list=PL4waBsMLGZzK6gYLG2pd7RoyxD1TfD2uA'
    output_directory = r'C:\Users\tdeyo\Desktop\Code\YouTube-2-MP3\mp3s'

    # Download the YouTube playlist in MP3 format directly
    download_youtube_playlist(playlist_url, output_directory)

if __name__ == "__main__":
    main()
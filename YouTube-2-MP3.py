from pytube import YouTube

video_url = input("Enter the URL of the YouTube video: ")
yt = YouTube(video_url)
video = yt.streams.filter(only_audio=True).first()
filename = f"{yt.title}.mp3"
video.download(filename=filename)
print(f"Download complete: {filename}")

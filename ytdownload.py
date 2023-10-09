from pytube import YouTube

def yt_download(url, file='download.mp4'):
    yt = YouTube(url) #Youtube 영상 주소

    yt.streams.filter(file_extension='mp4').get_by_resolution('720p').download(
        output_path='.', filename=file)
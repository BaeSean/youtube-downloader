from ytdownload import yt_download
from clip import sample_video, convert_time_to_seconds

url = 'https://youtu.be/6TEOiVX2Mjs'

file_name = '원본.mp4'
output_folder = '.'
start_time = '00:00:00'
end_time = '00:00:16'


yt_download(url, file_name)

sample_video(file_name, output_folder, start_time, end_time)



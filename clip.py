import os
import subprocess

def sample_video(video_path, output_folder, start_time, end_time, interval=15):

    # 비디오의 총 길이 가져오기
    duration_cmd = 'ffprobe -i {} -show_entries format=duration -v quiet -of csv="p=0"'.format(video_path)
    duration = float(subprocess.check_output(duration_cmd, shell=True))

    if(str(end_time) > str(duration)):
        print("잘못된 파일 길이")
        return
    
    # 시작 시간과 끝 시간을 초로 변환
    start_time_sec = convert_time_to_seconds(start_time)
    end_time_sec = convert_time_to_seconds(end_time)

    interval = end_time_sec - start_time_sec
    
    # 영상 샘플링
    sample_count = 1
    for i in range(start_time_sec, end_time_sec, interval):
        output_file = os.path.join(output_folder, 'sample{}.mp4'.format(sample_count))
        sample_cmd = 'ffmpeg -i {} -ss {} -t {} {}'.format(video_path, i, interval, output_file)
        subprocess.call(sample_cmd, shell=True)
        sample_count += 1

def convert_time_to_seconds(time_str):
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

# # 영상 경로 설정
# video_path = 'download.mp4'
# output_folder = '.'

# # 시작 시간과 끝 시간 설정 (예시: 00:01:30부터 00:05:00까지)
# start_time = '00:00:00'
# end_time = '00:00:12'

# # 영상 샘플링 실행
# sample_video(video_path, output_folder, start_time, end_time)

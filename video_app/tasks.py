import subprocess
import os


def convert_to_360p(file_path):
    file_path_no_extension, file_extension = os.path.splitext(file_path)
    target_path = f"{file_path_no_extension}_360p{file_extension}"
    cmd_1 = f'ffmpeg -i "{file_path}" -vf "scale=640:360" -c:v libx264 -crf 23 -c:a aac -strict -2 "{target_path}"'
    subprocess.run(cmd_1)
    convert_to_hsl_format(file_path)


def convert_to_hsl_format(file_path):
    cmd = f'ffmpeg -i "{file_path}" -codec: copy -start_number 0 -hls_time 10 -hls_list_size 0 -f hls output.m3u8'
    subprocess.run(cmd)
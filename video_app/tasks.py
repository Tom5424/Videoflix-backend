from celery import shared_task
import subprocess
import os


@shared_task
def convert_to_360p(file_path):
    file_path_no_extension, file_extension = os.path.splitext(file_path)
    target_path = f"{file_path_no_extension}_360p{file_extension}"
    file_path_linux = "/mnt/" + file_path.replace("\\", "/").replace("C:", "c")
    target_path_linux = "/mnt/" + target_path.replace("\\", "/").replace("C:", "c")
    cmd = f'ffmpeg -i "{file_path_linux}" -vf "scale=640:360" -c:v libx264 -crf 23 -c:a aac -strict -2 "{target_path_linux}"'
    subprocess.run(cmd, capture_output=True, shell=True)
    convert_to_hsl_format(file_path_linux)


def convert_to_hsl_format(file_path_linux):
    cmd = f'ffmpeg -i "{file_path_linux}" -codec: copy -start_number 0 -hls_time 10 -hls_list_size 0 -f hls output.m3u8'
    subprocess.run(cmd, capture_output=True, shell=True)
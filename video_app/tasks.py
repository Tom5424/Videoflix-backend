from django.core.files import File
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
    output_dir = "/mnt/c/Users/tompe/Desktop/Videoflix-backend/media/hls-outputs"
    base_name = os.path.splitext(os.path.basename(file_path_linux))[0]
    output_m3u8_data = os.path.join(output_dir, f"{base_name}.m3u8").replace("\\", "/")
    output_ts_data = os.path.join(output_dir, f"{base_name}_%03d.ts").replace("\\", "/")
    cmd = f'ffmpeg -i "{file_path_linux}" -c copy -start_number 0 -hls_time 10 -hls_list_size 0 -hls_segment_filename "{output_ts_data}" -f hls "{output_m3u8_data}"'
    subprocess.run(cmd, capture_output=True, shell=True)


def create_video_image(video):
    video_path = video.video_file.path
    video_image_path = os.path.splitext(video_path)[0] + ".jpg"
    cmd = f'ffmpeg -i "{video_path}" -ss 00:00:01 -frames:v 1 -q:v 2 -update 1 "{video_image_path}"'
    subprocess.run(cmd, shell=True, check=True)
    with open(video_image_path, "rb") as img_file:
        video.video_image.save(os.path.basename(video_image_path), File(img_file), save=True)
    os.remove(video_image_path)
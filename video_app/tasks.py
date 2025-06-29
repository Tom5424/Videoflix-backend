from django.core.files import File
from django.conf import settings
from celery import shared_task
import subprocess
import os


@shared_task
def converts_to_multi_qualities_and_hls_format(file_path):
    input_path = os.path.join(settings.MEDIA_ROOT, file_path)
    file_name = os.path.splitext(os.path.basename(input_path))[0]
    output_directory = os.path.join(settings.MEDIA_ROOT, "hls-outputs")
    os.makedirs(output_directory, exist_ok=True)
    master_playlist_name = f"{file_name}_master.m3u8"
    segment_files = f"{output_directory}/{file_name}_%v_%03d.ts"
    playlist_data = f"{output_directory}/{file_name}_%v.m3u8"
    cmd = [
        "ffmpeg", "-y",
        "-nostdin",
        "-fflags", "+genpts",
        "-i", input_path,
        "-filter_complex",
        "[0:v]split=4[v1][v2][v3][v4];"
        "[v1]scale=w=640:h=360[vout1];"
        "[v2]scale=w=854:h=480[vout2];"
        "[v3]scale=w=1280:h=720[vout3];"
        "[v4]scale=w=1920:h=1080[vout4]",
        "-map", "[vout1]", "-c:v:0", "libx264", "-b:v:0", "800k",
        "-map", "[vout2]", "-c:v:1", "libx264", "-b:v:1", "1400k",
        "-map", "[vout3]", "-c:v:2", "libx264", "-b:v:2", "2800k",
        "-map", "[vout4]", "-c:v:3", "libx264", "-b:v:3", "5000k",
        "-preset", "veryfast",          
        "-an",                          
        "-f", "hls",
        "-hls_time", "3",
        "-hls_list_size", "0",
        "-hls_playlist_type", "vod",
        "-hls_flags", "independent_segments",
        "-hls_segment_filename", segment_files,
        "-master_pl_name", master_playlist_name,
        "-var_stream_map", "v:0 v:1 v:2 v:3",
        playlist_data                 
    ]
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


def create_video_image(video):
    video_path = video.video_file.path
    video_image_path = os.path.splitext(video_path)[0] + ".jpg"
    cmd = f'ffmpeg -i "{video_path}" -ss 00:00:01 -frames:v 1 -q:v 2 -update 1 "{video_image_path}"'
    subprocess.run(cmd, shell=True, check=True)
    with open(video_image_path, "rb") as img_file:
        video.video_image.save(
            os.path.basename(video_image_path), File(img_file), save=True
        )
    os.remove(video_image_path)
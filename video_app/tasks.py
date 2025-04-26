from django.core.files import File
from celery import shared_task
import subprocess
import os


@shared_task
def converts_to_multi_qualities_and_hls_format(file_path):
    file_path_linux = "/mnt/" + file_path.replace("\\", "/").replace("C:", "c")
    file_name = os.path.splitext(os.path.basename(file_path_linux))[0]
    out_directory = "/mnt/c/Users/tompe/Desktop/Videoflix-backend/media/hls-outputs"
    os.makedirs(out_directory, exist_ok=True)
    master_playlist_name = f"{file_name}_master.m3u8"
    segment_files = f"{out_directory}/{file_name}_%v_%03d.ts"
    playlist_data = f"{out_directory}/{file_name}_%v.m3u8"
    cmd = [
        "ffmpeg", "-i", file_path_linux,
        "-filter_complex",
        "[0:v]split=4[v1][v2][v3][v4];"
        "[v1]scale=160:120[vout1];"
        "[v2]scale=640:360[vout2];"
        "[v3]scale=1280:720[vout3];"
        "[v4]scale=1920:1080[vout4]",
        "-map", "[vout1]", "-c:v:0", "libx264", "-b:v:0", "150k",
        "-map", "[vout2]", "-c:v:1", "libx264", "-b:v:1", "800k",
        "-map", "[vout3]", "-c:v:2", "libx264", "-b:v:2", "2800k",
        "-map", "[vout4]", "-c:v:3", "libx264", "-b:v:3", "5000k",
        "-f", "hls",
        "-hls_time", "10",
        "-hls_playlist_type", "vod",
        "-hls_segment_filename", segment_files,
        "-master_pl_name", master_playlist_name,
        "-var_stream_map", "v:0 v:1 v:2 v:3",
        playlist_data,
        "-preset", "veryfast",
    ]
    subprocess.run(cmd, check=True)



def create_video_image(video):
    video_path = video.video_file.path
    video_image_path = os.path.splitext(video_path)[0] + ".jpg"
    cmd = f'ffmpeg -i "{video_path}" -ss 00:00:01 -frames:v 1 -q:v 2 -update 1 "{video_image_path}"'
    subprocess.run(cmd, shell=True, check=True)
    with open(video_image_path, "rb") as img_file:
        video.video_image.save(os.path.basename(video_image_path), File(img_file), save=True)
    os.remove(video_image_path)
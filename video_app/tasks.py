import subprocess


def convert_360p(file_name):
    index = file_name.rfind('.')
    new_file_name = file_name[:index] + '_360p' + file_name[index:]
    cmd = f'ffmpeg -i "{file_name}" -s 640x360 -c:v libx264 -crf 23 -c:a aac -strict -2 "{new_file_name}"'
    subprocess.run(cmd)
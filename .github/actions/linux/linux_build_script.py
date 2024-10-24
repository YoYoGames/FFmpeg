import os
import shutil

github_workspace = os.getenv('GITHUB_WORKSPACE')
base_lib_dir = os.path.join(github_workspace, 'out/full_deploy/host')
base_bin_dir = os.path.join(github_workspace, 'out/full_deploy/host/ffmpeg')
target_dir = os.path.join(github_workspace, 'out/linux')

os.makedirs(target_dir, exist_ok=True)

files_to_copy = [
    "ffmpeg",
    "ffprobe",
    "libavcodec.so.60",
    "libavfilter.so.9",
    "libavformat.so.60",
    "libavutil.so.58",
    "libcharset.so.1",
    "libiconv.so.2",
    "liblzma.so.5",
    "libmp3lame.so.0",
    "libogg.so.0",
    "libopus.so.0",
    "libswresample.so.4",
    "libvorbis.so.0.4.9",
    "libvorbisenc.so.2.0.12",
    "libvorbisfile.so.3.3.8"
]

def find_binary_file(binary_name):
    for root, dirs, files in os.walk(base_bin_dir):
        for file in files:
            if binary_name in file:
                return os.path.join(root, file)
    return None

def find_library_file(library_name):
    for root, dirs, files in os.walk(base_lib_dir):
        for file in files:
            if library_name in file:
                return os.path.join(root, file)
    return None

for filename in files_to_copy:
    if filename in ["ffmpeg", "ffprobe", "libcharset.so.1"]:
        source_path = find_binary_file(filename) 
    else:
        source_path = find_library_file(filename) 

    if source_path is not None and os.path.isfile(source_path):
        shutil.copy2(source_path, target_dir)
        print(f"Copied {source_path} to {target_dir}")
    else:
        print(f"File not found: {filename} (resolved path: {source_path})")

print("File copying completed.")

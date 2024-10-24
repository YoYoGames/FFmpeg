import os
import shutil

github_workspace = os.getenv('GITHUB_WORKSPACE')

base_lib_dir = os.path.join(github_workspace, 'out/full_deploy/host')

bin_base_dir = os.path.join(github_workspace, 'out/full_deploy/host/ffmpeg')

target_dir = os.path.join(github_workspace, 'out/windows')

files_to_copy = [
    "ffmpeg.exe",
    "ffprobe.exe",
    "avcodec.60.dll",
    "avfilter.9.dll",
    "avformat.60.dll",
    "avutil.58.dll",
    "charset.1.dll",
    "iconv.2.dll",
    "liblzma.dll",
    "libmp3lame.dll",
    "ogg.dll",
    "opus.dll",
    "swresample.4.dll",
    "vorbis.dll",
    "vorbisenc.dll",
    "vorbisfile.dll"
]

os.makedirs(target_dir, exist_ok=True)

def find_binary_file(binary_name):
    for root, dirs, files in os.walk(bin_base_dir):
        for file in files:
            if binary_name == file:
                return os.path.join(root, file)
    return None

def find_library_file(library_name):
    for root, dirs, files in os.walk(base_lib_dir):
        for file in files:
            if library_name in file:
                return os.path.join(root, file)
    return None

for filename in files_to_copy:
    if filename in ["ffmpeg", "ffprobe", "libcharset.1.dylib"]:
        source_path = find_binary_file(filename) 
    else:
        source_path = find_library_file(filename) 

    if os.path.isfile(source_path):
        shutil.copy2(source_path, target_dir)
        print(f"Copied {source_path} to {target_dir}")
    else:
        print(f"File not found: {source_path}")

print("File copying completed.")

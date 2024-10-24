import os
import shutil

github_workspace = os.getenv('GITHUB_WORKSPACE')

base_lib_dir = os.path.join(github_workspace, 'out/full_deploy/host')

base_bin_dir = os.path.join(github_workspace, 'out/full_deploy/host/ffmpeg')

target_dir = os.path.join(github_workspace, 'out/macos')

files_to_copy = [
    "ffmpeg",
    "ffprobe",
    "libavcodec.60.dylib",
    "libavfilter.9.dylib",
    "libavformat.60.dylib",
    "libavutil.58.dylib",
    "libcharset.1.dylib",
    "libiconv.2.dylib",
    "liblzma.5.dylib",
    "libmp3lame.0.dylib",
    "libogg.0.dylib",
    "libopus.0.dylib",
    "libswresample.4.dylib",
    "libvorbis.0.4.9.dylib",
    "libvorbisenc.2.0.12.dylib",
    "libvorbisfile.3.3.8.dylib"
]

os.makedirs(target_dir, exist_ok=True)

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
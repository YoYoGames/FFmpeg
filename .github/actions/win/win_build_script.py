import os
import shutil


github_workspace = os.getenv('GITHUB_WORKSPACE')

if github_workspace is None:
    # Define local paths for testing
    print("Running locally, setting up local paths.")
    base_lib_dir = r"C:\Users\skanu\Downloads\ffmpeg_vendor_package_all_builds\ffmpeg-x86_64-win-Release\full_deploy\host"  # Change this to your local path
    base_bin_dir = r"C:\Users\skanu\Downloads\ffmpeg_vendor_package_all_builds\ffmpeg-x86_64-win-Release\full_deploy\host\ffmpeg"  # Change this to your local path
    target_dir = r"C:\Users\skanu\Downloads\ffmpeg_vendor_package_all_builds\ffmpeg-x86_64-win-Release\out\windows"  # Change this to your local path
else:
    base_lib_dir = os.path.join(github_workspace, 'out/full_deploy/host')
    base_bin_dir = os.path.join(github_workspace, 'out/full_deploy/host/ffmpeg')
    target_dir = os.path.join(github_workspace, 'out/windows')

os.makedirs(target_dir, exist_ok=True)     

files_to_copy = [
    "ffmpeg.exe",
    "ffprobe.exe",
    "avcodec-60.dll",
    "avfilter-9.dll",
    "avformat-60.dll",
    "avutil-58.dll",
    "charset-1.dll",
    "iconv-2.dll",
    "liblzma.dll",
    "libmp3lame.dll",
    "ogg.dll",
    "opus.dll",
    "swresample-4.dll",
    "vorbis.dll",
    "vorbisenc.dll",
    "vorbisfile.dll"
]

def find_binary_file(binary_name):
    for root, dirs, files in os.walk(base_bin_dir):
        for file in files:
            if binary_name in file:
                return os.path.join(root, file)
    return None

def find_library_file(library_name):
    for root, dirs, files in os.walk(base_lib_dir):
        print(f"Searching in: {root}") 
        for file in files:
            if library_name in file:
                return os.path.join(root, file)
    return None

for filename in files_to_copy:
    if filename in ["ffmpeg.exe", "ffprobe.exe", "charset.1.dll", "avcodec-60.dll", "avfilter-9.dll", "avformat-60.dll", "avutil-58.dll", "iconv.2.dll"]:
        source_path = find_binary_file(filename) 
    else:
        source_path = find_library_file(filename) 

    if source_path is not None and os.path.isfile(source_path):
        shutil.copy2(source_path, target_dir)
        print(f"Copied {source_path} to {target_dir}")
    else:
        print(f"File not found: {filename} (resolved path: {source_path})")

print("File copying completed.")

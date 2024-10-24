#!/bin/bash

# Define the directories
X86_64_DIR="$GITHUB_WORKSPACE/ffmpeg/macos-x86"
ARM64_DIR="$GITHUB_WORKSPACE/ffmpeg/macos-arm64"
OUTPUT_DIR="$GITHUB_WORKSPACE/out/macos"

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# List of libraries and executables to create universal binaries for
libraries=(
    "ffmpeg"
    "ffprobe"
    "libavcodec.60.dylib"
    "libavfilter.9.dylib"
    "libavformat.60.dylib"
    "libavutil.58.dylib"
    "libcharset.1.dylib"
    "libiconv.2.dylib"
    "liblzma.5.dylib"
    "libmp3lame.0.dylib"
    "libogg.0.dylib"
    "libopus.0.dylib"
    "libswresample.4.dylib"
    "libvorbis.0.4.9.dylib"
    "libvorbisenc.2.0.12.dylib"
    "libvorbisfile.3.3.8.dylib"
)

# Loop through the libraries and create universal binaries
for lib in "${libraries[@]}"; do
    echo "Creating universal binary for $lib..."
    
    X86_64_FILE="$X86_64_DIR/$lib"
    ARM64_FILE="$ARM64_DIR/$lib"
    
    # Check if both architecture files exist before attempting to create the universal binary
    if [[ -f "$X86_64_FILE" && -f "$ARM64_FILE" ]]; then
        lipo -create -output "$OUTPUT_DIR/$lib" "$X86_64_FILE" "$ARM64_FILE"
        echo "Successfully created universal binary for $lib"
    else
        echo "Skipping $lib, one or both architecture files are missing."
    fi
done

echo "Universal binaries created in $OUTPUT_DIR."

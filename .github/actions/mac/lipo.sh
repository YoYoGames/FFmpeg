#!/bin/bash

X86_64_DIR="$GITHUB_WORKSPACE/ffmpeg/macos-arm64"
ARM64_DIR="$GITHUB_WORKSPACE/ffmpeg/macos-x86"
OUTPUT_DIR="$GITHUB_WORKSPACE/ffmpeg/macos"

mkdir -p "$OUTPUT_DIR"

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

for lib in "${libraries[@]}"; do
    echo "Creating universal binary for $lib..."
    lipo -create -output "$OUTPUT_DIR/$lib" "$X86_64_DIR/$lib" "$ARM64_DIR/$lib"
done

echo "Universal binaries created in $OUTPUT_DIR."

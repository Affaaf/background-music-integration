# Video Background Music Adder

This Python script allows you to add background music or custom audio tracks to a video file. You can specify multiple audio files with start and end times to overlay onto the original video, replacing or mixing with its existing audio.

## 🎯 What It Does

This script is designed to:
- ✅ Add **background music** or **sound effects** to a video
- ✅ Automatically mix multiple audio tracks at specified time intervals
- ✅ Overlay audio without losing video quality
- ✅ Replace the original video with the modified version

## 💡 Example Use Cases
- Adding background music to a video presentation or vlog
- Inserting sound effects at specific moments
- Mixing commentary with original audio

## Requirements
- Python 3.x
- FFmpeg (for video processing)

## Install FFmpeg

Linux:
sudo apt install ffmpeg

macOS:
brew install ffmpeg

## Usage

1. Make sure you have Python installed.
2. Ensure FFmpeg is installed and accessible from the command line.
3. Save the Python script (e.g., `audio_video_merger.py`).
4. Update the script with your desired `video_file` and `audio_files` list.

### Example

```python
if __name__ == "__main__":
    video_file = "practice/video_file.webm"
    audio_files = [
        {"file_path": "file_example_MP3_700KB.mp3", "start_time": 0, "end_time": 50},
        {"file_path": "sample-15s.mp3", "start_time": 180, "end_time": 200},
        {"file_path": "sample-15s.mp3", "start_time": 51, "end_time": 70},
    ]

    create_video_with_audio(video_file, audio_files)

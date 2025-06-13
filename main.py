from utils.audio_video_merger import create_video_with_audio

if __name__ == "__main__":
    # The name of the video file inside utils/video/
    video_file = "video_file.webm"

    # List of audio tracks (all located inside utils/audio/)
    audio_files = [
        {"file_path": "file_example_MP3_700KB.mp3", "start_time": 0, "end_time": 50},
        {"file_path": "sample-15s.mp3", "start_time": 180, "end_time": 200},
        {"file_path": "sample-15s.mp3", "start_time": 51, "end_time": 70},
    ]

    # This will read from utils/video/, overlay audio from utils/audio/, and output to utils/output/final_video.mp4
    create_video_with_audio(video_file, audio_files)

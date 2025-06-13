import subprocess
import os

def create_video_with_audio(video_file, audio_files):
    """
    Add custom audio tracks to a video and replace the original video file.
    
    Args:
        video_file (str): Path to the original video file.
        audio_files (list): List of audio tracks with `file_path`, `start_time`, and `end_time`.
    """
    if not audio_files:
        print("No audio files provided. Exiting.")
        return

    # Temporary output file
    temp_output = "temp_output_video.mp4"

    filter_complex = []
    inputs = [f"-i {video_file}"] + [f"-i {a['file_path']}" for a in audio_files]
    audio_tracks = []

    # Add original video audio
    filter_complex.append("[0:a]volume=1.0[a0]")
    audio_tracks.append("[a0]")

    # Process user-provided audio files
    for i, audio in enumerate(audio_files, start=1):
        start = audio['start_time']
        duration = audio['end_time'] - audio['start_time']
        
        filter_complex.append(
            f"[{i}:a]aloop=loop=-1:size=2e+09,atrim=0:{duration},asetpts=PTS-STARTPTS,"
            f"adelay={start * 1000}|{start * 1000},volume=0.3[a{i}]"
        )
        audio_tracks.append(f"[a{i}]")

    # Combine all audio tracks
    filter_complex.append(f"{''.join(audio_tracks)}amix=inputs={len(audio_tracks)}:duration=longest[aout]")

    # Construct the FFmpeg command
    command = (
        f"ffmpeg {' '.join(inputs)} -filter_complex \"{'; '.join(filter_complex)}\" "
        f"-map 0:v:0 -map \"[aout]\" -c:v copy -c:a aac {temp_output}"
    )

    print("Running FFmpeg command:")
    print(command)

    # Execute the FFmpeg command
    subprocess.run(command, shell=True)

    # Replace the original video file with the new file
    if os.path.exists(temp_output):
        os.replace(temp_output, video_file)
        print(f"Original video file '{video_file}' replaced with the new file.")
    else:
        print("Error: Temporary output file was not created.")

# Example Usage
if __name__ == "__main__":
    video_file = "practice/video_file.webm"
    audio_files = [
        {"file_path": "file_example_MP3_700KB.mp3", "start_time": 0, "end_time": 50},
        {"file_path": "sample-15s.mp3", "start_time": 180, "end_time": 200},
        {"file_path": "sample-15s.mp3", "start_time": 51, "end_time": 70},
    ]

    create_video_with_audio(video_file, audio_files)

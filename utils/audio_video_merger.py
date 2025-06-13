import subprocess
import os

def create_video_with_audio(video_filename, audio_files, output_filename="final_video.mp4"):
    """
    Add custom audio tracks to a video and export the output to the output folder.

    Args:
        video_filename (str): Filename of the original video inside utils/video/
        audio_files (list): List of audio track dicts (file_path, start_time, end_time relative to utils/audio/)
        output_filename (str): Output file name to be saved inside utils/output/
    """
    # Construct full paths
    video_path = os.path.join("utils", "video", video_filename)
    output_path = os.path.join("utils", "output", output_filename)

    if not audio_files:
        print("No audio files provided. Exiting.")
        return

    # Temporary output
    temp_output = "temp_output_video.mp4"

    filter_complex = []
    inputs = [f"-i {video_path}"] + [
        f"-i utils/audio/{a['file_path']}" for a in audio_files
    ]
    audio_tracks = []

    # Original video audio
    filter_complex.append("[0:a]volume=1.0[a0]")
    audio_tracks.append("[a0]")

    # Add audio overlays
    for i, audio in enumerate(audio_files, start=1):
        start = audio['start_time']
        duration = audio['end_time'] - audio['start_time']

        filter_complex.append(
            f"[{i}:a]aloop=loop=-1:size=2e+09,atrim=0:{duration},asetpts=PTS-STARTPTS,"
            f"adelay={start * 1000}|{start * 1000},volume=0.3[a{i}]"
        )
        audio_tracks.append(f"[a{i}]")

    # Combine audio tracks
    filter_complex.append(
        f"{''.join(audio_tracks)}amix=inputs={len(audio_tracks)}:duration=longest[aout]"
    )

    # Build FFmpeg command
    command = (
        f"ffmpeg {' '.join(inputs)} -filter_complex \"{'; '.join(filter_complex)}\" "
        f"-map 0:v:0 -map \"[aout]\" -c:v copy -c:a aac {temp_output}"
    )

    print("Running FFmpeg command:")
    print(command)

    # Run FFmpeg
    subprocess.run(command, shell=True)

    # Move output to output folder
    if os.path.exists(temp_output):
        os.replace(temp_output, output_path)
        print(f"Final video saved to: {output_path}")
    else:
        print("Error: Temporary output file was not created.")

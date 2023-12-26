from moviepy.editor import VideoFileClip, concatenate_videoclips
from sys import argv

input_video_path=argv[1]
outVide=argv[2]


# List of input video files to be concatenated
#input_video_path = "C:\\Users\\ycrag\\Downloads\\concatenated_video.mp4"

# Initialize a list to store VideoFileClip objects
video_clips = []

# Iterate through each input video file
for i in range(5):
    # Load the video file
    video = VideoFileClip(input_video_path)

    # Append the video clip to the list
    video_clips.append(video)

# Concatenate video clips along with their audio tracks
final_video = concatenate_videoclips(video_clips, method="compose")

# Write the concatenated video to an output file
final_video.write_videofile(outVide, codec='libx264', audio_codec='aac')

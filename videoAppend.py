import cv2

# List of input video files to be appended
input_video_paths = ['C:\\Users\\ycrag\\Downloads\\Relax_Music.mp4', 'C:\\Users\\ycrag\\Downloads\\Relax_Music.mp4']  # Update with your video file paths

# Output video file
output_video_path = 'appended_video.mp4'

# Initialize variables for video properties
frame_width = None
frame_height = None
fps = None

input_video_path = "C:\\Users\\ycrag\\Downloads\\Relax_Music.mp4"
output_video_path = "C:\\Users\\ycrag\\Downloads\\Relax_Music_Out.mp4"


# Iterate through ea:ch input video file\
for i in range(2):
#for input_video_path in input_video_paths:
    # Open the input video file
    input_video = cv2.VideoCapture(input_video_path)

    # Get video properties from the first video file
    if frame_width is None or frame_height is None or fps is None:
        frame_width = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(input_video.get(cv2.CAP_PROP_FPS))

    # Open the output video file in append mode for the first input file
    if input_video_path == input_video_paths[0]:
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Change codec based on your requirement
        output_video = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

    # Read frames from the input video file and write to the output video file
    while True:
        ret, frame = input_video.read()

        if not ret:
            break

        # Write the frame to the output video
        output_video.write(frame)

    # Release the VideoCapture object for the current input video file
    input_video.release()

# Release the VideoWriter object for the output video file
output_video.release()

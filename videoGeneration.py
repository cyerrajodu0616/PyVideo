import cv2

# Input video file
input_video_path = "C:\\Users\\ycrag\\Downloads\\Relax_Music.mp4"

# Output video file
output_video_path = "C:\\Users\\ycrag\\Downloads\\Relax_Music_Out.mp4"

# Open the input video file
input_video = cv2.VideoCapture(input_video_path)

# Get the video properties
frame_width = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(input_video.get(cv2.CAP_PROP_FPS))

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Change codec based on your requirement
output_video = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

while input_video.isOpened():
    ret, frame = input_video.read()

    if not ret:
        break

    # Perform any processing on the frame here (optional)
    # For example, you can apply filters, transformations, etc.

    # Write the processed frame to the output video
    output_video.write(frame)

    # Display the frame (optional)
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture and VideoWriter objects
input_video.release()
output_video.release()

# Close all OpenCV windows
cv2.destroyAllWindows()

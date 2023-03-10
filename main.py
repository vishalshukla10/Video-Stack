import cv2
import numpy as np
import os

# Load two videos
video1 = cv2.VideoCapture('C:\\Users\\vishal\\Desktop\\1st_output_redcliff_message.mp4')
video2 = cv2.VideoCapture('C:\\Users\\vishal\\Desktop\\output_rupali_with_micro.mp4')


# Get frame rate of videos
fps = video1.get(cv2.CAP_PROP_FPS)

# Define transition time in seconds
transition_time = 2.0

# Loop over frames of video 1
while True:
    ret1, frame1 = video1.read()
    if not ret1:
        break

    # Read frame from video 2
    ret2, frame2 = video2.read()
    if not ret2:
        break

    # Resize frame 2 to match frame 1 dimensions
    frame2 = cv2.resize(frame2, (frame1.shape[1], frame1.shape[0]))

    # Display frame from video 1
    cv2.imshow('Video 1', frame1)

    # Calculate alpha for fade-in effect
    i = video1.get(cv2.CAP_PROP_POS_FRAMES)
    alpha = min(1.0, i / (fps * transition_time))

    # Apply fade-in effect
    blended_frame = cv2.addWeighted(frame1, 1 - alpha, frame2, alpha, 0)

    # Display blended frame
    cv2.imshow('Blended Frame', blended_frame)

    # Wait for a key press to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release videos and close windows
#video1.release()
video2.release()
cv2.destroyAllWindows()

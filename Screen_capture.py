import cv2

# Set up the camera
cap = cv2.VideoCapture(0)

# Capture a frame
ret, frame = cap.read()

# Save the frame as an image file
cv2.imwrite("image.png", frame)

# Release the camera
cap.release()

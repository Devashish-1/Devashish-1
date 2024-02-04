import cv2
import numpy as np
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set up the camera
cap = cv2.VideoCapture(0)

while True:
    # Capture each frame from the camera
    ret, frame = cap.read()

    # Flip the frame horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Use a simple thresholding technique for binary image
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

    # Find contours in the binary image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Check for hand gesture (considering only the largest contour)
    if len(contours) > 0:
        max_contour = max(contours, key=cv2.contourArea)

        # Assuming hand gesture when contour area is greater than a threshold
        if cv2.contourArea(max_contour) > 10000:
            # Get the bounding box of the hand
            x, y, w, h = cv2.boundingRect(max_contour)

            # Draw a rectangle around the hand
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Perform gesture recognition based on the bounding box
            # You can implement specific gestures and corresponding actions here

            # For example, display text and speak it aloud
            gesture_text = "Hand Gesture Detected"
            print(gesture_text)
            engine.say(gesture_text)
            engine.runAndWait()

    # Display the frame
    cv2.imshow("Gesture Recognition", frame)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()

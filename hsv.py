#pylint: disable-all
import cv2
import numpy as np

def main():
    # Create the windows
    cv2.namedWindow('color', 1)
    cv2.namedWindow('blue-mask', 1)
    cv2.namedWindow('green', 1)
    cv2.namedWindow('blue', 1)

    # These are just to arrange the windows nicely on your screen
    cv2.moveWindow('color', 635, 00)
    cv2.moveWindow('blue', 1300, 0)
    cv2.moveWindow('green', 635, 500)
    cv2.moveWindow('blue-mask', 1300, 500)

    cap = cv2.VideoCapture(0)

    while True:
        # Read in the image from webcam stream
        ret, frame = cap.read()

		# Convert the color space to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV);

        # HSV bounds for green image
        lower_green = np.array([50, 120, 100])
        upper_green = np.array([85, 255, 255])

        # HSV bounds for blue image
        lower_blue = np.array([90, 120, 100])
        upper_blue = np.array([110, 255, 255])

		# Create a binary image based on the HSV bounds
        green_mask = cv2.inRange(hsv, lower_green, upper_green)
        blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)

		# Overlay binary image with color image from webcam
        green_isolated = cv2.bitwise_and(frame, frame, mask=green_mask)
        blue_isolated = cv2.bitwise_and(frame, frame, mask=blue_mask)

        #Display the images in the window
        cv2.imshow('color', frame)
        cv2.imshow('blue', blue_isolated)
        cv2.imshow('blue-mask', blue_mask)
        cv2.imshow('green', green_isolated)

        # If we press 'q': exit the program
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

main()

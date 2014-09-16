import cv2
import numpy as np

def main():
    # Create the windows
    cv2.namedWindow('color', 1)
    cv2.namedWindow('red', 1)
    cv2.namedWindow('green', 1)
    cv2.namedWindow('blue', 1)

    # These are just to arrange the windows nicely on your screen
    cv2.moveWindow('color', 635, 00)
    cv2.moveWindow('blue', 1300, 0)
    cv2.moveWindow('green', 635, 500)
    cv2.moveWindow('red', 1300, 500)

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        # Create the black and white image
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #ret, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY);

        height, width, depth = frame.shape
        zeros = np.zeros((height, width), np.uint8)

        b, g, r = cv2.split(frame)

        #ret, r = cv2.threshold(r, 200, 255, cv2.THRESH_TOZERO);

        onlyBlue = cv2.merge((b, zeros, zeros))
        onlyGreen = cv2.merge((zeros, g, zeros))
        onlyRed = cv2.merge((zeros, zeros, r))

        cv2.imshow('color', frame)
        #cv2.imshow('gray', thresh)
        cv2.imshow('blue', onlyBlue)
        cv2.imshow('green', onlyGreen)
        cv2.imshow('red', onlyRed)

        # If we press 'q': exit the program
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

main()

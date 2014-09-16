#pylint: disable-all
import cv2
import numpy as np

def main():
    cv2.namedWindow('color', 1)

    cap = cv2.VideoCapture(0)

    while True:
        retVal, frame = cap.read()

        cv2.imshow('color', frame)

        # If we press 'q': exit the program
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

main()

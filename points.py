#pylint: disable-all
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
        # Read in the image from webcam stream
        ret, frame = cap.read()

        # Do some blurring to get rid of the noise
        frame = cv2.GaussianBlur(frame, (3,3), 0)

        # Convert the colorspace to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV);

        # HSV bounds for green image
        lower_green = np.array([50, 80, 60])
        upper_green = np.array([85, 255, 255])

        # HSV bounds for blue image
        lower_blue = np.array([90, 80, 60])
        upper_blue = np.array([120, 255, 255])

        # HSV bounds for green image
        lower_red = np.array([150, 80, 20])
        upper_red = np.array([190, 255, 255])

        # Create a binary image based on the HSV bounds
        green_mask = cv2.inRange(hsv, lower_green, upper_green)
        blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
        red_mask = cv2.inRange(hsv, lower_red, upper_red)

        # Denoise the binary images (remove small dots)
        green_mask = cv2.medianBlur(green_mask, 7)
        blue_mask = cv2.medianBlur(blue_mask, 7)
        red_mask = cv2.medianBlur(red_mask, 7)

        # Overlay binary image with color image from webcam
        green_isolated = cv2.bitwise_and(frame, frame, mask=green_mask)
        blue_isolated = cv2.bitwise_and(frame, frame, mask=blue_mask)
        red_isolated = cv2.bitwise_and(frame, frame, mask=red_mask)

        # Get the contours from the green_mask image
        contours, hierarchy = cv2.findContours(green_mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        # finding contour with maximum area and store it as best_cnt
        max_area = 0
        best_cnt = 0
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > max_area:
                max_area = area
                best_cnt = cnt

        # Print out the centerpoint of the best contour
        M = cv2.moments(best_cnt)
        if int(M['m00']) != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            #print str(cx) + ', ' + str(cy)
            if cx > 0 and cy > 0:
                cv2.circle(green_isolated, (cx, cy), 5, (0, 255, 255), -1)

        # Get the contours from the blue_mask image
        contours, hierarchy = cv2.findContours(blue_mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        # finding contour with maximum area and store it as best_cnt
        max_area = 0
        best_cnt = 0
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > max_area:
                max_area = area
                best_cnt = cnt

        # Print out the centerpoint of the best contour
        M = cv2.moments(best_cnt)
        if int(M['m00']) != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            #print str(cx) + ', ' + str(cy)
            if cx > 0 and cy > 0:
                cv2.circle(blue_isolated, (cx, cy), 5, (0, 255, 255), -1)

        # Get the contours from the red_mask image
        contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        # finding contour with maximum area and store it as best_cnt
        max_area = 0
        best_cnt = 0
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > max_area:
                max_area = area
                best_cnt = cnt

        # Print out the centerpoint of the best contour
        M = cv2.moments(best_cnt)
        if int(M['m00']) != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            #print str(cx) + ', ' + str(cy)
            if cx > 0 and cy > 0:
                cv2.circle(red_isolated, (cx, cy), 5, (0, 255, 255), -1)

        #Display the images in the window
        cv2.imshow('color', frame)
        cv2.imshow('blue', blue_isolated)
        cv2.imshow('green', green_isolated)
        cv2.imshow('red', red_isolated)

        # If we press 'q': exit the program
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

main()

import cv2
import time
import hand_detector



def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = hand_detector.hand_detector()

    while True:
        sucsess, img = cap.read()
        img = detector.find_hands(img)
        # Gives us the current time
        cTime = time.time()
        fps = 1 / (cTime - pTime)  # This is for calculating the FPS
        pTime = cTime
        lm_list = detector.find_pos(img, draw=False)
        # print out specific landmark
        if len(lm_list) != 0:
            print(lm_list[0])
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
        cv2.imshow("image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
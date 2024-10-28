import cv2
import time
import math as math
import hand_tracking as ht

def main():
        ctime=0
        ptime=0
        url = "http://192.168.2.9:4747/video?type=some.mjpeg"
        cap = cv2.VideoCapture(url)
        detector = ht.HandTrackingDynamic()
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        if not cap.isOpened():
            print("Cannot open camera")
            exit()

        while True:
            ret, frame = cap.read()

            frame = detector.findFingers(frame)
            lmsList = detector.findPosition(frame)
            if len(lmsList)!=0:
                print(lmsList[0])

            ctime = time.time()
            fps =1/(ctime-ptime)
            ptime = ctime

            cv2.putText(frame, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
 
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame', gray)
            cv2.waitKey(1)


                
if __name__ == "__main__":
            main()
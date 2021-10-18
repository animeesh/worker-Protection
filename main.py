import cv2
import datetime
import imutils

#image =cv2.imread("books.jpg")
def main():
    cap = cv2.VideoCapture("Untitled (2).mp4")
    fps_start_time=datetime.datetime.now()
    fps = 0
    total_frame = 0

    while True:
        ret,frame = cap.read()
        frame = imutils.resize(frame,width=800)
        total_frame=total_frame+1

        fps_end= datetime.datetime.now()
        time_diff= fps_end-fps_start_time
        if time_diff.seconds ==0:
            fps =0.0
        else:
            fps= (total_frame/time_diff.seconds)


        text="fps: {:.2f}".format(fps)
        cv2.putText(frame,text,(5,30),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),1)
        cv2.imshow("Application", frame)
        #cv2.rectangle(frame,(50,50),(500,500),(0,0,255),2)

        key = cv2.waitKey(1)
        if key ==ord("q"):
            break

    cv2.destroyAllWindows()

main()
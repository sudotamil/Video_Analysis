import cv2
import os

def extractFrames(pathIn, pathOut):
    #os.mkdir(pathOut)

    cap = cv2.VideoCapture(pathIn)
    count = 0

    while (cap.isOpened()):

        # Capture frame-by-frame
        ret, frame = cap.read()

        if ret == True:
            print('Read %d frame: ' % count, ret)
            cv2.imwrite(os.path.join(pathOut, "frame{:d}.jpg".format(count)), frame)  # save frame as JPEG file
            count += 1
        else:
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

def main():
    extractFrames('/home/bigtapp/projects/MY_Project/SampleVideo_1280x720_2mb.mp4', '/home/bigtapp/projects/MY_Project/frames')

if __name__=="__main__":
    main()

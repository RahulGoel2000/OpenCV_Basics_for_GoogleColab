#reading video

import cv2
vid = cv2.VideoCapture("samples/team.mp4")
#write 0 or 1 in place of URL if you want to the live feed of your laptop or webcam

while True:
  success, img = vid.read()
  cv2.imshow("Video",img)

  if cv2.waitKey(1) & 0xFF==ord('q'):
    break


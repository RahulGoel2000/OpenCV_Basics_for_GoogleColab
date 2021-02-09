#reading image

import cv2
img = cv2.imread("samples/team.jpg")

cv2.imshow("Team_Averea",img)
cv2.waitKey(0)

plt.imshow(img)
plt.show()

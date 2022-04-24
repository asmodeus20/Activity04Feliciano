import cv2
filePath = 'wazup.png'
imgFlag = int(1) 
img = cv2.imread(filePath,imgFlag)
cv2.imshow("meowww",img)
cv2.waitKey(0)
cv2.destroyAllWindows()